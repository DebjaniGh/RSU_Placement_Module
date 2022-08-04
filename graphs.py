import genetic_modular
import memetic_modular
import mem2

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# GENETIC
def rsu_count_versus_fitness(start, end):
    best = []
    average = []
    median = []

    for x in range(start, end):
        t = genetic_modular.genetic_algorithm(GENERATION_COUNT=40, RSU_COUNT=x)
        best.append(t[0])
        average.append(t[1])
        median.append(t[2])

    plt.xticks(range(start, end))
    plt.plot(range(start, end), best, label="Best")
    plt.plot(range(start, end), average, label="Average")
    plt.plot(range(start, end), median, label="Median")
    plt.xlabel('RSU Count')
    plt.ylabel('Fitness')
    plt.title('Fitness vs RSU Count')
    plt.legend()
    plt.grid(linestyle='dotted')
    plt.show()


def rsu_coverage_area_versus_fitness(start, end, jump):
    best = []
    average = []
    median = []

    for x in range(start, end, jump):
        t = genetic_modular.genetic_algorithm(GENERATION_COUNT=40, RSU_COVERAGE_AREA=x)
        best.append(t[0])
        average.append(t[1])
        median.append(t[2])

    plt.xticks(range(start, end, jump))
    plt.plot(range(start, end, jump), best, label="Best")
    plt.plot(range(start, end, jump), average, label="Average")
    plt.plot(range(start, end, jump), median, label="Median")
    plt.xlabel('RSU Coverage Area')
    plt.ylabel('Fitness')
    plt.title('Fitness vs RSU Coverage Area')
    plt.legend()
    plt.grid(linestyle='dotted')
    plt.show()


def selection_ratio_versus_fitness(start, end, jump):
    best = []
    average = []
    median = []
    x = []

    val = start
    while val < end:
        x.append(val)
        t = genetic_modular.genetic_algorithm(GENERATION_COUNT=40, SELECTION_RATIO=val, POPULATION_SIZE=70)
        best.append(t[0])
        average.append(t[1])
        median.append(t[2])
        val += jump

    best_spline = make_interp_spline(x, best)
    average_spline = make_interp_spline(x, average)
    median_spline = make_interp_spline(x, median)
    x_new = np.linspace(x[0], x[-1], 300)
    plt.plot(x_new, best_spline(x_new), label="Best")
    plt.plot(x_new, average_spline(x_new), label="Average")
    plt.plot(x_new, median_spline(x_new), label="Median") 
    plt.xlabel('Selection Ratio')
    plt.ylabel('Fitness')
    plt.title('Fitness vs Selection Ratio')
    plt.legend()
    plt.grid(linestyle='dotted')
    plt.show()


# rsu_count_versus_fitness(3, 10)
# rsu_coverage_area_versus_fitness(10, 100, 10)
# selection_ratio_versus_fitness(0.1,1,0.1)
# population_size_versus_fitness(6, 12, 1)
# genetic_modular.genetic_algorithm(plot_graph=True)


# MEMETIC

def plot_genetic_and_modular_graphs():
    generation_count = 20
    ga_best_fitness, ga_avg_fitness = genetic_modular.genetic_algorithm(GENERATION_COUNT=generation_count, get_graph_coordinates=True)
    ma_best_fitness, ma_avg_fitness = memetic_modular.genetic_algorithm(GENERATION_COUNT=generation_count, get_graph_coordinates=True)
    ma2_best_fitness, ma2_avg_fitness = mem2.genetic_algorithm(GENERATION_COUNT=generation_count,
                                                                        get_graph_coordinates=True)
    x = [i+1 for i in range(generation_count)]
    plt.xticks(x)
    plt.plot(x, ga_best_fitness, color='r', label='GA Best Fitness')
    plt.plot(x, ga_avg_fitness, color='g', label='GA Average Fitness')
    plt.plot(x, ma_best_fitness, color='b', label='MFRD Best Fitness')
    plt.plot(x, ma_avg_fitness, color='y', label='MFRD Average Fitness')
    plt.plot(x, ma2_best_fitness, color='c', label='GARHC Best Fitness')
    plt.plot(x, ma2_avg_fitness, color='m', label='GARHC Average Fitness')
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Fitness vs Generation')
    plt.axis([0, generation_count, min(ga_best_fitness + ma_best_fitness + ma2_best_fitness)/3, 1.2*max(ga_best_fitness + ma_best_fitness + ma2_avg_fitness)])
    plt.legend()
    plt.grid(linestyle='dotted')
    plt.show()

plot_genetic_and_modular_graphs() 