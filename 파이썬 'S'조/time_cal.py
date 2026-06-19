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

