fruit_tuple = ('Apple','Orange','Mango')
#print(fruit_tuple)
fruit_tuple_2 = ('Apple',)
#print(len(fruit_tuple))
del fruit_tuple_2
#print(fruit_tuple_2)

fruit_set = {'Apple','Orange','Mango'}
print(fruit_set)
print('Apples' in fruit_set)
fruit_set.add('Grape')
fruit_set.remove('Apple')
print(fruit_set)
fruit_set.clear()
del fruit_set
