#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:51:26 2024

@author: sstprk
"""
import numpy as np

from genetic_tsp import Genetic
from tabu_tsp import Tabu

cost_matrix_complex = np.array([[0, 10, 20, 3, 9, 8],
                                [7, 0, 9, 19, 4, 1],
                                [6, 18, 0, 12, 3, 18],
                                [10, 2, 6, 0, 13, 15],
                                [13, 9, 12, 19, 0, 3],
                                [5, 11, 8, 2, 10, 0]])

cost_matrix_complex = np.array([[0, 10, 20, 3, 9, 8],
                                [7, 0, 9, 19, 4, 1],
                                [6, 18, 0, 12, 3, 18],
                                [10, 2, 6, 0, 13, 15],
                                [13, 9, 12, 19, 0, 3],
                                [5, 11, 8, 2, 10, 0]])
initialsol = [1, 2, 3, 4, 5, 6]

gen = Genetic(cost_matrix_complex, 6)

"""genee = gen.init_generation(initialsol)

new = gen.new_generation(genee)"""

solution = gen.genetic_run(1000)
