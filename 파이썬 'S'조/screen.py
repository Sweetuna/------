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
