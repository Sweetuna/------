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
