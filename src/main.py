from multidimensional_problem import N_D_Problem
from Trial_Point_Method_file import trial_point_method
from golden_egg import golden_search
import numpy as np
import matplotlib.pyplot as plot
from gradient_1 import norma_calculate, nabla_calculate, gradient_method_store_metrics

"""
ИСПОЛЬЗОВАНИЕ:
1) ОПРЕДЕЛИТЬ ФУНКЦИЮ И КОЛИЧЕСТВО ПЕРЕМЕННЫХ В class N_D_Problem
2) ИЗМЕНИТЬ НАЧАЛЬНОЕ ПРИБЛИЖЕНИЕ В ЦИКЛЕ В main
3) ДОБАВИТЬ ЕСЛИ НАДО ВЫПОЛНЕНИЕ ПРОГРАММЫ ДЛЯ РАЗНЫХ ТОЧНОСТЕЙ В ТОМ ЖЕ ЦИКЛЕ
"""


def scalar(array_x):
    """
    используем для подтверждения
    ортогональности звеньев"""
    scalar_mult = []
    arr = np.array(array_x)
    for i in range(len(array_x) - 2):
        ans = np.dot(arr[i+1] - arr[i], arr[i+2] - arr[i+1])
        scalar_mult.append(ans)

    return scalar_mult


if __name__ == '__main__':
    pr1 = N_D_Problem()
    pr1.nabla_calculate()  # ОБЯЗАТЕЛЬНО ЗАПУСКАТЬ В НАЧАЛЕ ПРОГРАММЫ, ЕСЛИ БУДЕМ ИСПОЛЬЗОВАТЬ СИМВОЛЬНЫЕ ВЫЧИСЛЕНИЯ

    for acc in [0.0001]:
        t0 = [0.0, 0.0, 0.0]
        print('GOLDEN SEARCH:', acc)
        x = pr1.gradient_method(acc, t0, golden_search)
        print(scalar(x))

        print('TPM:', acc)
        y = pr1.gradient_method(acc, t0, trial_point_method)
        print(scalar(y))

        print('DFP', acc)
        z = pr1.gradient_method_DFP(acc, t0, trial_point_method)
        print(scalar(z))
















