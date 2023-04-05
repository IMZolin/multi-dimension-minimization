from multidimensional_problem import N_D_Problem
from gradient_1 import gradient_method
from Trial_Point_Method_file import trial_point_method

pr1 = N_D_Problem()
pr1.nabla_calculate()
print([2 * x for x in [3, 4]])
pr1.gradient_method(0.01, [3, 4], trial_point_method)




