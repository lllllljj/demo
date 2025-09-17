def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    a = np.array(lst).reshape(3, 3)

    # 按题目顺序：axis1(行), axis2(列), flattened
    mean = [a.mean(axis=1).tolist(), a.mean(axis=0).tolist(), a.mean().tolist()]
    var  = [a.var(axis=1).tolist(),  a.var(axis=0).tolist(),  a.var().tolist()]
    std  = [a.std(axis=1).tolist(),  a.std(axis=0).tolist(),  a.std().tolist()]
    max_ = [a.max(axis=1).tolist(),  a.max(axis=0).tolist(),  a.max().tolist()]
    min_ = [a.min(axis=1).tolist(),  a.min(axis=0).tolist(),  a.min().tolist()]
    sum_ = [a.sum(axis=1).tolist(),  a.sum(axis=0).tolist(),  a.sum().tolist()]

    return {
        'mean': mean,
        'variance': var,
        'standard deviation': std,
        'max': max_,
        'min': min_,
        'sum': sum_
    }
print(calculate([0, 6, 8, 6, 9, 8, 10, 9, 9]))
