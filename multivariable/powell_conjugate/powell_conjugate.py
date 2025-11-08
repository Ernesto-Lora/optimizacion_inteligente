#powell_conjugate
import numpy as np

def f_vector(X):
      """
      Himmelblau's function (vectorized input).
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

def powell_conjugate(X, f_vec):
      return 

if __name__ == "__main__":

     # Set parameters
     x1 = float(input('Enter first entry of x0: '))
     x2 = float(input('Enter second entry of x0: '))
     x_init1 = np.array([x1, x2])

     alpha_p = float(input('Enter alpha: '))   
     delta = float(input('Enter delta: ')) 
     epsilon_p = float(input('Enter epsilon: '))  # Tolerance

     print(f"Starting search from: {x_init1}")
     best_x1, best_f1 = patern_search(X=x_init1, delta=delta,
                                       alpha=alpha_p, epsilon=epsilon_p)
     print(f"\n--- Result ---")
     print(f"Found minimum at: {best_x1}")
     print(f"Function value: {best_f1}\n")