person = {
    'first_name':'John',
    'last_name':'Doe',
    'age':30
}
#unordered, unchange, indexed
person = dict(first_name = 'John',last_name = 'Doe', age = 30)
print(person)
print(person.get('last_name'))
#add an item
person['phone'] = '55555555'
#get keys
print(person.keys())
print(person.items())

person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# remove item
del(person['age'])
person.pop('phone')
print (person)


person.clear()

print(len(person2))
print(person)


# List of dict
people = [
    {'name' : 'Martha', 'age' : 40},
    {'name':'Bob','age':20 }
]
print(people[1]['name'])