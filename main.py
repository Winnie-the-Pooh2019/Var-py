import numpy as np
from scipy.stats import norm

average = 61
dispersion = 1.35

stocks = norm.random.normal(average, dispersion, 250)

profit = [(stocks[i + 1] - stocks[i]) / stocks[i] for i in range(len(stocks) - 1)]
average_profit = np.mean(profit)
std_profit = np.std(profit)
quantile = norm.pdf(0.01, loc=average_profit, scale=std_profit)

print(f'''Математическое ожидание = {average_profit}
Стандартное отклонение = {std_profit}
Квантиль = {quantile}''')
