# Portugal Covid-19 situation
# @ruiesteves

# Imports
import matplotlib.pyplot as plt

# Functions
def read():
    f = open("data","r")
    lines = f.readlines()

    days = [day for day in lines[0].split(" ")]
    days = days[0:len(days)-1]

    tests_by_day = [int(test) for test in lines[1].split(" ")]
    tests_by_day = tests_by_day[0:len(tests_by_day)-1]

    new_plus = [int(plus) for plus in lines[2].split(" ")]

    size = len(tests_by_day)

    new_negative = [(tests_by_day[i] - new_plus[i]) for i in range(size)]
    plus_percentage = [round((new_plus[i]/tests_by_day[i])*100,3) for i in range(size)]
    return days, tests_by_day, new_plus, new_negative, plus_percentage, size

def cumulative():
    days, tests_by_day, new_plus, new_negative, plus_percentage, size = read()
    cumulative_plus = []
    cumulative_total = []
    for i in range(size):
        if i == 0:
            cumulative_plus.append(new_plus[i]+112)
            cumulative_total.append(tests_by_day[i]+1136)
        else:
            cumulative_plus.append(cumulative_plus[i-1] + new_plus[i])
            cumulative_total.append(cumulative_total[i-1] + tests_by_day[i])

    return cumulative_plus, cumulative_total

def max_list(list):
    max = 0
    for item in list:
        if item > max:
            max = item
    return max
