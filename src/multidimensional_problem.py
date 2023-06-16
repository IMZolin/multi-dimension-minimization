from gradient_1 import gradient_method, nabla_calculate
from gradient_DFP import *
from graphics import draw_contoures_full, draw_contoures



class N_D_Problem:
    def __init__(self):
        # число переменных в целевой функции:
        self.variables_amount = 3
        # строковфй формат ц.ф (нужен для символьного вычисления производной):
        self.target_function_str = 'X[0] + X[1] + 0.5*X[2] + 3 * (1 + 3 * X[0] ** 2 + X[1] ** 2 + X[2] ** 2) ** (1/2)'
        #  eval - вычисляет строковое значение
        self.target_function = lambda X: eval(self.target_function_str)
        #  вектор градиента - его элементы - символьные представления частных производных
        self.nabla_vector = []
        #  точки
        self.X_step_points_array = []

    gradient_method = gradient_method
    nabla_calculate = nabla_calculate
    gradient_method_DFP = gradient_method_DFP
    draw_contoures = draw_contoures
    draw_contoures_full = draw_contoures_full


