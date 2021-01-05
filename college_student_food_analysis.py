import csv
from collections import namedtuple, defaultdict, Counter


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
bright_students = lambda my_data: [x for x in my_data if x.GPA > '3' and (x.income == '5' or x.income == '6')]


# Collecting weight stats
def weight_stats(data, x):
    weight_stats_dict = defaultdict(int)

    for student in data:
        if student.weight.isnumeric():
            weight_stats_dict[student.weight] += 1

    print(weight_stats_dict)

    weight_stats_count = Counter(weight_stats_dict)

    most_common_weight = weight_stats_count.most_common(x)
    most_weight_result = [i[0] for i in most_common_weight]

    least_common_weight = weight_stats_count.most_common()[:-x - 1:-1]
    least_weight_result = [i[0] for i in least_common_weight]

    most_common_weight_v2 = [key for key in weight_stats_dict if weight_stats_dict[key] ==
                             max(weight_stats_dict.values())]
    least_common_weight_v2 = [key for key in weight_stats_dict if weight_stats_dict[key] ==
                              min(weight_stats_dict.values())]

    common_weight_females = get_females([entry for entry in data if entry.weight in most_common_weight_v2])
    least_weight_males = get_males([entry for entry in data if entry.weight in least_common_weight_v2])

    return common_weight_females, least_weight_males


# Cleaning anomalies in weight
def weight_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [weight_data for weight_data in result if entry.weight.isnumeric()]
        return result
    return wrapper


# Cleaning anomalies in sports
def sports_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [sports_data for sports_data in result if sports_data.sports == '1' or sports_data.sports == '2']
        return result

    return wrapper


# Cleaning anomalies in income
def income_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        l = ['1', '2', '3', '4', '5', '6']
        result = [income_data for income_data in result if income_data.income in l]
        return result

    return wrapper


# Cleaning anomalies in fries
def fries_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [fries_data for fries_data in result if fries_data.fries == '1' or fries_data.fries == '2']
        return result

    return wrapper


# Cleaning anomalies in exercise
def exercise_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        l = ['1', '2', '3', '4', '5']

        result = [exercise_data for exercise_data in result if exercise_data in l]
        return result

    return wrapper


# Cleaning anomalies in drink
def drink_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [drink_data for drink_data in result if drink_data.drink == '1' or drink_data.drink == '2']
        return result

    return wrapper


# Cleaning anomalies in gender
def gender_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [gender_info for gender_info in result if gender_info.Gender == '1' or gender_info.Gender == '2']
        return result

    return wrapper


# Cleaning anomalies in GPA
def gpa_cleaner(func):
    def wrapper(*args):
        result = func(*args)
        result = [gpa_data for gpa_data in result if gpa_data.GPA.replace('.', '1').isnumeric()]
        return result
    return wrapper


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
    return grouped_data


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
students = bright_students(grouped_data)
print(weight_stats(grouped_data, 2))
