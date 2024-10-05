
import timeit
import random
import pandas as pd
from random import sample
import math
import matplotlib.pyplot as plt
import numpy as np

temperature = 1                 # initial temperature to start anneal with
alpha = 0.9999                  # fraction by which temperature is reduced in each iteration
minimum_temperature = 0.00001   # threshold for stopping iterations once temperature is very low
number_of_iterations = 10000
number_of_nodes = 20            # customer size (upto '400')


''' following function generates coordinates (x,y) of 'n' customer nodes in a [n,2] array '''

def generateCoordinates():
    data = pd.read_csv('MVRP_400N.txt', ' ')
    df = pd.DataFrame(data)
    coordinates = np.empty([number_of_nodes, 2])
    for i in range(number_of_nodes):
        for j in range(2):
            coordinates[i, 0] = df["X"][i]
            coordinates[i, 1] = df["Y"][i]
    return coordinates


coordinates = generateCoordinates()


''' this class passes coordinates of customer grid and do distance calculations between nodes '''

class distances:

    def __init__(self, coordinates):
        self.grid = coordinates
        self.distance_grid = np.empty((len(self.grid), len(self.grid)))

    ''' following function is to create 'n' by 'n' array storing distance from one node to other in respective cells'''

    def distance_matrix(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.distance_grid[i, j] = math.sqrt(
                    ((self.grid[i][0] - self.grid[j][0]) ** 2 + (self.grid[i][1] - self.grid[j][1]) ** 2))
        return self.distance_grid

    def get_distance_matrix(self):
        return self.distance_matrix()

    def distanclass distances:

    def __init__(self, coordinates):
        self.grid = coordinates
        self.distance_grid = np.empty((len(self.grid), len(self.grid)))

    ''' following function is to create 'n' by 'n' array storing distance from one node to other in respective cells'''

    def distance_matrix(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                self.distance_grid[i, j] = math.sqrt(
                    ((self.grid[i][0] - self.grid[j][0]) ** 2 + (self.grid[i][1] - self.grid[j][1]) ** 2))
        return self.distance_grid

    def get_distance_matrix(self):
        return self.distance_matrix()

    def distance(self, node1, node2):
        return self.distance_grid[node1, node2]

    ''' calculating total distance in a tour'''

    def tour_cost(self, tour=[]):
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += self.distance_grid[tour[i], tour[i + 1]]
        total_distance += self.distance_grid[tour[len(tour) - 1], tour[0]]
        return total_distance

    ''' passes list of nodes in a tour and returns respective coordinates of customer nodes'''

    def generate_coordinates(self, tour=[]):
        tour_coordinates = np.empty([len(tour), 2])
        for i in range(len(tour)):
            for j in range(2):
                tour_coordinates[i, j] = self.grid[tour[i], j]
        return tour_coordinates.astype('int')ce(self, node1, node2):
        return self.distance_grid[node1, node2]

    ''' calculating total distance in a tour'''

    def tour_cost(self, tour=[]):
        total_distance = 0
        for i in range(len(tour) - 1):
            total_distance += self.distance_grid[tour[i], tour[i + 1]]
        total_distance += self.distance_grid[tour[len(tour) - 1], tour[0]]
        return total_distance

    ''' passes list of nodes in a tour and returns respective coordinates of customer nodes'''

    def generate_coordinates(self, tour=[]):
        tour_coordinates = np.empty([len(tour), 2])
        for i in range(len(tour)):
            for j in range(2):
                tour_coordinates[i, j] = self.grid[tour[i], j]
        return tour_coordinates.astype('int')


''' nearest neighbor as a greedy heuristic to create initial good solution'''

class nearestNeighborSearch:

    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.solution = []

    def NNS(self):
        self.N = len(self.coordinates)
        free_nodes = []
        dist = distances(self.coordinates)
        dist.get_distance_matrix()
        for i in range(self.N - 1):
            free_nodes.append(i + 1)
        current_node = 0
        self.solution = [current_node]
        while free_nodes:
            next_node = min(
                free_nodes, key=lambda x: dist.distance(current_node, x))
            free_nodes.remove(next_node)
            self.solution.append(next_node)
            current_node = next_node
        return self.solution


''' simulated annealing to improve initial solution achieved from NNS,
it iterates with declining temperature of annealing, escaping local optima and
trying to locate global optima within threshold values '''


class simulatedAnnealing:

    def __init__(self, t0, iterations, alpha, least_temp, coordinates):
        self.init_temp = t0
        self.num_iter = iterations
        self.temp_threshold = least_temp
        self.temp_fraction = alpha
        self.coordinates = coordinates
        self.num_nodes = len(self.coordinates)
        self.best_tour = []
        self.explored_tour = []

# next state is generated by altering previous tour by reversing a segment of route from a customer to another customer

    def generate_state(self, tour=[]):
        new_tour = list(tour)
        l = random.randint(1, len(tour) - 1)
        i = random.randint(1, len(tour) - l)
        new_tour[i: (i + l)] = reversed(new_tour[i: (i + l)])
        return new_tour

    def SA(self):
        temp = self.init_temp
        nns = nearestNeighborSearch(coordinates)
        dist = distances(coordinates)
        dist.get_distance_matrix()
        current_tour = nns.NNS()
        self.best_tour = current_tour
        self.explored_tour.append(current_tour)
        self.best_tempr = 0
        self.iter_to_opt = 0
        for i in range(self.num_iter):
            new_tour = self.generate_state(current_tour)
            if new_tour not in self.explored_tour and temp >= self.temp_threshold:
                self.explored_tour.append(new_tour)
                d1 = dist.tour_cost(current_tour)
                d2 = dist.tour_cost(new_tour)
                if d1 >= d2:  # if new solution is better than previous one, accept it right away
                    for i in range(len(new_tour)):
                        current_tour = new_tour
                else:
                    delta = d2 - d1
                    # calculate probability if new solution is not better than previous
                    probability = np.exp(-delta / temp)
                    # keep solution if probability is better than a random probability between 0 and 1.
                    if probability >= np.random.normal(0.50, 0.005):
                        current_tour = new_tour
                if dist.tour_cost(current_tour) <= dist.tour_cost(self.best_tour):
                    self.best_tour = current_tour
                    self.best_tempr = temp
                    self.iter_to_opt = i
                # reduce temperature for next iteration by pre-defined fraction.
                temp *= self.temp_fraction

        return self.best_tour, dist.tour_cost(self.best_tour), self.best_tempr, self.iter_to_opt


tsp = simulatedAnnealing(temperature, number_of_iterations,alpha, minimum_temperature, coordinates)
dist = distances(coordinates)
dist.get_distance_matrix()
nns = nearestNeighborSearch(coordinates)
nns.NNS()
start_sa = timeit.default_timer()
tsp.SA()
end_sa = timeit.default_timer()
start_nns = timeit.default_timer()
print('\nInitial solution by NNS is:', dist.tour_cost(nns.solution))
end_nns = timeit.default_timer()
print('\nBest tour found is:', tsp.best_tour)
print('\nMinimum distance covered is:', dist.tour_cost(tsp.best_tour))
print('\nBest temperature to get optimal solution:', tsp.best_tempr)
print('\nIterations completed to get optimal solution:', tsp.iter_to_opt)
print('\nSolution improved by SA is:', dist.tour_cost(
    nns.solution) - dist.tour_cost(tsp.best_tour))
print('\nTime taken by NNS is:', end_nns - start_nns)
print('\nTime taken by SA is:', end_sa - start_sa)

'''for simplicity, the following function plots all components line by line '''

def plotSA():
    dist_list = []
    dist = distances(coordinates)
    dist.get_distance_matrix()
    x = []
    for i in range(len(tsp.explored_tour)):
        x.append(i)
    for i in tsp.explored_tour:
        dist_list.append(dist.tour_cost(i))
    xx, yy = dist.generate_coordinates(tsp.best_tour)[:, 0],  dist.generate_coordinates(tsp.best_tour)[:, 1]
    depot = tsp.coordinates[0]
    _xx, _yy = [xx[0], xx[tsp.num_nodes - 1]], [yy[0], yy[tsp.num_nodes - 1]]

    plt.subplot(2, 2, 1)
    plt.scatter(depot[0], depot[1], marker='o')
    plt.plot([dist.generate_coordinates(nns.solution)[:, 0][0], dist.generate_coordinates(nns.solution)[:, 0][tsp.num_nodes - 1]],[dist.generate_coordinates(nns.solution)[:, 1][0], dist.generate_coordinates(nns.solution)[:, 1][tsp.num_nodes - 1]], 'x-', color='b')
    plt.plot(dist.generate_coordinates(nns.solution)[:, 0], dist.generate_coordinates(nns.solution)[:, 1], 'x-', color='b')
    plt.text(depot[0] + 0.5, depot[1] + 0.5, str('D')), plt.title('Nearest Neighbor Search - VRP'), plt.ylabel('Y-Coordinates')

    plt.subplot(2, 2, 3)
    plt.scatter(depot[0], depot[1], marker='o')
    plt.plot(_xx, _yy, 'x-', color='b')
    plt.plot(xx, yy, 'x-', color='b')
    plt.text(depot[0] + 0.5, depot[1] + 0.5, str('D')), plt.title('Simulated Annealing - VRP'), plt.xlabel('X-Coordinates'), plt.ylabel('Y-Coordinates')

    plt.subplot(1, 2, 2)
    plt.scatter(dist_list.index(min(dist_list)),min(dist_list), color='g', marker='x')
    plt.axhline(y=min(dist_list), color='g',linestyle='-', label='SA Solution')
    plt.text(dist_list.index(min(dist_list)) + 1, min(dist_list) +0.5, 'SA Solution:' + ' ' + str(round(min(dist_list), 2)))
    plt.axhline(y=dist.tour_cost(nns.solution), color='r',linestyle='-', label='NNS Solution')
    plt.scatter(0, dist.tour_cost(nns.solution), color='r', marker='x')
    plt.text(1, dist.tour_cost(nns.solution) + 0.5, 'NNS Optimal:' +' ' + str(round(dist.tour_cost(nns.solution), 2)))
    plt.plot(x, dist_list)
    plt.title('Simulated Annealing - Cooling: SUDHAN'), plt.xlabel('Iterations'), plt.ylabel('Total Cost')
    plt.show()


graph = plotSA()