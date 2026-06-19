import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, TextBox
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import platform

# =========================================================
# 한글 폰트 및 마이너스 기호 설정
# =========================================================
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
else:
    plt.rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False


# =========================================================
# 1. 현재 시간 불러오기
# =========================================================

KST = ZoneInfo("Asia/Seoul")
BASE_DATE = datetime(2026, 1, 1, tzinfo=KST)

current_date = datetime.now(KST)
elapsed_days = (current_date - BASE_DATE).total_seconds() / 86400


# =========================================================
# 2. 행성 데이터 준비 (출처: NASA Planetary Fact Sheet)
# rotation_period: 자전주기 (지구 일 기준)
# real_radius: 실제 적도 반경 (km)
# =========================================================

planets = [
    {"name": "Mercury", "radius": 0.4, "period": 88, "size": 30, "color": "gray", "initial_angle": 0, "rotation_period": 58.65, "real_radius": 2439.7},
    {"name": "Venus", "radius": 0.7, "period": 225, "size": 50, "color": "orange", "initial_angle": 45, "rotation_period": 243.02, "real_radius": 6051.8},
    {"name": "Earth", "radius": 1.0, "period": 365, "size": 60, "color": "blue", "initial_angle": 90, "rotation_period": 0.99, "real_radius": 6371.0},
    {"name": "Mars", "radius": 1.5, "period": 687, "size": 45, "color": "red", "initial_angle": 135, "rotation_period": 1.03, "real_radius": 3389.5},
    {"name": "Jupiter", "radius": 2.3, "period": 4333, "size": 120, "color": "brown", "initial_angle": 180, "rotation_period": 0.41, "real_radius": 69911.0},
    {"name": "Saturn", "radius": 3.0, "period": 10759, "size": 100, "color": "gold", "initial_angle": 225, "rotation_period": 0.44, "real_radius": 58232.0},
    {"name": "Uranus", "radius": 3.7, "period": 30687, "size": 80, "color": "lightblue", "initial_angle": 270, "rotation_period": 0.72, "real_radius": 25362.0},
    {"name": "Neptune", "radius": 4.4, "period": 60190, "size": 80, "color": "darkblue", "initial_angle": 315, "rotation_period": 0.67, "real_radius": 24622.0},
]


# =========================================================
# 3. 계산 함수
# =========================================================

def get_planet_angle(planet, days):
    angle = np.radians(planet["initial_angle"]) + 2 * np.pi * days / planet["period"]
    return angle % (2 * np.pi)


def get_planet_position(planet, days):
    angle = get_planet_angle(planet, days)
    r = planet["radius"]

    x = r * np.cos(angle)
    y = r * np.sin(angle)

    return x, y


def get_angle_from_position(x, y):
    return np.arctan2(y, x) % (2 * np.pi)


def get_angle_difference(a, b):
    return abs(np.angle(np.exp(1j * (a - b))))


# =========================================================
# 4. 상태 변수
# =========================================================

speed = 1.0
paused = False
time_direction = 1

dragging_planet = None
target_angles = {}

calculated_date = None
calculated_elapsed_days = None

planet_points = {}
planet_texts = {}
target_points = {}
coordinate_texts = {}

tutorial_fig = None
tutorial_exit_button = None


# =========================================================
# 5. 화면 구성
# =========================================================

fig, (sim_ax, info_ax) = plt.subplots(
    1,
    2,
    figsize=(14, 8),
    gridspec_kw={"width_ratios": [3, 1]}
)

plt.subplots_adjust(bottom=0.25)

sim_ax.set_xlim(-5, 5)
sim_ax.set_ylim(-5, 5)
sim_ax.set_aspect("equal")
sim_ax.set_facecolor("black")
sim_ax.set_title("Planet Orbit Simulation")

info_ax.set_xlim(0, 1)
info_ax.set_ylim(0, 1)
info_ax.axis("off")
info_ax.set_title("Planet Data")

# 태양
sim_ax.scatter(0, 0, s=350, color="yellow")
sim_ax.text(0.1, 0.1, "Sun", color="white", fontsize=9)

# 궤도
theta = np.linspace(0, 2 * np.pi, 500)

