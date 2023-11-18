# Basic program to explain Python dictionaries

my_dict = {
    'aanya': '11-Feb',
    'vihaan': '27-Nov',
    'sunny': '18-Aug',
    'bhoomika': '15-Sep'
}

name = input('Enter name: ')

# print(my_dict['yamini'])

if name in my_dict:
    bday = my_dict[name]
    print('Birthday of ' + name + ' is ' + bday)
else:
    print('Error: name not found')

for key, value in my_dict.items():
    print(key, value)