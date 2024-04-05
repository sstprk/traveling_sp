#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:13:03 2024

@author: sstprk
"""
import numpy as np

class Tabu:
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
    