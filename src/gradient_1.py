from sympy import *
from One_D_Problem_file import One_D_Problem
import numpy as np


def nabla_calculate(self):
    """эта функция должна отрабатывать один раз и возвращать спиок символьных частных производных"""
    function = self.target_function_str
    X = []
    for i in range(self.variables_amount):
        X.append(Symbol(f'X[{i}]'))
    for i in range(self.variables_amount):
        self.nabla_vector.append(str(eval(function).diff(X[i])))


def norma_calculate(vector):
    pow_sum = 0
    for item in vector:
        pow_sum += pow(item, 2)
    return sqrt(pow_sum)


def gradient_method(self, accuracy, X0, one_d_method):
    X = X0
    self.X_step_points_array = []
    while True:
        #  вычисляем ЗНАЧЕНИЯ градиента в точке Х
        grad_f_k = []
        for item in self.nabla_vector:
            grad_f_k.append(eval(item))

        """
        ВОТ ЗДЕСЬ, Я ПРЕДПОЛАГАЮ, НАДО ЗАПОМИНАТЬ ТОЧКИ (X), КОТОРЫЕ ПОТОМ НАДО ВЫВОДИТЬ НА ГРАФИКАХ.
        МОЖНО ВЕРНУТЬ ИХ МАССИВ ИЗ МЕТОДА И ПОТОМ ОТДЕЛЬНЫМ МЕТОДОМ ОТРИСОВЫВАТЬ. ТАК ЛОГИЧНЕЕ:
        """
        print([round(X[i], 5) for i in range(len(X))])
        self.X_step_points_array.append(X)

        #  создаем и решаем задачу минимизации
        p = One_D_Problem()
        p.left_border = 0
        p.right_border = 1
        p.target_function = lambda alfa: self.target_function([X[i] - alfa * grad_f_k[i] for i in range(len(X))])
        alfa_k = one_d_method(p, accuracy)[0]

        #  k -> k + 1
        X = [X[i] - alfa_k * grad_f_k[i] for i in range(len(X))]

        #  проверка на решение
        if norma_calculate(grad_f_k) < accuracy:
            return self.X_step_points_array


def gradient_method_store_metrics(self, accuracy, X0, one_d_method, x_star):
    """
    Дополнительная функция для вычислений разных характиристик. Принципиально для решения не нужна
    """
    X = X0
    self.X_step_points_array = []
    m = 0.5
    M = 12
    col2 = []
    col4 = []
    # alfa0 = 6
    while True:
        #  вычисляем ЗНАЧЕНИЯ градиента в точке Х
        grad_f_k = []
        for item in self.nabla_vector:
            grad_f_k.append(eval(item))

        """
        ВОТ ЗДЕСЬ, Я ПРЕДПОЛАГАЮ, НАДО ЗАПОМИНАТЬ ТОЧКИ (X), КОТОРЫЕ ПОТОМ НАДО ВЫВОДИТЬ НА ГРАФИКАХ.
        МОЖНО ВЕРНУТЬ ИХ МАССИВ ИЗ МЕТОДА И ПОТОМ ОТДЕЛЬНЫМ МЕТОДОМ ОТРИСОВЫВАТЬ. ТАК ЛОГИЧНЕЕ:
        """
        self.X_step_points_array.append(X)

        #  создаем и решаем задачу минимизации
        p = One_D_Problem()
        p.left_border = 0
        p.right_border = 1
        p.target_function = lambda alfa: self.target_function([X[i] - alfa * grad_f_k[i] for i in range(len(X))])
        alfa_k = one_d_method(p, accuracy)[0]

        x = np.array(X)
        r = norma_calculate(grad_f_k)
        col2.append(norma_calculate(grad_f_k))
        col4.append(1 - alfa_k * accuracy * m * (1 + m / M))

        #  k -> k + 1
        # print(X)
        X = [X[i] - alfa_k * grad_f_k[i] for i in range(len(X))]

        #  проверка на решение
        if norma_calculate(grad_f_k) < accuracy:
            return col2, col4



