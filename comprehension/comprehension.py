data_list = [1, 2, 3, 4, 5]

# square
print([data * data for data in data_list])

# square only even (conditional)
print([data * data for data in data_list if data % 2 is 0])

############

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k: v * 2 for k, v in dict1.items()}
print(double_dict1)
