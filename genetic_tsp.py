#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:31:05 2024

@author: sstprk
"""

import numpy as np

def cost(solution, cost_matrix):
    
    cost = 0
    
    for idx in range(len(solution)-1):
        
        loc1 = solution[idx] - 1
        loc2 = solution[idx+1]-1
        
        cost += cost_matrix[loc1][loc2]
        
    cost += cost_matrix[solution[len(solution)-1]-1][solution[0]-1]
    
    return cost

def init_generation(initial_sol):
    generation = []
    for i in range(len(initial_sol)):
        
        for j in range(i+1, len(initial_sol)):
            
            member = initial_sol.copy()
            member[i], member[j] = member[j], member[i]
            
            generation.append(member)
            
    return generation

def choose_survivors(generation, cost_matrix):
    survivors = []
    midlen = len(generation) // 2
    np.random.shuffle(generation)
    
    for i in range(midlen):
        if cost(generation[i], cost_matrix) < cost(generation[midlen + i], cost_matrix):
            survivors.append(generation[i])
        
        else:
            survivors.append(generation[midlen + i])
            
    return survivors

def create_offsprings(parent_a, parent_b):
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

def crossover(survivors):
    offsprings = []
    midlen = len(survivors) // 2
    
    for idx in range(midlen):
        parent_a, parent_b = survivors[idx], survivors[midlen + idx]
        
        for _ in range(2):
            offsprings.append(create_offsprings(parent_a, parent_b))
            offsprings.append(create_offsprings(parent_b, parent_a))
    
    return offsprings

def mutation(generation):
    mutated_gen = []
    
    for member in generation:
        
        if np.random.randint(0, 1000) < 9:
            
            idx1, idx2 = np.random.randint(0, len(member)-1), np.random.randint(0, len(member)-1)
            member[idx1], member[idx2] = member[idx2], member[idx1]
        
        mutated_gen.append(member)
    return mutated_gen
    
def new_generation(init_generation, cost_matrix):
    survivors = choose_survivors(init_generation, cost_matrix)
    crossed_gen = crossover(survivors)
    present_generation = mutation(crossed_gen)
    
    return present_generation

def choose_best(points, paths, count):
    return sorted(paths, key=lambda path: cost(points, path))[:count]

def choose_worst(points, paths, count):
    return sorted(paths, reverse=True, key=lambda path: cost(points, path))[:count]

initial_sol = [1,2,3,4,5,6]

cost_matrix_complex = np.array([[0, 10, 20, 3, 9, 8],
                                [7, 0, 9, 19, 4, 1],
                                [6, 18, 0, 12, 3, 18],
                                [10, 2, 6, 0, 13, 15],
                                [13, 9, 12, 19, 0, 3],
                                [5, 11, 8, 2, 10, 0]])

first_gen = init_generation(initial_sol)

next_gen = new_generation(first_gen, cost_matrix_complex)

print(next_gen)