for planet in planets:
    r = planet["radius"]
    sim_ax.plot(
        r * np.cos(theta),
        r * np.sin(theta),
        color="white",
        linewidth=0.5
    )

# 행성 객체 생성
for i, planet in enumerate(planets):
    name = planet["name"]
    x, y = get_planet_position(planet, elapsed_days)

    point = sim_ax.scatter(x, y, s=planet["size"], color=planet["color"])
    name_text = sim_ax.text(x + 0.08, y + 0.08, name, color="white", fontsize=8)

    target_point = sim_ax.scatter(
        [],
        [],
        s=planet["size"] * 1.6,
        facecolors="none",
        edgecolors="lime",
        linewidths=1.5
    )

    coord_text = info_ax.text(
        0.05,
        0.92 - i * 0.105,
        "",
        color="black",
        fontsize=10,
        family="monospace"
    )

    planet_points[name] = point
    planet_texts[name] = name_text
    target_points[name] = target_point
    coordinate_texts[name] = coord_text

result_text = info_ax.text(
    0.05,
    0.03,
    "",
    color="green",
    fontsize=10,
    family="monospace"
)


clicked_info_text = fig.text(
    0.01, 0.40,
    "행성을 클릭하면\n정보가 표시됩니다.",
    color="black",
    fontsize=10,
    va="top",
    fontweight="bold"
)


# =========================================================
# 6. 입력창
# =========================================================

date_ax = plt.axes([0.10, 0.10, 0.22, 0.05])
date_box = TextBox(date_ax, "Date", initial=current_date.strftime("%Y-%m-%d"))

speed_ax = plt.axes([0.10, 0.03, 0.22, 0.05])
speed_box = TextBox(speed_ax, "Speed", initial=str(speed))


def submit_date(text):
    global current_date, elapsed_days

    try:
        current_date = datetime.strptime(text, "%Y-%m-%d").replace(tzinfo=KST)
        elapsed_days = (current_date - BASE_DATE).total_seconds() / 86400

        result_text.set_text(f"Date changed:\n{current_date.strftime('%Y-%m-%d')}")

        update_screen()
        fig.canvas.draw_idle()

    except ValueError:
        result_text.set_text("Invalid date.\nUse YYYY-MM-DD.")
        fig.canvas.draw_idle()


def submit_speed(text):
    global speed

    try:
        speed = float(text)
        result_text.set_text(f"Speed changed:\n{speed}")
        fig.canvas.draw_idle()

    except ValueError:
        result_text.set_text("Invalid speed.")
        fig.canvas.draw_idle()


date_box.on_submit(submit_date)
speed_box.on_submit(submit_speed)


# =========================================================
# 7. 화면 업데이트
# =========================================================

def update_screen():
    for planet in planets:
        name = planet["name"]

        x, y = get_planet_position(planet, elapsed_days)

        planet_points[name].set_offsets([[x, y]])
        planet_texts[name].set_position((x + 0.08, y + 0.08))

        if name in target_angles:
            target_angle = target_angles[name]
            r = planet["radius"]

            target_x = r * np.cos(target_angle)
            target_y = r * np.sin(target_angle)

            dx = target_x - x
            dy = target_y - y

            displacement = np.sqrt(dx ** 2 + dy ** 2)

            coordinate_texts[name].set_text(
                f"{name:<8} x={x:>6.2f} y={y:>6.2f}\n"
                f"         target=({target_x:>5.2f},{target_y:>5.2f})\n"
                f"         disp={displacement:>6.2f}"
            )

        else:
            coordinate_texts[name].set_text(
                f"{name:<8} x={x:>6.2f} y={y:>6.2f}"
            )


# =========================================================
# 8. 키보드 입력 처리
# =========================================================

def on_key(event):
    global speed, paused, time_direction

    if event.key == " ":
        paused = not paused

    elif event.key == "up":
        speed *= 2

    elif event.key == "down":
        speed /= 2

    elif event.key == "right":
        speed += 1

    elif event.key == "left":
        speed -= 1

    elif event.key == "r":
        time_direction *= -1

    speed_box.set_val(str(speed))

    direction_text = "forward" if time_direction == 1 else "reverse"
    result_text.set_text(f"speed={speed}\npaused={paused}\ntime={direction_text}")

    fig.canvas.draw_idle()


