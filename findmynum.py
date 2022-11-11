# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:29:37 2022

@author: Acer
"""

import random

my_num = random.randint(0, 20)

print("Raqam topish o'yinini o'ynaymiz")
savol = "Istalgan raqamni kiriting?(to'xtatish uchun 0 ni bosing): "
while True:
    ask = int(input(savol))
    if my_num > ask:
        print("Kattaroq raqam o'ylang")
    if my_num < ask:
        print("Kichikroq raqam o'ylang")
    else:
        print(f"Tabrikl0ayman siz topdingiz siz o'ylagan raqam {ask} edi")
        break
print("Dastur tugadi")