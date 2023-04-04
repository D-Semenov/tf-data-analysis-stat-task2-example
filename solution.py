import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p 
    return (np.max(x)+np.min(x))/2,\
           ((np.max(x)+np.min(x))/2)/(alpha**(1/len(x)))
