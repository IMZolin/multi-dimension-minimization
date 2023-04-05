import numpy as np
import matplotlib.pyplot as plt
from One_D_Problem_file import One_D_Problem
from Trial_Point_Method_file import trial_point_method
from uniform_search import  uniform_search_method
from golden_egg import golden_search, gold
import math


def super_target_function(self, x_, delta):
    return (x_ - delta) ** 2


def data_generating(accuracy, method):
    method_array = []

    for i in range(1000):
        pr1 = One_D_Problem()
        pr1.left_border = -2
        pr1.right_border = 2

        delta_x = np.random.randint(low=-1, high=2) * (pr1.right_border - pr1.left_border) / 2

        #  delta_x = -2 => min
        #  delta_x = 0 or 2 => max
        pr1.target_function = lambda x_: super_target_function(pr1, x_, delta_x)

        if method == uniform_search_method:
            method_array.append(method(self=pr1, accuracy=accuracy, n=6)[1])  # возвращаю только количество итераций
        else:
            method_array.append(method(self=pr1, accuracy=accuracy)[1])  # возвращаю только количество итераций

    return np.mean(method_array)


def graphics():
    """
    Добавить сбда другие два метода
    :return:
    """
    accuracy_array = [-1, -3, -5, -7, -9, -11, -13, -15]
    tpm_method_array = []
    us_method_array = []
    golden_array = []

    for accuracy in accuracy_array:
        tpm_method_array.append(data_generating(10 ** accuracy, trial_point_method))
        us_method_array.append(data_generating(10 ** accuracy, uniform_search_method))
        golden_array.append(data_generating(10 ** accuracy, golden_search))

    tpm_method_theory_min = []
    tpm_method_theory_max = []
    us_method_theory = []
    golden_theory = []

    for accuracy in accuracy_array:
        # tpm_method_theory_min.append(2 * (math.log2(4 / (10 ** accuracy)) // 1) + 1)  # типа округлили до целого
        # tpm_method_theory_max.append(3 * (math.log2(4 / (10 ** accuracy)) // 1) + 1)
        tpm_method_theory_min.append(2 + math.log2(4 / (10 ** accuracy)) // 1)  # типа округлили до целого
        tpm_method_theory_max.append(3 + 2 * (math.log2(4 / (10 ** accuracy)) // 1))
        us_method_theory.append(((math.log(10 ** accuracy / 4, 2 / 6)) // 1 + 1) * 5)
        golden_theory.append(math.log((10 ** accuracy) / 4, 1 - gold) // 1 + 1 + 2)

    plt.plot([10 ** x for x in accuracy_array], tpm_method_array, label='tpm')
    plt.plot([10 ** x for x in accuracy_array], tpm_method_theory_min, '--', label='min tpm theory')
    plt.plot([10 ** x for x in accuracy_array], tpm_method_theory_max, '--', label='max tpm theory')
    plt.xlabel('accuracy')
    plt.ylabel('function calculation')
    plt.legend()
    plt.semilogx()
    plt.show()

    plt.plot([10 ** x for x in accuracy_array], us_method_array, label='us')
    plt.plot([10 ** x for x in accuracy_array], us_method_theory, '--', label='us theory')
    plt.xlabel('accuracy')
    plt.ylabel('function calculation')
    plt.legend()
    plt.semilogx()
    plt.show()

    plt.plot([10 ** x for x in accuracy_array], golden_array, label='gold')
    plt.plot([10 ** x for x in accuracy_array], golden_theory, '--', label='gold theory')
    plt.xlabel('accuracy')
    plt.ylabel('function calculation')
    plt.legend()
    plt.semilogx()
    plt.show()

    plt.plot([10 ** x for x in accuracy_array], tpm_method_array, '-o', label='tpm')
    plt.plot([10 ** x for x in accuracy_array], us_method_array, '-o', label='us')
    plt.plot([10 ** x for x in accuracy_array], golden_array, '-o', label='gold')
    plt.xlabel('accuracy')
    plt.ylabel('function calculation')
    plt.legend()
    plt.semilogx()
    plt.show()



graphics()
