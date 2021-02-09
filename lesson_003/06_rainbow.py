# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x = 0
for i in rainbow_colors:
    start_point = sd.get_point(50 + x, 50 + x)
    end_point = sd.get_point(350 + x, 450 + x)
    sd.line(start_point=start_point, end_point=end_point, color=i, width=5)
    x += 20


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(100,10)
radius = 500
for i in rainbow_colors:
    radius += 5
    sd.circle(center_position=point, radius=radius, color=i, width=5)

sd.pause()
