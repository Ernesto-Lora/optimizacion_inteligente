
import numpy as np


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
from newton_raphson import newton_minimize

def one_variable_optimization(f):
      x_op = newton_minimize(x0=0,epsilon=0.0001,delta=0.0001,f=f)
      return x_op

def gradient(X,f):
      """
      Numeric gradient in a point X of function f.
      X. Numpy array, e.g., np.array([x1, x2])
      f. Function that takes a numpy array and return a sacalar (float)
      """
      delta = 0.001
      N = len(X)
      delta_vec = delta * np.identity(N)
      gradient_ = np.zeros(N, dtype=float)
      for i in range(N):
            gradient_[i] = (f(X+delta_vec[i])-f(X-delta_vec[i]))/(2*delta)

      return gradient_

def conjugateGradient(X, f, epsilon1 = 0.001, max_iter = 100):
     #Step 1. Inicialize
     x0 = X.copy()
     print(f"Starting at {x0}")
     #Step 2. Compute gradient and set direction
     gradient_ = gradient(X=x0,f=f)
     s_direction = -gradient_.copy()

     # step 3. find λ such that make f (x(0) + λ(0) s(0) )
     # a minimum
     def g(l): return f(x0 +s_direction*l)
     l_min = one_variable_optimization(f=g)
     x1 = x0 - gradient_*l_min
     print(f"x1 found: {x1}")
     gradient1_ = gradient(X=x1,f=f)

     gradientkm1 = gradient_.copy()
     gradientk = gradient1_.copy()
     s_directionkm1 = s_direction
     xk = x1.copy()
     for iter in range(max_iter):
          print(f"Conjugate Iteration {iter+1}:")
          # step 4. find new direction
          gradientk_norm_square = np.linalg.norm(gradientk)**2
          gradientkm1_norm_square = np.linalg.norm(gradientkm1)**2
          ratio = gradientk_norm_square/gradientkm1_norm_square
          s_directionk = -gradientk + ratio*s_directionkm1

          # Step 5.  Find λ(k) such that f (x(k) + λ(k) s(k) ) is minimum
          # Set x(k+1) = x(k) + λ(k) s(k) 
          def g(l): return f(xk +s_directionk*l)
          l_min = one_variable_optimization(f=g)
          xkp1 = xk +s_directionk*l_min
          print(f"New x: {xkp1}")
          # Step 6. Termination condition
          gradientkp1 = gradient(xkp1,f)
          gradientkp1_norm = np.linalg.norm(gradientkp1)
          print(f"With gradient Norm {gradientkp1_norm}")
          change_ratio = np.linalg.norm( (xkp1 - xk))/ np.linalg.norm(xk)
          print(f"Change Ratio: {change_ratio}")
          if change_ratio < epsilon1 or gradientkp1_norm < epsilon1:
               return xkp1
          xk = xkp1.copy()
          gradientkm1 = gradientk.copy()
          gradientk = gradientkp1.copy()

     print("Do not reached convengerce")
     return xk

if __name__ == "__main__":

     # Set parameters
     x1 = float(input('Enter first entry of x0: '))
     x2 = float(input('Enter second entry of x0: '))
     x_init1 = np.array([x1, x2])
     epsilon_p = float(input('Enter epsilon: '))  # Tolerance

     best_x1 = conjugateGradient(X=x_init1 , f=f_vector, epsilon1=epsilon_p)
     print(f"Found minimum at: {best_x1}")
     print(f"Function value: {f_vector(best_x1)}\n")
