from src.One_D_Problem_file import One_D_Problem

if __name__ == '__main__':
    problem = One_D_Problem()
    x, num_calls = problem.golden_search(0.0001)
    print(x, num_calls)
