# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x = 0
for i in range(10):
    start_point = sd.get_point(50 + x, 50 + x)
    end_point = sd.get_point(100 + x, 100 + x)
    sd.rectangle(left_bottom=start_point, right_top=end_point, width=2)
    x += 20

sd.pause()
