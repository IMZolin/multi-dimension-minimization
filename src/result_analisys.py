import numpy as np
import matplotlib.pyplot as plt
from One_D_Problem_file import One_D_Problem
from Trial_Point_Method_file import trial_point_method
from uniform_search import uniform_search_method
from golden_egg import golden_search, gold
import math
from multidimensional_problem import N_D_Problem
import math
from gradient_1 import norma_calculate


def graphics():
    ndp = N_D_Problem()
    ndp.nabla_calculate()
    X0 = [1, 1]

    x_star = ndp.gradient_method_DFP(pow(10, -3), X0, golden_search)[-1]
    f_star = ndp.target_function(x_star)

    x_1 = ndp.gradient_method(pow(10, -3), X0, golden_search)
    f_1 = []
    for i in range(len(x_1)):
        f_1.append(abs(ndp.target_function(x_1[i]) - f_star))

    x_DFP = ndp.gradient_method_DFP(pow(10, -3), X0, trial_point_method)
    f_DFP = []
    for i in range(len(x_DFP)):
        f_DFP.append(abs(ndp.target_function(x_DFP[i]) - f_star))

    plt.plot(range(1, len(x_1) + 1), f_1, label='Gradient Method')
    plt.plot(range(1, len(x_DFP) + 1), f_DFP, label='DFP')
    plt.xlabel('iteration')
    plt.ylabel('log loss')
    plt.title('|f(x_k) - f(x_star)|')
    plt.legend()
    plt.semilogy()
    plt.show()

    print('cat')
    print(f_DFP)
    for i in range(len(f_DFP) - 1):
        print(f_DFP[i+1] / (3*f_DFP[i]**2))


def show_double_speed():
    ndp = N_D_Problem()
    ndp.nabla_calculate()
    X0 = [1, 7]

    x_array = np.array(ndp.gradient_method_DFP(pow(10, -4), X0, golden_search))
    x_star = x_array[-1]

    f_star = ndp.target_function(x_star)


    col1 = [norma_calculate(item - x_star) for item in x_array]
    plt.plot(range(len(col1)), col1)
    plt.semilogy()
    plt.xlabel('iteration')
    plt.ylabel('||x_k - x*||')
    plt.title('DFP, eps = 0.0001')
    plt.show()

    print()
    print(col1)
    col2 = []
    for i in range(len(x_array) - 1):
        col2.append(col1[i+1] / (col1[i]**2))
        print(round(col1[i], 4), round(col2[i], 4))
    # print(col2)


# graphics()
show_double_speed()

