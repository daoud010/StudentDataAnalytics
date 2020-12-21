import csv
from collections import namedtuple


# Group your data
def group_values_with_columns(data, col_req, **kwargs):
    Student = namedtuple('Student', 'GPA Gender drink exercise fries income sports weight')
    columns_index = [data[0].index(name) for name in col_req]

    if kwargs:
        individuals = data[1:kwargs['n'] + 1]
    else:
        individuals = data[1:51]  # 50 by default

    grouped_data = []  # list of tuples of columns and values

    for individual in individuals:
        value = [individual[i] for i in columns_index]
        grouped_data.append(Student._make(value))

    return grouped_data


# Get length of a particular list
def count(func):
    def wrapper(*args):
        result = func(*args)
        result = len(result)
        return result

    return wrapper


# Get females from the grouped_data
@count
def get_females(data):
    return [entry for entry in data if entry.Gender == "1"]


# Get males from the grouped_data
@count
def get_males(data):
    return [entry for entry in data if entry.Gender == "2"]


# Count using dictionaries how many people associate drink with soda and orange juice
def drink_stats(data):
    drink_count = {}

    for item in data:
        if item.drink in drink_count:
            drink_count[item.drink] += 1
        else:
            drink_count[item.drink] = 1
    return drink_count


# Collecting exercise stats
def exercise_stats(data, x):
    pattern_count = [entry for entry in data if entry.exercise == x]
    return get_males(pattern_count), get_females(pattern_count)


# Students loving Mcdonalds fries
Mcdonalds_fries = count(lambda my_data: [x for x in my_data if x.fries == '1'])

#  Maintaining academia and jobs
# bright_students = ...


# Collecting weight stats
def weight_stats(data, x):
    return


# Cleaning anomalies in weight
def weight_cleaner(func):
    return


# Cleaning anomalies in sports
def sports_cleaner(func):
    return


# Cleaning anomalies in income
def income_cleaner(func):
    return


# Cleaning anomalies in fries
def fries_cleaner(func):
    return


# Cleaning anomalies in exercise
def exercise_cleaner(func):
    return


# Cleaning anomalies in drink
def drink_cleaner(func):
    return


# Cleaning anomalies in gender
def gender_cleaner(func):
    return


# Cleaning anomalies in GPA
def gpa_cleaner(func):
    return


# Cleaning the dataset
@weight_cleaner
@sports_cleaner
@income_cleaner
@fries_cleaner
@exercise_cleaner
@drink_cleaner
@gender_cleaner
@gpa_cleaner
def clean_data(grouped_data):
    return


# ________________________________________________________________________________#


# Reading the dataset in a list
with open('food.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)  # contains the data in the raw format.

# Columns you'll deal with in this project
required_columns = ['GPA', 'Gender', 'drink', 'exercise', 'fries', 'income', 'sports', 'weight']

# Start calling the functions
grouped_data = group_values_with_columns(data, required_columns, n=60)
for entry in grouped_data:
    print(entry)
print(get_females(grouped_data))
print(get_males(grouped_data))
print(drink_stats(grouped_data))
print(exercise_stats(grouped_data, '1'))
print(exercise_stats(grouped_data, '2'))
print(Mcdonalds_fries(grouped_data))
