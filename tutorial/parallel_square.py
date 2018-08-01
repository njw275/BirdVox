from joblib import Parallel, delayed

def f(x):
    print(x)
    return x*x

li = Parallel(n_jobs=-1)(delayed(f)(i) for i in range(10))
print(li)
