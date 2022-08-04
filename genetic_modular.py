import random
import matplotlib.pyplot as plt

# SUMO SETUP STARTS 
import os, sys
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
# SUMO SETUP ENDS
import sumolib

# FETCHING NODES STARTS
net = sumolib.net.readNet('Map/map.net.xml')
nodes = net.getNodes()
# FETCHING NODES ENDS

def genetic_algorithm(
    RSU_COVERAGE_AREA=100,
    RSU_COUNT=6,
    POPULATION_SIZE=8,
    GENERATION_COUNT=20,
    SELECTION_RATIO=0.5,
    MUTATION_PROBABILITY=1/6,
    get_graph_coordinates=False,
):
    # INTERSECTIONS COVERED BY RSU STARTS
    def get_intersections_covered(rsu_location):
        """Returns the intersections covered by an individual."""
        global nodes
        (x, y) = nodes[rsu_location].getCoord()
        # Get all edges within RSU_COVERAGE_AREA
        edges = net.getNeighboringEdges(x, y, RSU_COVERAGE_AREA)

        # Get all nodes connected with edges
        connected_nodes = set()
        for edge in edges:
            connected_nodes.add(edge[0].getFromNode())
            connected_nodes.add(edge[0].getToNode())
        
        intersections_covered = set()
        for node in connected_nodes:
            dist = (x-node.getCoord()[0])**2 + (y-node.getCoord()[1])**2
            if dist < RSU_COVERAGE_AREA**2:
                intersections_covered.add(node)
        return intersections_covered
    # INTERSECTIONS COVERED BY RSU END

    LOCATION_COUNT = len(nodes)
    print('Number of nodes: ' + str(LOCATION_COUNT))
    
    def fitness_function(x):
        """Returns the fitness level of a particular individual."""
        sum = 0
        total_intersections_covered = set()
        for rsu_location in x:
            total_intersections_covered = total_intersections_covered.union(get_intersections_covered(rsu_location))
        
        return len(total_intersections_covered)

    def crossover(parent1, parent2):
        """Generates child from two offsprings using single-point crossover."""
        lst = []
        point = random.randint(1, RSU_COUNT-2)

        for i in range(point+1):
            lst.append(parent2[i])
        
        for i in range(point+1, RSU_COUNT):
            lst.append(parent1[i])

        return tuple(lst)

    def mutate(child):
        """Mutates an individual."""
        lst = list(child)
        random_value = random.uniform(0,1)
        if random_value < MUTATION_PROBABILITY:
            random_index = random.randint(0, RSU_COUNT - 1)
            random_location = random.randint(0, LOCATION_COUNT - 1)
            lst[random_index] = random_location
        return tuple(lst)

    # Generating a random population.
    population = []
    for _ in range(POPULATION_SIZE):
        lst = []
        for _ in range(RSU_COUNT):
            lst.append(random.randint(0, LOCATION_COUNT-1))

        population.append(tuple(lst))

    print('Initial population:', population)

    best_fitness = []
    avg_fitness = []
    for _ in range(GENERATION_COUNT):
        population.sort(key = fitness_function, reverse=True)
        best_fitness.append(fitness_function(population[0]))
        avg_fitness.append(sum(fitness_function(x) for x in population)/POPULATION_SIZE)

        # Selecting population as per SELECTION_RATIO.
        selected_population = int(POPULATION_SIZE*SELECTION_RATIO)
        new_generation = population[0:selected_population]
        offspring = []
        # Creating the new population to replace the less fit individuals.
        for _ in range(POPULATION_SIZE-selected_population):
            parents = random.choices(new_generation, k = 2)
            child = crossover(parents[0], parents[1])
            mutated_child = mutate(child)
            offspring.append(mutated_child)
        # print(offspring)
        new_generation.extend(offspring)

        population = new_generation

    population.sort(key = fitness_function, reverse=True)
    print('Final population:', population)

    # PLOTTING GRAPHS STARTS
    if get_graph_coordinates:
        return (best_fitness, avg_fitness)
    # PLOTTING GRAPH ENDS

    mid = len(population)//2
    return (
        fitness_function(population[0]),
        sum(fitness_function(x) for x in population)/POPULATION_SIZE,
        (fitness_function(population[mid]) + fitness_function(population[~mid]))/2,
    )
    # GENETIC ALGORITHM ENDS

