import numpy as np
from sympy import *
from One_D_Problem_file import One_D_Problem



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


def gradient_method_DFP(self, accuracy, X0, one_d_method):
    X = X0
    self.X_step_points_array = []
    Hessian = np.eye(len(X0))  # инициализируем гессиан единичной матрицей
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
        p.target_function = lambda alfa: self.target_function([X[i] - alfa * np.matmul(Hessian, grad_f_k)[i] for i in range(len(X))])
        alfa_k = one_d_method(p, accuracy)[0]

        #  вычисляем ЗНАЧЕНИЯ градиента в точке Х_k+1
        #  для этого запомним X в новую переменную, а на место X поставим X_k+1 (чтобы eval работал с X)
        X_old = X.copy()
        X = [X[i] - alfa_k * np.matmul(Hessian, grad_f_k)[i] for i in range(len(X))]
        grad_f_k_plus_1 = []
        for item in self.nabla_vector:
            grad_f_k_plus_1.append(eval(item))

        #  теперь обновляем Гессиан
        delta_X = [X[i] - X_old[i] for i in range(len(X))]  # правильный порядок?
        y = delta_X
        delta_g = [grad_f_k_plus_1[i] - grad_f_k[i] for i in range(len(X))]
        z = np.matmul(Hessian, delta_g)
        w = 1

        delta_Hessian = (1 / w) * (np.outer(delta_X, y) / (np.dot(y, delta_g))) - np.outer((np.dot(Hessian, delta_g)), z) / (np.dot(z, delta_g))
        Hessian = w * (Hessian + delta_Hessian)



        #  проверка на решение
        if norma_calculate(grad_f_k) < accuracy:
            return self.X_step_points_array


