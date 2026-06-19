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
