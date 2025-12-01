import json

def calculate_total_cost(route, distances):
    """Calculates the cost of a given route."""
    cost = 0.0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i+1]
        cost += distances[from_city][to_city]
    return cost

def two_opt_swap(route, i, k):
    """
    Performs a 2-opt swap by reversing the segment between i and k.
    This effectively swaps edges (i-1, i) and (k, k+1) with (i-1, k) and (i, k+1).
    """
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    return new_route

def solve_2opt(route, distances):
    improved = True
    iteration = 0
    best_route = route
    best_cost = calculate_total_cost(route, distances)
    
    print(f"Initial Cost: {best_cost:.4f}")
    print(f"Initial Route: {best_route}\n")
    print("-" * 60)
    print(f"{'Iter':<5} | {'Movement (Swap)':<25} | {'New Cost':<10} | {'Improvement'}")
    print("-" * 60)

    while improved:
        improved = False
        # We iterate from the 2nd node to the 2nd-to-last node
        # because the start/end node (index 0 and -1) is fixed in the cycle representation
        # for simplicity in this specific swap implementation.
        for i in range(1, len(best_route) - 2):
            for k in range(i + 1, len(best_route) - 1):
                
                # Create a new route with the swap
                new_route = two_opt_swap(best_route, i, k)
                new_cost = calculate_total_cost(new_route, distances)

                if new_cost < best_cost:
                    diff = best_cost - new_cost
                    iteration += 1
                    
                    print(f"{iteration:<5} | Reverse Seg [{i}:{k}] ({best_route[i]}..{best_route[k]}) | {new_cost:<10.4f} | -{diff:.4f}")
                    
                    best_route = new_route
                    best_cost = new_cost
                    improved = True
                    # We restart the search after a found improvement (First Improvement strategy)
                    # to ensure we don't mess up indices.
                    break 
            if improved:
                break

    print("-" * 60)
    return best_route, best_cost

def main():
    try:
        # Load the data saved by the previous script
        with open('tsp_solution_data.json', 'r') as f:
            data = json.load(f)
            
        initial_route = data['initial_route']
        distances = data['distances']

        print("Starting 2-Opt Optimization...\n")
        
        final_route, final_cost = solve_2opt(initial_route, distances)

        print(f"\nOptimization Finished.")
        print(f"Final 2-Opt Cost: {final_cost:.4f}")
        print(f"Final Path: {final_route}")
        
    except FileNotFoundError:
        print("Error: 'tsp_solution_data.json' not found. Run the Nearest Neighbor script first.")

if __name__ == "__main__":
    main()