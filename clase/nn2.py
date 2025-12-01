import json

def solve_tsp_nearest_neighbor(start_city, distances):
    current_city = start_city
    path = [current_city]
    visited = {current_city}
    total_cost = 0.0
    
    cities = list(distances.keys())
    n = len(cities)

    while len(visited) < n:
        neighbors = distances[current_city]
        nearest_city = None
        min_dist = float('inf')

        for city, dist in neighbors.items():
            if city not in visited:
                if dist < min_dist:
                    min_dist = dist
                    nearest_city = city
        
        if nearest_city:
            path.append(nearest_city)
            visited.add(nearest_city)
            total_cost += min_dist
            current_city = nearest_city
        else:
            break

    # Return to start
    return_dist = distances[current_city][start_city]
    path.append(start_city)
    total_cost += return_dist

    return path, total_cost

def main():
    filename = 'city_distances.json'
    output_filename = 'tsp_solution_data.json'
    
    try:
        with open(filename, 'r') as f:
            distances = json.load(f)
            
        cities = list(distances.keys())
        best_solution = {"cost": float('inf'), "path": []}

        # Find the best NN solution
        for start_node in cities:
            path, cost = solve_tsp_nearest_neighbor(start_node, distances)
            if cost < best_solution["cost"]:
                best_solution = {"cost": cost, "path": path}

        print(f"Best NN solution found starting at city {best_solution['path'][0]}")
        print(f"Cost: {best_solution['cost']:.4f}")
        print(f"Path: {best_solution['path']}")

        # SAVE THE DATA
        save_data = {
            "initial_route": best_solution['path'],
            "distances": distances,
            "initial_cost": best_solution['cost']
        }
        
        with open(output_filename, 'w') as f:
            json.dump(save_data, f, indent=4)
        print(f"\nSuccessfully saved solution and distances to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

if __name__ == "__main__":
    main()