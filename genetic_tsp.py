#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:31:05 2024

@author: sstprk
"""

import numpy as np

class Genetic:
    def __init__(self, cost_matrix, destination_count):
        """
        Constructor of the class for generating a random initial solution and take a cost matrix as an input to know how many units takes to get from one location to another. 
        """
        
        if cost_matrix.shape != (destination_count, destination_count):
            raise Exception("Cost matrix and destination count are incompatible.")
            
        self.cost_matrix = cost_matrix
        self.initial_sol = list([element for element in range(1, destination_count+1)])
        
        self.first_gen = self.init_generation(self.initial_sol)
        
    def set_initial_sol(self, new_sol):
        """
        Set function for letting user to set a new initial solution respect to the destination count has been set before.
        """
        
        if len(new_sol != self.destination_count):
            raise Exception("New solution must have the same destination count as the one created initially.")
            
        self.initial_sol = new_sol
        
    def set_cost_matrix(self, new_cost_matrix):
        """
        Set function for letting user to set a new cost matrix respect to the destination count has been set before.
        """
        
        if new_cost_matrix.shape != [self.destination_count, self.destination_count]:
            raise Exception("New cost matrix and current destination count are incompatible.")
            
        self.cost_matrix = new_cost_matrix
        
    def init_generation(self, initial_sol):
        """
        Function to create the first generation of the algorithm by taking the initial solution has been created before. Returns created generation as a 2D array.
        """
        
        generation = []
        
        for i in range(len(initial_sol)):
            
            for j in range(i+1, len(initial_sol)):
                member = initial_sol.copy()

                member[i], member[j] = member[j], member[i]
                
                generation.append(member)
                
        return generation
    
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
    
    
    def choose_survivors(self, generation):
        """
        Function to choose survivors of the given generation regarding their fitness in terms of survival of the fittest. Returns choosen survivors as an array.
        """
        
        survivors = []
        midlen = len(generation) // 2
        np.random.shuffle(generation)
        
        for i in range(midlen):
            if self.cost(generation[i]) < self.cost(generation[midlen + i]):
                survivors.append(generation[i])
            
            else:
                survivors.append(generation[midlen + i])
                
        return survivors
    
    def create_offsprings(self, parent_a, parent_b):
        """
        Function to create offsprings for each application of the crossover. Creates an offspring with the given parent solutions. Returns the created offspring as an array.
        """
        
        offspring = []
        start = np.random.randint(0, len(parent_a)-1)
        end = np.random.randint(start, len(parent_a))
        
        part_a = parent_a[start:end]
        part_b = list([element for element in parent_b if not element in part_a])
        
        for i in range(len(parent_a)):
            if start <= i < end:
                offspring.append(part_a.pop(0))
                
            else:
                offspring.append(part_b.pop(0))
        
        return offspring
    
    def crossover(self, survivors):
        """
        Function for application of the crossover to the given survivors. Returns crossed new generation as a 2D array.
        """
        
        offsprings = []
        midlen = len(survivors) // 2
        
        for idx in range(midlen):
            parent_a, parent_b = survivors[idx], survivors[midlen + idx]
            
            for _ in range(2):
                offsprings.append(self.create_offsprings(parent_a, parent_b))
                offsprings.append(self.create_offsprings(parent_b, parent_a))
        
        return offsprings
    
    def mutation(self, generation):
        """
        Function for application of the mutation. Mutation is going to be applied with less then %10 probability. Returns the final generation as a 2D array.
        """
        
        mutated_gen = []
        
        for member in generation:
            
            if np.random.randint(0, 1000) < 9:
                
                idx1, idx2 = np.random.randint(0, len(member)-1), np.random.randint(0, len(member)-1)
                member[idx1], member[idx2] = member[idx2], member[idx1]
            
            mutated_gen.append(member)
        return mutated_gen
        
    def new_generation(self, generation):
        """Function for creating a new generation with applying the genetic algorithm. Returns the new generation as a 2D generation
        """
        
        survivors = self.choose_survivors(generation)
        crossed_gen = self.crossover(survivors)
        new_generation = self.mutation(crossed_gen)
        
        return new_generation
    
    def choose_best(self, solutions, count = 1):
        """
        Function to choose the best solution among the given generation or any solution array with a compatible shape considering the count. Returns the first requested amount of best solutions as an 2D array.
        """
        
        return sorted(solutions, key=lambda solution: (self.cost(solution), solution))[:count]
    
    def choose_worst(self, solutions, count = 1):
        """
        Function to choose the worst solution among the given generation or any solution array with a compatible shape considering the count. Returns the first requested amount of worst solutions as an 2D array.
        """
        
        return sorted(solutions, reverse=True, key=lambda solution: self.cost(solution))[:count]
    
    def genetic_run(self, max_iteration):
        """
        Function to execute the algorithm for travelling salesman problem by iterating throuugh given number. Returns the best solution.
        """
        
        current_gen = self.first_gen
        best_solution = self.choose_best(current_gen, 1)

        for iterr in range(max_iteration):
            
            print(current_gen)
            print(f"{iterr+1}. generation :")
            
            new_gen = self.new_generation(current_gen)
            
            print(new_gen)
            
            best_in_newgen = self.choose_best(new_gen, 1)         
            
            if self.cost(best_solution[0]) < self.cost(best_in_newgen[0]):
                best_solution = best_in_newgen
            
            current_gen = new_gen
                                
            
            print(f"Best solution : {best_solution}, Cost : {self.cost(best_solution[0])}")
            
        return best_solution