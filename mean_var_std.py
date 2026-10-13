import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    return {
        name: [f(arr, axis=0).tolist(), f(arr, axis=1).tolist(), f(arr).tolist()]
        for name, f in funcs.items()
    }
