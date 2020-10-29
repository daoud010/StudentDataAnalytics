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
    return


# Get females from the grouped_data
@count
def get_females():
    return


# Get males from the grouped_data
@count
def get_males():
    return


# Count using dictionaries how many people associate drink with soda and orange juice
def drink_stats(data):
    return


# Collecting exercise stats
def exercise_stats(data, x):
    return


# Students loving Mcdonalds fries
# Mcdonalds_fries = ...

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
grouped_data = group_values_with_columns(data, required_columns, n=50)
for entry in grouped_data:
    print(entry)
