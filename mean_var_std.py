import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    arr = np.array(list).reshape(3, 3)

    calculations['mean'] = [arr.mean(axis=0), arr.mean(axis=1), np.mean(list)]
    calculations['variance'] = [arr.var(axis=0), arr.var(axis=1), np.var(list)]
    calculations['standard deviation'] = [arr.std(axis=0), arr.std(axis=1), np.std(list)]
    calculations['max'] = [arr.max(axis=0), arr.max(axis=1), max(list)]
    calculations['min'] = [arr.min(axis=0), arr.min(axis=1), min(list)]
    calculations['sum'] = [arr.sum(axis=0), arr.sum(axis=1), sum(list)]



    return calculations