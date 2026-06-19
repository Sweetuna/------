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