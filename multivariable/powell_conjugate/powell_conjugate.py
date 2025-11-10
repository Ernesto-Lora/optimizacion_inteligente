#powell_conjugate
import numpy as np

# Newton method
def first_derivative(f1, f3, delta):
    return (f1 - f3) / (2 * delta)


def second_derivative(f1, f2, f3, delta):
    return (f1 + f3 - 2 * f2) / delta**2


def newton_minimize(x0, epsilon, delta, f, alpha_init=1.0, lambda_reg=1e-6):
    """
    Modified Newton method for minimization (with damping and curvature check).

    Parameters:
        x0 : float              # initial guess
        epsilon : float         # tolerance for stopping
        delta : float           # finite difference delta
        f : callable            # function to minimize
        alpha_init : float      # initial step size for line search
        lambda_reg : float      # regularization to keep curvature positive
    """

    k = 0
    while True:
        f1 = f(x0 + delta)
        f2 = f(x0)
        f3 = f(x0 - delta)

        g = first_derivative(f1, f3, delta)    
        H = second_derivative(f1, f2, f3, delta)

        if abs(g) < epsilon:
            break

        # Regularize Hessian to avoid division by zero or negative curvature
        if H <= 0:
            H = abs(H) + lambda_reg

        step = -g / H

        # Line search (damping): reduce alpha until function decreases
        alpha = alpha_init
        while f(x0 + alpha * step) > f2:
            alpha *= 0.5
            if alpha < 1e-6:
                break

        # Update point
        x_new = x0 + alpha * step

        if abs(x_new - x0) < epsilon:
            x0 = x_new
            break

        x0 = x_new
        k += 1

        if k > 200:
            print(" Max iterations reached.")
            break
    return x0


def f_vector(X):
      """
      Himmelblau's function (vectorized input).
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

def one_variable_optimization(f):
      x_op = newton_minimize(x0=0,epsilon=0.001,delta=0.001,f=f)
      return x_op

def powell_conjugate(X, f_vec, epsilon = 0.001, max_iter = 5):
      # Step 1. Start with canonical unit vectors for directions
      x0 = X.copy()
      s1 = np.array([1.0,0.0]) #2D
      s2 = np.array([0.0,1.0])

      for iter in range(max_iter):

            print(f"Iteration {iter+1}")
            # Step 2. Fiding one dimensional minimuns
            def g0(l): return f_vec( x0+l*s1 )
            l0 = one_variable_optimization(g0)
            x1 = x0 + l0*s1
            print(f"x1: {x1}")
            def g1(l): return f_vec( x1+l*s2 )
            l1 = one_variable_optimization(g1)
            x2 = x1+l1*s2
            print(f"x2: {x2}")
            def g2(l): return f_vec( x2+l*s1 )
            l2 = one_variable_optimization(g2)
            x3 = x2+l2*s1
            print(f"Final point in this search is {x3}")

            #step 3. Form new conjugate direction
            d = x3-x1
            d_norm = np.linalg.norm(d)
            print(f"Direction is {d} with norm {d_norm}")

            #step 4. if the norm is small. Terminate
            lin_dep = abs(np.dot(d, s1)) / (np.linalg.norm(d) * np.linalg.norm(s1) + 1e-12) > 0.9999
            # lin_dep is the cosine of the angle between d and s1
            # if this is almost 1 or -1 (thats why the absolute value),
            #  then they are almost linear dependent
            # 1e-12: prevents divition by zero

            if d_norm<epsilon or lin_dep:
                  return x3, f_vec(x3)
            s2 = s1.copy()
            s1 = d.copy()/d_norm
            print(s2,s1)
            x0 = x3

      return x3, f_vec(x3)

if __name__ == "__main__":

     # Set parameters
     x1 = float(input('Enter first entry of x0: '))
     x2 = float(input('Enter second entry of x0: '))
     x_init1 = np.array([x1, x2])

     epsilon_p = float(input('Enter epsilon: '))  # Tolerance

     print(f"Starting search from: {x_init1}")
     best_x1, best_f1 = powell_conjugate(X= x_init1, epsilon=epsilon_p,
                                         f_vec = f_vector)
     print(f"\n--- Result ---")
     print(f"Found minimum at: {best_x1}")
     print(f"Function value: {best_f1}\n")