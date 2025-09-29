# Golden-section search
import numpy as np
def f(x):
    return x**2 +54/x


def custom_print(aw, bw, a,b ,k):
    print(f"Iteration {k}")
    print(f"Interval found (in the (1,0) range): [{aw:.6f}, {bw:.6f}]")
    print(f"Interval length (Lw): {bw - aw:.6f}")
    print(f"Interval found: [{x(aw, a, b):.6f}, {x(bw, a, b):.6f}]")
    print(f"Interval length (L): {(bw - aw)*(b-a):.6f}")
    print("-" * 40)

def get_x_test(funs, xs):
    a1 = (funs[1]-funs[0])/(xs[1]-xs[0])
    a2 = 1/(xs[2]-xs[1])*( (funs[2]-funs[0])/(xs[2]-xs[0]) - a1 ) 
    return (xs[0]+xs[1])/2 - a1/(2*a2)

def quadratic_estimation(x1,delta,tol1,tol2,f):
    print(f"The initial point is: {x1:.6f}")
    print(f"With a tolerance one of {tol1}")
    print(f"And tolerance two of {tol2}")

    x2 = x1 + delta
    # xs =  np.array([x1, x2, 0])
    # funs = np.array([f(x1), f(x2), 0])
    if f(x1) > f(x2):
        x3 = x1+2*delta
    else:
        dummy = x1
        x1 = dummy - delta
        x2 = dummy
        x3 = dummy + delta

    xs =  np.array([x1, x2, x3])
    funs = f(xs) 

    min_index = np.argmin(funs)
    f_min = funs[min_index]
    x_min = xs[min_index]
    x_test = get_x_test(funs, xs)
    f_test = f(x_test)
    print(f"The current minimum is {x_min}")
    print(f"|f_min-f_test|: {abs(f_min - f_test):.6f}")
    while(abs(f_min - f_test) > tol1 and abs(x_min-x_test) > tol2):
        all_xs = np.append(xs, x_test)
        all_fs = np.append(funs, f_test)

        # A track of the indexes after reordering from the short to the largest
        order = np.argsort(all_xs)  
        all_xs_sorted = all_xs[order]
        all_fs_sorted = all_fs[order]
        new_min_index = np.argwhere(order == min_index)

        if new_min_index == 1 or new_min_index == 2:
            xs[0] = all_xs_sorted[new_min_index-1]
            xs[1] = all_xs_sorted[new_min_index]
            xs[2] = all_xs_sorted[new_min_index+1]

            funs[0] = all_fs_sorted[new_min_index-1]
            funs[1] = all_fs_sorted[new_min_index]
            funs[2] = all_fs_sorted[new_min_index+1]
        else:
            # get indices of the 3 smallest values
            idx = np.argsort(all_fs)[:3]
            xs = all_xs[idx]
            funs = all_fs[idx]

        min_index = np.argmin(funs)
        f_min = funs[min_index]
        x_min = xs[min_index]
        x_test = get_x_test(funs, xs)
        f_test = f(x_test)
        print(f"The current minimum is {x_min}")
        print(f"|f_min-f_test|: {abs(f_min - f_test):.6f}")

    print(f"Returning the value: {x_min}")
    return x_min

if __name__ == "__main__":
    # x1 = float(input('Enter the value of "x1": '))
    # tol1 = float(input('Enter the tolerance "tol1": '))
    # tol2 = float(input('Enter the tolerance "tol2": '))
    # delta = float(input('Enter the step "delta": '))

    # quadratic_estimation(x1 = x1,delta = delta,tol1=tol1,tol2=tol2,f = f)
    quadratic_estimation(x1 = 1,delta = 1,tol1=1e-3,tol2=1e-3,f = f)
