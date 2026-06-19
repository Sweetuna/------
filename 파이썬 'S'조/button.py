
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


