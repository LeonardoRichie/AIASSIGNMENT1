import random
#distance between cities and their distances
nodecity = {
    'a': {'c': 10,'b': 12, 'g': 12},
    'b': {'a': 12, 'd': 12, 'c': 8},
    'c': {'a': 10, 'e': 3, 'g': 9,'b': 8, 'd': 11},
    'd': {'b': 12, 'e': 11,'c': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'e': 6,'d': 10, 'g': 9},
    'g': {'a': 12,  'e': 7, 'c': 9, 'f': 9}
}

def mutation(route):#perform mutation on routes
    idx1, idx2 = sorted(random.sample(range(1, len(route) - 1), 2))  # Get two distinct indices and sort them
    route[idx1:idx2+1] = reversed(route[idx1:idx2+1])  # Reverse the segment between idx1 and idx2
    return route

def distTotal(route):#total distance route
    total = 0
    for i in range(len(route) - 1):
        if route[i] in nodecity and route[i+1] in nodecity[route[i]]:
            total += nodecity[route[i]][route[i+1]]
        else:
            return float('inf') 
    if route[-1] in nodecity and route[0] in nodecity[route[-1]]:
        total += nodecity[route[-1]][route[0]]
    else:
        return float('inf')  
    return total

#state population
popSize = 50
population = [['a', 'b', 'c', 'd', 'e', 'f', 'g'] for _ in range(popSize)]

#Generation Loop
numGen = 1000 #1000x
for generation in range(numGen):
    fitness = [1 / distTotal(route) for route in population]
    parents = random.choices(population, weights=fitness, k=popSize)


    newPop = []#Create population
    for i in range(popSize // 2):
        parent1, parent2 = parents[i], parents[i + popSize // 2]
        crossover_point = random.randint(1, len(parent1) - 2) 
        child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
        newPop.extend([mutation(child1), mutation(child2)])
    population = newPop

cityTraveled = min(population, key=lambda route: distTotal(route)) #best route
shortest = distTotal(cityTraveled)




#print output
print(f"Best Route: {' -> '.join(cityTraveled)}" + " -> a")
print(f"Shortest Distance: {shortest}")
