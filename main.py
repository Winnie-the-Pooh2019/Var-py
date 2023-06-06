import numpy as np
from scipy.stats import norm

average = 61
dispersion = 1.35
stocks = np.random.normal(average, dispersion, 250)
profit = [(stocks[i + 1] - stocks[i]) / stocks[i] for i in range(len(stocks) - 1)]
average_profit = np.mean(profit)
std_profit = np.std(profit)
print(f'''Математическое ожидание = {average_profit}
Стандартное отклонение = {std_profit}''')


def var_gen(a):
    print(f'''\n\nУстановим уровень значимости a = {a}:''')

    quantile = norm.ppf(a, loc=average_profit, scale=std_profit)
    print(f'Квантиль = {quantile}')
    min_price_1 = (quantile + 1) * average
    min_price_5 = (quantile * (5 ** 0.5) + 1) * average
    print(f'''
    Минимальная стоимость актива в следующем временном периоде = {min_price_1}
    Минимальная стоимость актива через 5  временных периодов = {min_price_5}''')
    var_1 = (min_price_1 - stocks[-1]) / (stocks[-1] / 100)
    var_5 = (min_price_5 - stocks[-1]) / (stocks[-1] / 100)
    print(f'''
    VAR на следующий период времени = {var_1}
    VAR через 5 периодов = {var_5}''')

    return var_1, var_5


v11, v15 = var_gen(0.01)
v21, v25 = var_gen(0.05)
