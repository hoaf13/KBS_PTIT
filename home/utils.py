# Bộ suy diễn

import numpy as np

def bmi_calculator(weight, height):
    # param :weight: (kg)
    # param :height: (cm)
    res = weight/((height/100)*(height/100))
    return res 


def tdee_calculator(weight, height, age, activity_level, gender):
    # param :weight: (kg)
    # param :height: (cm)
    # param :age: 
    # param :activity_level: 
    # param :gender: (0-nam|1-nu)
    print(weight, height, age, activity_level, gender)
    r = None
    if activity_level == 0:
        r = 1.2
    if activity_level == 1:
        r = 1.375
    if activity_level == 2:
        r = 1.55
    if activity_level == 3:
        r = 1.725
    bmr = None
    if gender == 0:
        bmr = 13.397 * weight + 4.799 * height - 5.677 * age + 88.362
    if gender == 1:
        bmr = 9.247 * weight + 3.098 * height - 4.33 * age + 447.593
    tdee = bmr * r
    return tdee

def cbr_calculator(problem, cases, weights):
    problem, cases, weights = np.array(problem), np.array(cases), np.array(weights)
    result, index = 0, 0
    for i, case in enumerate(cases):
        distances = (weights * (1 / (np.abs(problem - case) + 1))).sum() / weights.sum()
        if distances > result:
            result = distances
            index = i
    return index

def byte2string(byte_obj):
    return byte_obj.decode("utf-8") 