fig.canvas.mpl_connect("key_press_event", on_key)


# =========================================================
# 9. 행성 직접 조정: 마우스 드래그 및 클릭 시 정보 갱신
# =========================================================

def on_press(event):
    global dragging_planet

    if event.inaxes != sim_ax:
        return

    if event.xdata is None or event.ydata is None:
        return

    click_x = event.xdata
    click_y = event.ydata

    closest_name = None
    closest_distance = float("inf")

    for planet in planets:
        name = planet["name"]
        px, py = planet_points[name].get_offsets()[0]

        distance = np.sqrt((click_x - px) ** 2 + (click_y - py) ** 2)

        if distance < closest_distance:
            closest_distance = distance
            closest_name = name

    if closest_distance < 0.25:
        dragging_planet = closest_name
        
        # 클릭한 행성의 데이터를 찾아 텍스트 갱신
        planet_data = next(p for p in planets if p["name"] == dragging_planet)
        
        info_str = (
            f"--- {planet_data['name']} ---\n"
            f"공전주기: {planet_data['period']} 일\n"
            f"자전주기: {planet_data['rotation_period']} 지구 일\n"
            f"크기(반경): {planet_data['real_radius']:,.1f} km\n"
        )
        clicked_info_text.set_text(info_str)
        fig.canvas.draw_idle()


def on_motion(event):
    if dragging_planet is None:
        return

    if event.inaxes != sim_ax:
        return

    if event.xdata is None or event.ydata is None:
        return

    planet = next(p for p in planets if p["name"] == dragging_planet)

    new_angle = get_angle_from_position(event.xdata, event.ydata)
    target_angles[dragging_planet] = new_angle

    r = planet["radius"]
    x = r * np.cos(new_angle)
    y = r * np.sin(new_angle)

    target_points[dragging_planet].set_offsets([[x, y]])

    result_text.set_text(f"Target set:\n{dragging_planet}")
    update_screen()
    fig.canvas.draw_idle()


def on_release(event):
    global dragging_planet
    dragging_planet = None


fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("motion_notify_event", on_motion)
fig.canvas.mpl_connect("button_release_event", on_release)


# =========================================================
# 10. 목표 형태까지 걸리는 시간 계산
# =========================================================

def find_closest_time_to_target(max_days=70000, step=5):
    if not target_angles:
        return None, None

    best_day = None
    best_error = float("inf")

    for future_day in np.arange(0, max_days + step, step):
        total_error = 0

        for planet in planets:
            name = planet["name"]

            if name in target_angles:
                predicted_angle = get_planet_angle(planet, elapsed_days + future_day)
                target_angle = target_angles[name]

                total_error += get_angle_difference(predicted_angle, target_angle)

        if total_error < best_error:
            best_error = total_error
            best_day = future_day

    return best_day, best_error


def calculate_target_time(event):
    global calculated_date, calculated_elapsed_days

    if not target_angles:
        result_text.set_text("Drag planet first.")
        fig.canvas.draw_idle()
        return

    best_day, best_error = find_closest_time_to_target()

    calculated_date = current_date + timedelta(days=float(best_day))
    calculated_elapsed_days = (calculated_date - BASE_DATE).total_seconds() / 86400

    result_text.set_text(
        f"Closest match:\n"
        f"+{best_day:.0f} days\n"
        f"{calculated_date.strftime('%Y-%m-%d')}\n"
        f"error={best_error:.3f}"
    )

    fig.canvas.draw_idle()


# =========================================================
# 11. 버튼
# =========================================================

calc_ax = plt.axes([0.38, 0.10, 0.18, 0.05])
calc_button = Button(calc_ax, "Calculate")
calc_button.on_clicked(calculate_target_time)


goto_ax = plt.axes([0.58, 0.10, 0.18, 0.05])
goto_button = Button(goto_ax, "Go To Date")


def move_to_calculated_date(event):
    global current_date, elapsed_days, paused

    if calculated_date is None or calculated_elapsed_days is None:
        result_text.set_text("Calculate first.")
        fig.canvas.draw_idle()
        return

    current_date = calculated_date
    elapsed_days = calculated_elapsed_days
    paused = True

    date_box.set_val(current_date.strftime("%Y-%m-%d"))

    result_text.set_text(
        f"Moved to:\n{current_date.strftime('%Y-%m-%d')}"
    )

    update_screen()
    fig.canvas.draw_idle()


