#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:51:26 2024

@author: sstprk
"""
import numpy as np
import matplotlib.pyplot as plt
import timeit as t

from genetic_tsp import Genetic
from tabu_tsp import Tabu
from simulated_ann_tsp import SimulatedAnnealing

def measureTimeAn(res, time, cost):
    for v in cost:
        clas = SimulatedAnnealing(v)
        
        starting_time = t.default_timer()
        sol, sol_cost= clas.annealing_run(300)
        end = t.default_timer() - starting_time
        time.append(end)
        res.append([sol, sol_cost])
    
    return time, res

def measureTimeGen(res, time, cost):
    for v in cost:
        clas = Genetic(v)
        
        starting_time = t.default_timer()
        sol, sol_cost= clas.genetic_run(300)
        end = t.default_timer() - starting_time
        time.append(end)
        res.append([sol, sol_cost])
    
    return time, res

def measureTimeTabu(res, time, cost):
    for v in cost:
        clas = Tabu(v)
        
        starting_time = t.default_timer()
        sol, sol_cost= clas.tabu_run(300, 5)
        end = t.default_timer() - starting_time
        time.append(end)
        res.append([sol, sol_cost])
    
    return time, res

if __name__ == "__main__":
    np.random.seed(1)
    n = [5, 10, 20, 30, 40]
    costs = []
    time_Ann = []
    results_Ann = []
    time_Gen = []
    results_Gen = []
    time_Tabu = []
    results_Tabu = []
    
    for i in n:
        cost_matrix_complex = np.random.randint(1,30, (i, i))
        
        for idx in range(cost_matrix_complex.shape[0]):
            cost_matrix_complex[idx][idx] = 0
            
        costs.append(cost_matrix_complex)
    
    time_Ann, results_Ann = measureTimeAn(results_Ann, time_Ann, costs)
    
    time_Gen, results_Gen = measureTimeGen(results_Gen, time_Gen, costs)
    
    time_Tabu, results_Tabu = measureTimeTabu(results_Tabu, time_Tabu, costs)
    
    plt.figure(0)
    plt.plot(n, time_Ann, color="green", label="Annealing")
    plt.scatter(n, time_Ann, color="green")
    
    plt.plot(n, time_Gen, color="red", label="Genetic")
    plt.scatter(n, time_Gen, color="red")
    
    plt.plot(n, time_Tabu, color="blue", label="Tabu")
    plt.scatter(n, time_Tabu, color="blue")
    
    plt.grid(visible=True)
    
    plt.legend()
    
    plt.xlabel("Number of destinations (n)")
    plt.ylabel("Execution time")
    
    plt.show()
    

