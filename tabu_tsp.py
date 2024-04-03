#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:13:03 2024

@author: sstprk
"""
import numpy as np

#Cost function
def cost(solution, cost_matrix):
    
    cost = 0
    
    for idx in range(len(solution)-1):
        
        loc1 = solution[idx] - 1
        loc2 = solution[idx+1]-1
        
        cost += cost_matrix[loc1][loc2]
        
    cost += cost_matrix[solution[len(solution)-1]-1][solution[0]-1]
    
    return cost

#Function for generating neighbors
def generate_neighbors(solution):
    
    neighbors = []
    for i in range(len(solution)):
        
        for j in range(i+1, len(solution)):
            
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            
            neighbors.append(neighbor)
            
    return neighbors

#Main function
def tabu_search_main(initial_solution, max_iteration, tabu_list_size, cost_matrix):
    
    tabu_list = []
    best_solution = initial_sol
    current_solution = initial_sol
    best_neighbor_cost = float("inf")
    
    for i in range(max_iteration):
        neighbors = generate_neighbors(current_solution)
        best_neighbor = None
        
        
        for neighbor in neighbors:
            if not any(np.array_equal(neighbor, tabu) for tabu in tabu_list):
                neighbor_cost = cost(neighbor, cost_matrix)
                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost
                   
        if np.array_equal(best_neighbor, None):
            print("terminated")
            break
        
        current_solution = best_neighbor

        if len(tabu_list) > tabu_list_size:
            
            tabu_list.pop(0)
            
        if cost(current_solution, cost_matrix) < cost(best_solution, cost_matrix):
            
            best_solution = current_solution
            tabu_list.append(current_solution)

        
        if i % 1 == 0:
            print(f"Tabu list: {tabu_list}")
            print(f"Best solution on the current iteration: {best_solution}, Cost: {cost(best_solution, cost_matrix)}")
            
    print(f"Solution: {best_solution, cost(best_solution, cost_matrix)}")
    return best_solution
    

np.random.seed(0)

initial_sol = np.array([2, 1, 5, 4, 3, 6])

#For the case that each interspace between destinations has different costs for going and returning.
cost_matrix_complex = np.array([[0, 10, 20, 3, 9, 8],
                                [7, 0, 9, 19, 4, 1],
                                [6, 18, 0, 12, 3, 18],
                                [10, 2, 6, 0, 13, 15],
                                [13, 9, 12, 19, 0, 3],
                                [5, 11, 8, 2, 10, 0]])
#Different from previos matrix, it has the same cost for each direction from one destination to another
cost_matrix = np.array([[0, 10, 6, 3, 13, 5],
                       [10, 0, 9, 19, 4, 11],
                       [6, 9, 0, 6, 12, 8],
                       [3, 19, 6, 0, 7, 2],
                       [13, 4, 12, 7, 0, 10],
                       [5, 11, 8, 2, 10, 0]])

costt = cost(initial_sol, cost_matrix)
print(costt)

solution = tabu_search_main(initial_sol, 1000, 5, cost_matrix_complex)