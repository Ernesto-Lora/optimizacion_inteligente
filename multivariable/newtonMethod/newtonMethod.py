
import numpy as np
def f_vector(X):
      """
      Himmelblau's function (vectorized input).
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2


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


def hessian(X, f):
    """
    Numeric Hessian matrix in a point X of function f.
    X. Numpy array, e.g., np.array([x1, x2])
    f. Function that takes a numpy array and return a scalar (float)
    """
    delta = 0.001
    N = len(X)
    delta_vec = delta * np.identity(N)
    hessian_ = np.zeros((N, N), dtype=float)
    f_X = f(X) # Store f(X) to avoid re-calculating it on diagonal steps

    for i in range(N):
        for j in range(N):
            if i == j:
                # Diagonal elements (Second derivative w.r.t xi)
                # Formula: (f(x+h) - 2f(x) + f(x-h)) / h^2
                val = (f(X + delta_vec[i]) - 2 * f_X + f(X - delta_vec[i])) / (delta**2)
                hessian_[i, j] = val
            else:
                # Off-diagonal elements (Mixed partial derivative w.r.t xi, xj)
                # Formula: (f(x+hi+hj) - f(x+hi-hj) - f(x-hi+hj) + f(x-hi-hj)) / 4h^2
                term1 = f(X + delta_vec[i] + delta_vec[j])
                term2 = f(X + delta_vec[i] - delta_vec[j])
                term3 = f(X - delta_vec[i] + delta_vec[j])
                term4 = f(X - delta_vec[i] - delta_vec[j])
                val = (term1 - term2 - term3 + term4) / (4 * delta**2)
                hessian_[i, j] = val
                
    return hessian_

def newtonMethodMultivariable(X, f, epsilon1 = 0.001, max_iter = 100):
     #Step 1. Inicialize
     xk = X.copy()
     print(f"Starting at {xk}")
     fxk = f(xk)
     for iter in range(max_iter):
          print(f"Iteration {iter+1}:")
          print(f"Current f(xk) = {fxk}")
          #Step 2. Compute gradient
          gradient_ = gradient(X=xk,f=f)
          gradient_norm = np.linalg.norm(gradient_)
          print(f"The gradient is {gradient_}")
          print(f"With norm {gradient_norm}")
          #Step 3. Termintion check
          if abs(gradient_norm ) < epsilon1:
               return xk
          
          #Step 4. Find x(k+1) such that
          #  f(x(k+1)) = f(x(k) − α(k) [∇^2 f(x(k))]^(-1) ∇ f (x(k) ))
          # is a minimum 
          hessiank = hessian(X=xk, f=f)
          
          inverse_hessiank = np.linalg.inv(hessiank)

          def g(l): return f(xk -l*inverse_hessiank @ gradient_)
          l_min = one_variable_optimization(f=g)
          
          xkp1 = xk - l_min* inverse_hessiank @ gradient_

          print(f"New point found {xkp1}")
          fxkp1 = f(xkp1)
          print(f"New f(x(k+1)) = {fxkp1}")
          change_ratio = abs(( fxkp1 - fxk )/(fxk+1e-12) )
          print(f"The change ratio is {change_ratio}")

          #step 5. Termination Check
          if change_ratio < epsilon1:
               return xkp1
          xk = xkp1
          fxk = fxkp1
     print("Do not reached convengerce")
     return xk

if __name__ == "__main__":

     # Set parameters
     x1 = float(input('Enter first entry of x0: '))
     x2 = float(input('Enter second entry of x0: '))
     x_init1 = np.array([x1, x2])

     epsilon_p = float(input('Enter epsilon: '))  # Tolerance

     best_x1 =newtonMethodMultivariable(X=x_init1,
                                         f=f_vector,
                                           epsilon1=epsilon_p)
     print(f"Found minimum at: {best_x1}")
     print(f"Function value: {f_vector(best_x1)}\n")
     