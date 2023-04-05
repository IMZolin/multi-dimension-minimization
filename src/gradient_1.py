from sympy import *
from One_D_Problem_file import One_D_Problem


def nabla_calculate(self):
    """
    эта функция должна отрабатывать один раз и возвращать спиок строк = выражения, которые надо вычислить
    """
    function = self.target_function_str
    X = []
    for i in range(self.variables_amount):
        X.append(Symbol(f'X[{i}]'))
    for i in range(self.variables_amount):
        self.nabla_vector.append(str(eval(function).diff(X[i])))


def gradient_method(self, accuracy, X0, one_d_method):
    X = X0
    while True:  # условие на норму
        # grad_f_k = [eval(x) for x in self.nabla_vector]  # ЗНАЧЕНИЯ градиента на к-м шаге
        grad_f_k = []
        for item in self.nabla_vector:
            grad_f_k.append(eval(item))

        #  создаем и решаем задачу минимизации
        p = One_D_Problem()
        p.left_border = 0
        p.right_border = 1
        p.target_function = lambda alfa: self.target_function([X[i] - alfa * grad_f_k[i] for i in range(len(X))])
        alfa_k = one_d_method(p, accuracy)[0]
        print('Yo')

        X = [X[i] - alfa_k * grad_f_k[i] for i in range(len(X))]

        print('UwU')



