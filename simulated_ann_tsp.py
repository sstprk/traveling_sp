#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 00:18:24 2024

@author: sstprk
"""
import numpy as np

class SimulatedAnnealing:
    def __init__(self, cost_matrix, destination_count):
        """
        
        """

        if cost_matrix.shape != (destination_count, destination_count):
            raise Exception("Cost matrix and destination count are incompatible.")
            
        self.cost_matrix = cost_matrix
        self.initial_sol = list([element for element in range(1, destination_count+1)])
        
        
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
    
    def create_generation(self, initial_sol):
        """
        Function to create the first generation of the algorithm by taking the initial solution has been created before. Returns created generation as a 2D array.
        """
        
        generation = []
        
        for i in range(1, len(initial_sol)):
            
            for j in range(i+1, len(initial_sol)):
                member = initial_sol.copy()

                member[i], member[j] = member[j], member[i]
                
                generation.append(member)
                
        return generation
        
    def acceptance_check(self, current_sol, new_sol, temp):
        """
        
        """
        
        return np.exp(-(current_sol - new_sol) / temp) > np.random.random(1)[0]
    
    def choose_best(self, solutions, count = 1):
        """
        Function to choose the best solution among the given generation or any solution array with a compatible shape considering the count. Returns the first requested amount of best solutions as an 2D array.
        """
        
        return sorted(solutions, key=lambda solution: self.cost(solution))[:count]
    
    def annealing_run(self, init_temp):
        """
        
        """
        initial_gen = self.create_generation(self.initial_sol)
        current_best = self.choose_best(initial_gen)[0]
        
        for temp in reversed(range(init_temp)):
            new_gen = self.create_generation(current_best)
            new_sol = self.choose_best(new_gen)[0]
            
            if self.cost(current_best) > self.cost(new_sol):
                current_best = new_sol
                
            else:
                if self.acceptance_check(self.cost(current_best), self.cost(new_sol), temp):
                    current_best = new_sol
                    
            if temp % (init_temp // 10) == 0:
                print(f"{temp+1} degree : {current_best}, {self.cost(current_best)}")
        print("------------------------------------------------------------")
        print(f"Best solution : {self.cost(current_best)}")
        print("------------------------------------------------------------")

        return current_best
    
    
    
