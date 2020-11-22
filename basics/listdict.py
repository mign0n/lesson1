a_list = [3, 5, 7, 9, 10.5]
print(a_list)
a_list.append('Python')
print(len(a_list))

print(a_list[0])
print(a_list[-1])
a_list.remove('Python')

a_dict = {"city": "Москва", "temperature": "20"}
print(a_dict['city'])
a_dict['temperature'] = str(int(a_dict['temperature']) - 5)
print(a_dict)

print(a_dict.get('country'))
print(a_dict.get('country', 'Россия'))
a_dict['date'] = '27.05.2019'
print(len(a_dict))
