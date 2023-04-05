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


def gradient_method(self, accuracy, X0, one_d_method):
    X = X0
    X_step_points_array = []
    while True:
        #  вычисляем ЗНАЧЕНИЯ градиента в точке Х
        grad_f_k = []
        for item in self.nabla_vector:
            grad_f_k.append(eval(item))

        """
        ВОТ ЗДЕСЬ, Я ПРЕДПОЛАГАЮ, НАДО ЗАПОМИНАТЬ ТОЧКИ (X), КОТОРЫЕ ПОТОМ НАДО ВЫВОДИТЬ НА ГРАФИКАХ.
        МОЖНО ВЕРНУТЬ ИХ МАССИВ ИЗ МЕТОДА И ПОТОМ ОТДЕЛЬНЫМ МЕТОДОМ ОТРИСОВЫВАТЬ. ТАК ЛОГИЧНЕЕ:
        """
        X_step_points_array.append(X)

        #  создаем и решаем задачу минимизации
        p = One_D_Problem()
        p.left_border = 0
        p.right_border = 1
        p.target_function = lambda alfa: self.target_function([X[i] - alfa * grad_f_k[i] for i in range(len(X))])
        alfa_k = one_d_method(p, accuracy)[0]

        #  k -> k + 1
        print(X)
        X = [X[i] - alfa_k * grad_f_k[i] for i in range(len(X))]

        #  проверка на решение
        if norma_calculate(grad_f_k) < accuracy:
            return X_step_points_array



