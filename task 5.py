import math
import random

# Locations
# 0 = Restaurant
# 1-5 = Customers
locations = [
    (0, 0),   # Restaurant
    (2, 6),   # Customer 1
    (5, 3),   # Customer 2
    (6, 7),   # Customer 3
    (8, 2),   # Customer 4
    (3, 1)    # Customer 5
]

n = len(locations)

# Calculate distance between two locations
def calculate_distance(a, b):
    x1, y1 = locations[a]
    x2, y2 = locations[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Distance matrix
distance = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance[i][j] = calculate_distance(i, j)


# ACO parameters
num_ants = 20
num_iterations = 100
alpha = 1       # Importance of pheromone
beta = 5        # Importance of distance
evaporation = 0.5
Q = 100


# Initialize pheromone
pheromone = [[1.0 for _ in range(n)] for _ in range(n)]

random.seed(42)

best_route = None
best_distance = float("inf")


# Ant Colony Optimization
for iteration in range(num_iterations):

    all_routes = []

    for ant in range(num_ants):

        route = [0]              # Start at restaurant
        unvisited = set(range(1, n))

        while unvisited:

            current = route[-1]
            choices = list(unvisited)

            probabilities = []

            for next_node in choices:
                pheromone_value = pheromone[current][next_node] ** alpha
                distance_value = (1 / distance[current][next_node]) ** beta

                probabilities.append(
                    pheromone_value * distance_value
                )

            # Select next customer
            total = sum(probabilities)
            random_value = random.uniform(0, total)

            cumulative = 0

            for i in range(len(choices)):
                cumulative += probabilities[i]

                if random_value <= cumulative:
                    next_node = choices[i]
                    break

            route.append(next_node)
            unvisited.remove(next_node)

        # Return to restaurant
        route.append(0)

        # Calculate route distance
        route_distance = 0

        for i in range(len(route) - 1):
            route_distance += distance[route[i]][route[i + 1]]

        all_routes.append((route_distance, route))

        # Update best route
        if route_distance < best_distance:
            best_distance = route_distance
            best_route = route.copy()

    # Pheromone evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - evaporation)

    # Pheromone update
    for route_distance, route in all_routes:

        pheromone_deposit = Q / route_distance

        for i in range(len(route) - 1):

            a = route[i]
            b = route[i + 1]

            pheromone[a][b] += pheromone_deposit
            pheromone[b][a] += pheromone_deposit


# Display result
print("Food Delivery Route using Ant Colony Optimization")
print("--------------------------------------------------")

print("Restaurant = 0")
print("Customer 1 = 1")
print("Customer 2 = 2")
print("Customer 3 = 3")
print("Customer 4 = 4")
print("Customer 5 = 5")

print("\nBest Route:")

for i, node in enumerate(best_route):

    if node == 0:
        name = "Restaurant"
    else:
        name = "Customer " + str(node)

    if i < len(best_route) - 1:
        print(name, "->", end=" ")

    else:
        print(name)

print("\nMinimum Distance:",
      round(best_distance, 2), "units")
