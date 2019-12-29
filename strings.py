name = 'Mi'
age = 27
print('Hello I am ' + name + ' amd I am ' + str(age))

#Argument by position
print('{},{},{}'.format('a','b','c'))
print('{1},{2},{0}'.format('a','b','c'))
print('My name is {name} and I am {age}' .format(name = name, age = age))
print(f'My name is {name} and I am {age}')

s = "Good morning"

# Capitalize first letter
print(s.capitalize())
#uppper
print(s.upper())
#lowercase
print(s.lower())
#get length
print(len(s))
# replace
print(s.replace('morning', 'everyone'))

#Count
sub = "o"
print(s.count(sub))
print(s.startswith('Good'))
print(s.endswith('ng'))
print(s.split())
print(s.find('G'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
