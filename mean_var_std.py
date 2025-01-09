import numpy as np


def calculate(x):
    if len(x) != 9:
        raise ValueError("List must contain nine numbers.")
    calculations = {'mean': [], 'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}
    ar = np.array([x[0:3], x[3:6], x[6:len(x)]])

    for i in range(2):
        # mean
        t = list(map(float, (np.mean(ar, axis=i))))
        calculations['mean'].append(t)

        # variance
        t = list(map(float, (np.var(ar, axis=i))))
        calculations['variance'].append(t)

        t = list(map(float, (np.std(ar, axis=i))))
        calculations['standard deviation'].append(t)

        # max
        t = list(map(float, (np.max(ar, axis=i))))
        calculations['max'].append(t)
        # min
        t = list(map(float, (np.min(ar, axis=i))))
        calculations['min'].append(t)
        # sum
        t = list(map(float, (np.sum(ar, axis=i))))
        calculations['sum'].append(t)


    calculations['mean'].append(float((np.mean(ar.flatten()))))
    calculations['variance'].append(float((np.var(ar.flatten()))))
    calculations['standard deviation'].append(float((np.std(ar.flatten()))))
    calculations['max'].append(float((np.max(ar.flatten()))))
    calculations['min'].append(float((np.min(ar.flatten()))))
    calculations['sum'].append(float((np.sum(ar.flatten()))))
    return calculations


