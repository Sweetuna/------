
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

