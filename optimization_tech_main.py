#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:51:26 2024

@author: sstprk
"""
import numpy as np

from genetic_tsp import Genetic
from tabu_tsp import Tabu
from simulated_ann_tsp import SimulatedAnnealing

np.random.seed(1)

cost_matrix_complex = np.random.randint(1,30, (50,50))

for idx in range(cost_matrix_complex.shape[0]):
    cost_matrix_complex[idx][idx] = 0

gen = Genetic(cost_matrix_complex, 50)
tabu = Tabu(cost_matrix_complex, 50)
simulann = SimulatedAnnealing(cost_matrix_complex, 50)

"""
genee = gen.create_generation(initialsol)

new = gen.new_generation(genee)

gen2 = gen.new_generation(new)"""

print("GENETIC ALGORITHM")
print("------------------------------------------------------------")

solution_gen = gen.genetic_run(500)

print("TABU SEARCH ALGORITHM")
print("------------------------------------------------------------")

#solution_tabu = tabu.tabu_run(500, 5)

print("SIMULATED ANNEALING ALGORITHM")
print("------------------------------------------------------------")

#solution_ann = simulann.annealing_run(500)

