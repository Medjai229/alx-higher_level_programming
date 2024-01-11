#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    sum_weighted_numbers = sum(value * weight for value, weight in my_list)
    sum_weight = sum(weight for value, weight in my_list)

    if sum_weight == 0:
        return (0)

    return (sum_weighted_numbers / sum_weight)
