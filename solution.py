import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #alpha = 1 - p
    a1 = (1 - p)/2
    a2 = (1 + p)/2
    return (x.max() - 0.023)/(a2**(1/len(x))) + 0.023,\
           (x.max() - 0.023)/(a1**(len(x))) + 0.023
