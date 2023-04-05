from gradient_1 import gradient_method, nabla_calculate


class N_D_Problem:
    def __init__(self):
        self.variables_amount = 2
        # self.target_function_str = '2*(X[0] + X[1])**2 + 3*X[1]'
        self.target_function_str = '4 * X[0] + X[1] + 4 * (1 + 3 * X[0] ** 2 + X[1] ** 2) ** (1/2)'
        self.target_function = lambda X: eval(self.target_function_str)
        self.nabla_vector = []

    gradient_method = gradient_method
    nabla_calculate = nabla_calculate