goto_button.on_clicked(move_to_calculated_date)


reset_ax = plt.axes([0.38, 0.03, 0.18, 0.05])
reset_button = Button(reset_ax, "Reset")


def reset_simulation(event):
    global current_date, elapsed_days, speed, paused, time_direction
    global calculated_date, calculated_elapsed_days

    current_date = datetime.now(KST)
    elapsed_days = (current_date - BASE_DATE).total_seconds() / 86400

    speed = 1.0
    paused = False
    time_direction = 1

    calculated_date = None
    calculated_elapsed_days = None

    target_angles.clear()

    for name in target_points:
        target_points[name].set_offsets(np.empty((0, 2)))

    date_box.set_val(current_date.strftime("%Y-%m-%d"))
    speed_box.set_val(str(speed))

    result_text.set_text("Simulation reset.")
    clicked_info_text.set_text("행성을 클릭하면\n정보가 표시됩니다.")

    update_screen()
    fig.canvas.draw_idle()


reset_button.on_clicked(reset_simulation)


reverse_ax = plt.axes([0.58, 0.03, 0.18, 0.05])
reverse_button = Button(reverse_ax, "Reverse")


def reverse_time(event):
    global time_direction

    time_direction *= -1

    direction_text = "forward" if time_direction == 1 else "reverse"
    result_text.set_text(f"Time direction:\n{direction_text}")

    fig.canvas.draw_idle()


reverse_button.on_clicked(reverse_time)


# --- 튜토리얼 팝업 및 버튼 구현부 ---

def show_tutorial(event):
    global tutorial_fig, tutorial_exit_button
    
    if tutorial_fig is not None and plt.fignum_exists(tutorial_fig.number):
        return
        
    tutorial_fig = plt.figure(figsize=(6, 5))
    tutorial_fig.canvas.manager.set_window_title("Tutorial")
    
    tut_ax = tutorial_fig.add_axes([0, 0, 1, 1])
    tut_ax.axis("off")
    
    tutorial_text = (
        "Date: 날짜 직접 입력\n"
        "Speed: 속도 직접 입력\n"
        "Calculate: 초록색 목표 위치와 가장 가까워지는 날짜 계산\n"
        "Go To Date: 계산된 날짜로 이동\n"
        "Reset: 초기화\n"
        "Reverse: 시간 진행 방향 반전\n\n"
        "SPACE: 일시정지 / 재생\n"
        "↑: 속도 2배\n"
        "↓: 속도 절반\n"
        "→: 속도 +1\n"
        "←: 속도 -1\n"
        "R: 시간 방향 반전"
    )
    
    tut_ax.text(
        0.5, 0.55, tutorial_text,
        ha="center", va="center", fontsize=11
    )
    
    exit_ax = tutorial_fig.add_axes([0.4, 0.05, 0.2, 0.08])
    tutorial_exit_button = Button(exit_ax, "exit")
    
    def close_tutorial(event):
        plt.close(tutorial_fig)
        
    tutorial_exit_button.on_clicked(close_tutorial)
    tutorial_fig.show()


tutorial_ax = plt.axes([0.01, 0.17, 0.08, 0.05])
tutorial_button = Button(tutorial_ax, "Tutorial")
tutorial_button.on_clicked(show_tutorial)


# =========================================================
# 12. 애니메이션
# =========================================================

def update(frame):
    global elapsed_days, current_date

    if not paused:
        elapsed_days += speed * time_direction
        current_date = BASE_DATE + timedelta(days=float(elapsed_days))

        if frame % 10 == 0:
            date_box.set_val(current_date.strftime("%Y-%m-%d"))

    update_screen()

    return (
        list(planet_points.values())
        + list(planet_texts.values())
        + list(target_points.values())
        + list(coordinate_texts.values())
        + [result_text, clicked_info_text]
    )


ani = FuncAnimation(
    fig,
    update,
    interval=50,
    blit=False
)

update_screen()
plt.show()