#Patern search
import numpy as np

def f_vector(X):
      """
      Himmelblau's function (vectorized input).
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

# Exploratory move
# f+=f(x1​,…,xi​+Δi​,…,xn​)
def exploratory(Xc, delta):
    """
    Exploratory move for Hooke-Jeeves.
    Xc: current base point (numpy array)
    delta: step size
    """
    X = Xc.copy()
    # This loop is correct: it checks x-axis, then y-axis from the new point
    for i in range(2): 
        unit_vector = np.array([0.0,0.0]) #2D
        unit_vector[i] = 1

        # Check current, plus, and minus
        Xs = [X, X + delta * unit_vector, X - delta * unit_vector]
        Fs = [f_vector(x) for x in Xs]

        # Choose the one with the minimum f
        X = Xs[np.argmin(Fs)]

    if np.allclose(X, Xc): # Check if the point moved
        return False, X
    else:
        # A move means f(X) <= f(Xc) (due to argmin)
        # We assume f(X) < f(Xc) for a successful move
        return True, X

def patern_move(x_current, x_prev):
     """
     x_currect: np.array
     x_prev: np.array
     """
     
     return 2*x_current - x_prev 
     
def patern_search(X, delta, alpha, epsilon, max_iter=200):
     print(f"Starting in {X}")
     X_k = X.copy() 
     
     iter_num = 0
     while delta >= epsilon: # Do while
          iter_num += 1
          if iter_num > max_iter:
               print("Error: Max iterations reached. Stopping.")
               break
          
          print(f"\n--- Iter {iter_num} (delta={delta:.5f}) ---")
          print(f"Base X_k = {X_k}, f(X_k) = {f_vector(X_k):.4f}")

          X_k_start_iter = X_k.copy()
          suc, X_out = exploratory(X_k, delta)
          
          if suc:
               print(f"Exploratory success. New base: {X_out}")
               
               X_kminus1 = X_k.copy() 
               X_k = X_out.copy()
               
               j = 0
               while True:
                    j += 1
                    if j > 100: # Safety break
                         print("Warning: Inner pattern loop limit reached.")
                         break

                    # Step 4: Calculate pattern point
                    X_kplus1_p = patern_move(X_k, X_kminus1)
                    print(f"  (j={j}) Pattern point: {X_kplus1_p}")

                    # Step 5: Explore from pattern point
                    _, X_kplus1 = exploratory(X_kplus1_p, delta)
                    print(f"  (j={j}) Exploratory from pattern: {X_kplus1}")

                    # Step 6: Check for improvement
                    if f_vector(X_kplus1) < f_vector(X_k):
                         # SUCCESS: The pattern move worked!
                         # Accept X_kplus1 as the new base.
                         # Update points and *continue* the pattern loop.
                         print(f"  (j={j}) Pattern SUCCESS: f({f_vector(X_kplus1):.4f}) < f({f_vector(X_k):.4f})")
                         X_kminus1 = X_k.copy()
                         X_k = X_kplus1.copy()
                    else:
                         # FAILURE: The pattern move didn't help.
                         # Discard X_kplus1. The last good point is X_k.
                         print(f"  (j={j}) Pattern FAILED. Reverting to base {X_k}")
                         # Break
                         break
               
          else:
               # Step 2 (initial exploratory move) failed.
               # We are stuck at X_k_start_iter with this delta.
               print(f"Initial exploratory FAILED from {X_k_start_iter}")
               
               # We must reduce delta.
               print(f"Reducing delta.")
               delta = delta / alpha
               
               # Ensure our base point is the one we started this iter with
               X_k = X_k_start_iter

     # --- End of 'while delta >= epsilon' loop ---
     print(f"\nConvergence reached. Delta ({delta:.5f}) < Epsilon ({epsilon})")
     return X_k, f_vector(X_k)

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


               
