import math

def objective_function(x_val):
    return (x_val**2 + 54 / x_val)

def compute_derivative(func_val1, func_val2, step_size):
    return (func_val1 - func_val2) / (2 * step_size)

def calculate_interpolation_param(point_a, point_b, func_a, func_b, deriv_a, deriv_b):
    if point_a == point_b:
        return 0.5
    
    z = 3 * (func_a - func_b) / (point_b - point_a) + deriv_a + deriv_b
    omega = ((point_b - point_a) / abs(point_b - point_a) ) * math.sqrt(z**2 - deriv_a * deriv_b)
    
    return (deriv_b + omega - z) / (deriv_b - deriv_a + 2 * omega)

def get_test_point(point_a, point_b, interpolation_param):
    if interpolation_param <= 0:
        return point_b
    elif interpolation_param >= 1:
        return point_a
    else:
        return point_b - interpolation_param * (point_b - point_a)

def cubic_interpolation_optimizer(start_point, initial_step, tolerance, derivative_step, func):
    print(f"Starting optimization at: {start_point}")
    print(f"Initial step size: {initial_step}")
    print(f"Convergence tolerance: {tolerance}")
    print(f"Derivative step size: {derivative_step}")
    
    current_point = start_point
    current_deriv = compute_derivative(
        func(current_point + derivative_step), 
        func(current_point - derivative_step), 
        derivative_step
    )
    
    # Determine search direction
    if current_deriv > 0:
        initial_step = -initial_step
    
    iteration_count = 0
    # Find initial bracket
    while True:
        next_point = current_point + (2 ** iteration_count) * initial_step
        next_deriv = compute_derivative(
            func(next_point + derivative_step), 
            func(next_point - derivative_step), 
            derivative_step
        )
        
        # Check if we've bracketed a minimum
        if current_deriv * next_deriv <= 0:
            point_a, point_b = current_point, next_point
            deriv_a, deriv_b = current_deriv, next_deriv
            break
            
        current_deriv = next_deriv
        current_point = next_point
        iteration_count += 1
    
    func_a = func(point_a)
    func_b = func(point_b)
    
    optimization_iteration = 1
    while optimization_iteration <= 50:
        print(f"Current interval: [{point_a:.6f}, {point_b:.6f}]")
        print(f"Derivatives: {deriv_a:.6f}, {deriv_b:.6f}")
        
        # Calculate interpolation parameter
        interpolation_param = calculate_interpolation_param(
            point_a, point_b, func_a, func_b, deriv_a, deriv_b
        )
        
        # Get candidate point
        candidate_point = get_test_point(point_a, point_b, interpolation_param)
        candidate_func_val = func(candidate_point)
        
        print(f"Iteration {optimization_iteration}: Candidate point = {candidate_point:.6f}")
        
        # Ensure function value decreases
        while candidate_func_val > func_a:
            candidate_point = candidate_point - 0.5 * (candidate_point - point_a)
            candidate_func_val = func(candidate_point)
        
        # Compute derivative at candidate point
        candidate_deriv = compute_derivative(
            func(candidate_point + derivative_step), 
            func(candidate_point - derivative_step), 
            derivative_step
        )
        
        # Check convergence criteria
        if (abs(candidate_deriv) <= tolerance and 
            abs((candidate_point - point_a) / candidate_point) <= tolerance):
            break
            
        # Update interval
        if candidate_deriv * deriv_a < 0:
            point_b, func_b, deriv_b = candidate_point, candidate_func_val, candidate_deriv
        else:
            point_a, func_a, deriv_a = candidate_point, candidate_func_val, candidate_deriv
            
        optimization_iteration += 1
    
    optimal_point = (point_a + point_b) / 2
    print(f"Optimization complete. Final point: {optimal_point:.6f}")
    return optimal_point

# Execute the optimization
result = cubic_interpolation_optimizer(
    start_point=1,
    initial_step=0.5,
    tolerance=1e-3,
    derivative_step=1e-3,
    func=objective_function
)
