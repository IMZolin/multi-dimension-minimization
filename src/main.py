from multidimensional_problem import N_D_Problem
from Trial_Point_Method_file import trial_point_method
from golden_egg import golden_search

pr1 = N_D_Problem()
pr1.nabla_calculate()  # ОБЯЗАТЕЛЬНО ЗАПУСКАТЬ В НАЧАЛЕ ПРОГРАММЫ, ЕСЛИ БУДЕМ ИСПОЛЬЗОВАТЬ СИМВОЛЬНЫЕ ВЫЧИСЛЕНИЯ

print('GOLDEN SEARCH:')
pr1.gradient_method(0.1, [3, 4], golden_search)
print('TPM:')
pr1.gradient_method(0.1, [3, 4], trial_point_method)




