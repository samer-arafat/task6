# Q1
my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict['name'])
my_dict.update({'workplace': 'workplace'})
print(my_dict)

#   Q2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
dict = dict(my_tuple)
print(dict)

# Q3
dic1 = {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
n_dict ={'name': 'Dema', 'age': 20,'job': 'Engineer', 'ID': 456367, 'Year': 2003 }
print(n_dict)

# Q4
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}

# Q5
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
if 'id' in my_dict:
    print(True)
else:
    print(False)