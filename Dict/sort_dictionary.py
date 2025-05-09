from operator import itemgetter

data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

print(sorted(data_list, key=itemgetter('age')))

#by using lambda
print(sorted(data_list, key=lambda i: i['age']))