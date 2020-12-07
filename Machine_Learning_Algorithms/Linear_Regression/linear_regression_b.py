# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:48:21 2019

@author: Soham Shah
"""

# y = mx + b 

# m is slope, b is y-intercept 


import numpy as np

import pandas as pd

points = pd.read_csv('Salary_Data.csv')



# minimize the "sum of squared errors". This is how we calculate and correct our error

def compute_error_for_line_given_points(b,m,points):

	totalError = 0 	#sum of square error formula

	for i in range (0, len(points)):

		x = points[i, 0]

		y = points[i, 1]

		totalError += (y-(m*x + b)) ** 2

	return totalError/ float(len(points))




def stepGradient(b_current, m_current, points, learningRate):

    b_gradient = 0 
 
    m_gradient = 0 

    N = float(len(points)) 

    for i in range(0, len(points)): 
    
       b_gradient += -(2/N) * (points[i].y - ((m_current*points[i].x) +  b_current)) 
    
       m_gradient += -(2/N) * points[i].x * (points[i].y - ((m_current * points[i].x) + b_current)) 
    
    new_b = b_current - (learningRate * b_gradient) 
    
    new_m = m_current - (learningRate * m_gradient) 
    
    return [new_b, new_m]



def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteartions):

	b = starting_b

	m = starting_m

	for i in range(num_iteartions):

		b,m = stepGradient(b, m, points, learning_rate)

	return [b,m]


"""def run():

	#Step 1: Collect the data

	points = genfromtxt('data.csv', delimiter=',')

	#Step 2: Define our Hyperparameters

	learning_rate = 0.0001 #how fast the data converge

	#y=mx+b (Slope formule)

	initial_b = 0 # initial y-intercept guess

	initial_m = 0 # initial slope guess

	num_iteartions = 1000

	print("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points)))

    print("Running...")

    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)

    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points)))
"""



# main function

if __name__ == "__main__":

	run()


