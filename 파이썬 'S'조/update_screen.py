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
