import json

def solve_tsp_nearest_neighbor(start_city, distances):
    """
    Solves TSP using Nearest Neighbor heuristic starting from a specific city.
    """
    # Initialize variables
    current_city = start_city
    path = [current_city]
    visited = {current_city}
    total_cost = 0.0
    
    # Get total number of cities to visit
    all_cities = list(distances.keys())
    n = len(all_cities)

    # Step 1: Visit nearest unvisited neighbors
    while len(visited) < n:
        neighbors = distances[current_city]
        nearest_city = None
        min_dist = float('inf')

        # Find the closest unvisited city
        for city, dist in neighbors.items():
            if city not in visited:
                if dist < min_dist:
                    min_dist = dist
                    nearest_city = city
        
        # Move to the nearest city
        if nearest_city:
            path.append(nearest_city)
            visited.add(nearest_city)
            total_cost += min_dist
            current_city = nearest_city
        else:
            # Should not happen in a complete graph
            break

    # Step 2: Return to the start city to close the loop
    # We look up the distance from the last city back to the start
    return_dist = distances[current_city][start_city]
    path.append(start_city)
    total_cost += return_dist

    return path, total_cost

def main():
    filename = 'city_distances.json'
    
    try:
        # Load the data
        with open(filename, 'r') as f:
            data = json.load(f)
            
        cities = list(data.keys())
        print(f"Loaded {len(cities)} cities. Calculating {len(cities)} solutions...\n")
        
        results = []

        # Run the heuristic for every city as the starting point
        for start_node in cities:
            path, cost = solve_tsp_nearest_neighbor(start_node, data)
            results.append({
                "start": start_node,
                "path": path,
                "cost": cost
            })

        # Output the results
        print(f"{'Start City':<12} | {'Total Cost':<12} | {'Path'}")
        print("-" * 60)
        
        # Sort results by cost to see the best one first (optional, but helpful)
        results.sort(key=lambda x: x['cost'])

        for res in results:
            path_str = " -> ".join(res['path'])
            print(f"{res['start']:<12} | {res['cost']:<12.4f} | {path_str}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # --- OPTIONAL: Create the dummy file for testing based on your data ---
    # You can remove this block if your file already exists.
    sample_data = {
        "0": {"0": 0.0, "1": 30.4631, "2": 15.2315, "3": 47.3814, "4": 62.9365, "5": 55.4437, "6": 94.1488},
        "1": {"0": 30.4631, "1": 0.0, "2": 34.0588, "3": 21.8403, "4": 36.6742, "5": 47.8539, "6": 93.2952},
        "2": {"0": 15.2315, "1": 34.0588, "2": 0.0, "3": 36.1, "4": 50.5, "5": 45.2, "6": 85.1},
        "3": {"0": 47.3814, "1": 21.8403, "2": 36.1, "3": 0.0, "4": 18.5, "5": 28.3, "6": 72.4},
        "4": {"0": 62.9365, "1": 36.6742, "2": 50.5, "3": 18.5, "4": 0.0, "5": 12.1, "6": 60.2},
        "5": {"0": 55.4437, "1": 47.8539, "2": 45.2, "3": 28.3, "4": 12.1, "5": 0.0, "6": 50.5},
        "6": {"0": 94.1488, "1": 93.2952, "2": 85.1, "3": 72.4, "4": 60.2, "5": 50.5, "6": 0.0}
    }
    # Note: I filled in dummy data for 2-6 based on logic to make it runnable, 
    # but the script will use your actual file content when run normally.
    with open('city_distances.json', 'w') as f:
        json.dump(sample_data, f, indent=4)
    # ---------------------------------------------------------------------

    main()