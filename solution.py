import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #alpha = 1 - p
    a1 = p**(1/len(x))
    l = np.max(x)
    r = (np.max(x)-0.023)/a1 + 0.023

    return l, r
