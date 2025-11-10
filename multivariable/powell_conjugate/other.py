import numpy as np
import time

# --- Part 1: 1D Search ---
def golden_section_search(g, a, b, tol=1e-6):
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(b - a) > tol:
        if g(c) < g(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return (b + a) / 2

# --- Part 2: Main Powell Method ---
def powell_method(f_vec, x0, epsilon=1e-6, max_iter=100):
    n = len(x0)
    x_k = np.array(x0, dtype=float)
    S = np.identity(n)
    
    print(f"Starting Powell's Method from x0 = {x0}")
    
    for k in range(max_iter):
        x_prev = x_k.copy()
        p = [x_k.copy()]
        delta_f_max = 0.0
        idx_max = 0
        
        # Step 2. Sequential 1D minimizations
        for i in range(n):
            s_i = S[i]
            def g(l):
                return f_vec(p[i] + l * s_i)
            
            l_min = golden_section_search(g, a=-10.0, b=10.0, tol=epsilon)
            p_new = p[i] + l_min * s_i
            p.append(p_new)
            
            delta_f = f_vec(p[i]) - f_vec(p_new)
            if delta_f > delta_f_max:
                delta_f_max = delta_f
                idx_max = i
                
        x_k = p[n]
        
        # Step 3. Check convergence
        if np.linalg.norm(x_k - x_prev) < epsilon:
            print(f"\nConverged after {k+1} iterations.")
            return x_k, f_vec(x_k)
            
        # Step 4. Generate new conjugate direction
        d = p[n] - p[0]
        
        # Step 5. Minimize along new direction
        def g_d(l):
            return f_vec(p[n] + l * d)
        
        l_d_min = golden_section_search(g_d, a=-10.0, b=10.0, tol=epsilon)
        x_k = p[n] + l_d_min * d
        
        # Step 6. Update direction set (Powell's refinement)
        f_0 = f_vec(p[0])
        f_n = f_vec(p[n])
        f_d_new = f_vec(x_k)
        
        is_useful = f_d_new < f_0
        condition_check = (f_0 - 2*f_n + f_d_new) * (f_0 - f_n - delta_f_max)**2 \
                          < 0.5 * delta_f_max * (f_0 - f_d_new)**2

        if is_useful and condition_check:
            # Shift and replace
            for i in range(idx_max, n - 1):
                S[i] = S[i+1]
            S[n-1] = d / np.linalg.norm(d)
        
        # print(f"Iter {k+1}: x = {x_k}, f(x) = {f_vec(x_k)}")

            
    print("\nReached max iterations.")
    return x_k, f_vec(x_k)

# --- Part 3: Test Function (Rosenbrock) ---
def rosenbrock(X):
    # Optimum is at [1, 1] with value 0
    x = X[0]
    y = X[1]
    return (1 - x)**2 + 100 * (y - x**2)**2

def f_vector(X):
      """
      Himmelblau's function (vectorized input).
      X is a numpy array, e.g., np.array([x1, x2])
      """
      x1 = X[0]
      x2 = X[1]
      return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2

# --- Run the optimization ---
start_time = time.time()
x_initial = np.array([0, 4])
min_point, min_val = powell_method(f_vector, x_initial)
end_time = time.time()

print("--- Results ---")
print(f"Minimum found at: {min_point}")
print(f"Function value:   {min_val}")
print(f"Time taken:       {end_time - start_time:.4f} seconds")