#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 23:13:03 2024

@author: sstprk
"""
import numpy as np

class Tabu:
    def __init__(self, cost_matrix):
        """
        
        """
        
        self.cost_matrix = cost_matrix
        self.destination_count = cost_matrix.shape[0]
    
    def cost(self, solution):
        """
        Objective function of the algorithm for calculating the fitness of given solution. For this case it calculating fitness by only considering the cost matrix as a factor. Returns total cost of the solution as an integer.
        """
        
        cost = 0
        
        for idx in range(len(solution)-1):
            
            loc1 = solution[idx] - 1
            loc2 = solution[idx+1]-1
            
            cost += self.cost_matrix[loc1][loc2]
            
        cost += self.cost_matrix[solution[len(solution)-1]-1][solution[0]-1]
        
        return cost
    
    #Function for generating neighbors
    def generate_neighbors(self, solution):
        """
        Function for generating possible neighbors. Takes an initial solution as input. Returns the new generated neighbours as a list.
        """
        
        neighbors = []
        for i in range(1, len(solution)-1):
            
            for j in range(i+1, len(solution)):
                if i != j:
                    neighbor = solution.copy()
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    
                    neighbors.append(neighbor)
                
        return neighbors
    
    #Main function
    def tabu_run(self, max_iteration, tabu_list_size):
        """
        
        """
        
        tabu_list = []
        initial_sol = np.array([element for element in range(1, self.destination_count+1)])
        best_solution = initial_sol
        current_solution = initial_sol
        best_neighbor_cost = float("inf")
                
        for i in range(max_iteration):
            best_neighbor = None
            neighbors = self.generate_neighbors(current_solution)
            
            for neighbor in neighbors:
                if not any(np.array_equal(neighbor, tabu) for tabu in tabu_list):
                    neighbor_cost = self.cost(neighbor)
                    if neighbor_cost < best_neighbor_cost:
                        best_neighbor = neighbor
                        best_neighbor_cost = neighbor_cost
                       
                    
            if np.array_equal(best_neighbor, None):
                print("terminated")
                break
            
            current_solution = best_neighbor
            tabu_list.append(best_neighbor)
    
            if len(tabu_list) > tabu_list_size:
                
                tabu_list.pop(0)
                
            if self.cost(current_solution) < self.cost(best_solution):
                
                best_solution = current_solution
    
            
            if i % (max_iteration // 10) == 0:
                print(f"Tabu list: {tabu_list}")
                print(f"Best solution on the {i}. iteration: {best_solution}, Cost: {self.cost(best_solution)}")
        print("------------------------------------------------------------")
        print(f"Best solution is the {i}. solution: {self.cost(best_solution)}")
        print("------------------------------------------------------------")

        return list(best_solution), self.cost(best_solution)
    