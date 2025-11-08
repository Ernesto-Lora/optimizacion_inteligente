import numpy as np

def f_vector(X):
      """
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2


def generate_simplex(X0, alpha):
     """
     Generates the initial N+1 vertices of the simplex.
     X0: is a numpy array (a vector) for the initial point
     alpha: a scalar for the size of the simplex
     """
     N = len(X0)
     delta1 = ((np.sqrt(N + 1) + N - 1) / (N * np.sqrt(2))) * alpha
     delta2 = ((np.sqrt(N + 1) - 1) / (N * np.sqrt(2))) * alpha

     X_simplex = np.tile(X0, (N + 1, 1)).astype(float)
     
     for i in range(N):
        X_simplex[i + 1, :] += delta2
        X_simplex[i + 1, i] += (delta1 - delta2)
        
     return X_simplex

def centroid(X_except_h):
     """
     Computes the centroid of all points *except* the worst point (Xh).
     X_except_h: An (N x N) numpy array of N points.
     """
     return np.mean(X_except_h, axis=0)

def reflex(Xc, Xh):
     """
     Reflects the worst point (Xh) through the centroid (Xc).
     """
     return 2 * Xc - Xh

def expansion(gamma, Xc, Xh):
     """
     Expands the simplex in the reflection direction.
     Xe = Xc + gamma * (Xc - Xh)
     """
     return (gamma + 1) * Xc - gamma * Xh

def contraction_out(beta, Xc, Xh):
     """
     Performs an "outside" contraction.
     This is the function you provided as `contraction`.
     X_cout = Xc + beta * (Xc - Xh)
     """
     return (beta + 1) * Xc - beta * Xh

def contraction_in(beta, Xc, Xh):
     """
     Performs an "inside" contraction.
     X_cin = Xc - beta * (Xc - Xh)
     """
     return (1 - beta) * Xc + beta * Xh



X_simplex_predifined = np.array([
         [0.0, 0.0],
         [2.0, 0.0],
         [1.0, 1.0]
     ])

def fmt_vec(v):
    return "(" + ", ".join(f"{x:.3f}" for x in v) + ")"


def simplex(x0, alpha, beta, gamma, epsilon, f, max_iter=1000):
     """
     Performs the Nelder-Mead simplex minimization algorithm.

     Parameters:
     x0: Initial guess (numpy array)
     alpha: Scale for initial simplex generation
     beta: Contraction coefficient (e.g., 0.5)
     gamma: Expansion coefficient (e.g., 2.0)
     epsilon: Convergence tolerance
     f: The objective function to minimize (must take a numpy array)
     max_iter: Maximum number of iterations
     """
     N = len(x0)

     X = generate_simplex(x0, alpha)
     # X = X_simplex_predifined

     F = np.array([f(X[i]) for i in range(N + 1)])

     for iter_count in range(max_iter): # Do while with max iterations 
          order = np.argsort(F)
          F = F[order]
          X = X[order]

          # Assign points: Xl (best), Xg (second worst), Xh (worst)
          Xl = X[0]
          Fl = F[0]
          Xg = X[-2]
          Fg = F[-2]
          Xh = X[-1]
          Fh = F[-1]
          print(f"Iteration {iter_count}")
          print(f"xl = {fmt_vec(Xl)}, f(xl) = {Fl:.3f}")
          print(f"xg = {fmt_vec(Xg)}, f(xg) = {Fg:.3f}")
          print(f"xh = {fmt_vec(Xh)}, f(xh) = {Fh:.3f}")

          # Compute centroid (excluding the worst point Xh)
          Xc = centroid(X[:-1])
          Fc = f(Xc)

          Xr = reflex(Xc, Xh)
          Fr = f(Xr)
          X_new = Xr
          F_new = Fr

          if Fr < Fl:
               X_new = expansion(gamma, Xc, Xh)
               F_new = f(X_new)
               
          elif  Fr >= Fh:
               X_new = contraction_in(beta, Xc, Xh)
               F_new = f(X_new)
               
          elif Fg < Fr < Fh:
               X_new = contraction_out(beta, Xc, Xh)
               F_new = f(X_new)
               
          X[-1]  = X_new.copy()
          F[-1] = F_new
          
          Q = np.sqrt(np.sum((F - Fc)**2) / (N + 1))
          print(f"Q = {Q:.3f}")
          
          if Q < epsilon:
               return Xl, Fl # Return best point and its value

     print("Warning: Maximum iterations reached without convergence.")
     return Xl, Fl


if __name__ == "__main__":

     # Set parameters
     x1 = float(input('Enter first entry of x0: '))
     x2 = float(input('Enter second entry of x0: '))
     x_init1 = np.array([x1, x2])

     alpha_p = float(input('Enter alpha: '))   
     beta_p = float(input('Enter beta: '))    # Contraction
     gamma_p = float(input('Enter gamma: '))     # Expansion
     epsilon_p = float(input('Enter epsilon: '))  # Tolerance

     print(f"Starting simplex from: {x_init1}")
     best_x1, best_f1 = simplex(x_init1, alpha_p, beta_p, gamma_p,
                                 epsilon_p, f_vector, max_iter=100)
     print(f"Found minimum at: {best_x1}")
     print(f"Function value: {best_f1}\n")