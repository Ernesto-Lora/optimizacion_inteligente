import numpy as np

def f(x):
    return x**2 +54/x

def get_x_test(funs, xs):
    a1 = (funs[1] - funs[0]) / (xs[1] - xs[0])
    a2 = ((funs[2] - funs[0]) / (xs[2] - xs[0]) - a1) / (xs[2] - xs[1])
    return (xs[0] + xs[1]) / 2 - a1 / (2 * a2)

def quadratic_estimation(x1, delta, tol1, tol2, f, max_iter=100):
    print(f"The initial point is: {x1:.6f}")
    print(f"With a tolerance one of {tol1}")
    print(f"And tolerance two of {tol2}")

    # --- Bracketing step ---
    x2 = x1 + delta
    if f(x1) > f(x2):
        x3 = x1 + 2 * delta
    else:
        x3 = x1 - delta
        x2, x1 = x1, x3  # reorder so xs are increasing

    xs = np.array([x1, x2, x3], dtype=float)
    xs.sort()
    funs = f(xs)

    k = 0
    while k < max_iter:
        k += 1
        # Fit parabola and get test point
        x_test = get_x_test(funs, xs)
        f_test = f(x_test)

        # Find current minimum
        min_index = np.argmin(funs)
        f_min = funs[min_index]
        x_min = xs[min_index]

        print(f"Iteration {k}")
        print(f"xs = {xs}")
        print(f"f(xs) = {funs}")
        print(f"x_test = {x_test:.6f}, f_test = {f_test:.6f}")
        print(f"Current min: x = {x_min:.6f}, f(x) = {f_min:.6f}")
        print(f"|f_min - f_test| = {abs(f_min - f_test):.6e}")
        print(f"|x_min - x_test| = {abs(x_min - x_test):.6e}")
        print("-" * 40)

        # --- stopping condition ---
        if abs(f_min - f_test) <= tol1 and abs(x_min - x_test) <= tol2:
            break

        # --- update rule: replace the worst point ---
        all_xs = np.append(xs, x_test)
        all_fs = np.append(funs, f_test)

        # sort by x for consistency
        order = np.argsort(all_xs)
        all_xs = all_xs[order]
        all_fs = all_fs[order]

        # keep the best 3 neighboring points around the minimum
        min_idx = np.argmin(all_fs)
        if min_idx == 0:
            xs = all_xs[:3]
            funs = all_fs[:3]
        elif min_idx == len(all_fs) - 1:
            xs = all_xs[-3:]
            funs = all_fs[-3:]
        else:
            xs = all_xs[min_idx - 1:min_idx + 2]
            funs = all_fs[min_idx - 1:min_idx + 2]

    print(f"Returning the value: {x_min:.6f}")
    return x_min

if __name__ == "__main__":
    # x1 = float(input('Enter the value of "x1": '))
    # tol1 = float(input('Enter the tolerance "tol1": '))
    # tol2 = float(input('Enter the tolerance "tol2": '))
    # delta = float(input('Enter the step "delta": '))

    # quadratic_estimation(x1 = x1,delta = delta,tol1=tol1,tol2=tol2,f = f)
    quadratic_estimation(x1 = 4,delta = 2,tol1=1e-3,tol2=1e-3,f = f)