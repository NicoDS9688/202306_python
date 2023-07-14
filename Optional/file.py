num1 = 42 #- variable declaration, number
num2 = 2.3 #- variable declaration, number
boolean = True #-boolean
string = 'Hello World' #- variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- variable declaration, list, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- variable declaration, dictionary, initialize
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration, tuple, initialize
print(type(fruit)) #- log statement, tuple, type check
print(pizza_toppings[1]) # log statement, list, access value
pizza_toppings.append('Mushrooms') # list, add value
print(person['name']) # log statement, dictionary, access value
person['name'] = 'George' # dictionary, add value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) # log statement, tuple, access value

if num1 > 45:  # conditional, if
    print("It's greater") # log statement 
else: # conditional, else
    print("It's lower") # log statement 

if len(string) < 5: # conditional, if
    print("It's a short word!") # log statement 
elif len(string) > 15: # conditional, else if
    print("It's a long word!") # log statement 
else: # conditional, else 
    print("Just right!") # log statement 

for x in range(5): # for loop, start
    print(x) # log statement 
for x in range(2,5):
    print(x) # log statement 
for x in range(2,10,3):
    print(x) # log statement 
x = 0 #- variable declaration, number
while(x < 5): #while loop, start
    print(x) # log statement 
    x += 1 # while loop, increment

pizza_toppings.pop() #list, delete value
pizza_toppings.pop(1) #list, delete value

print(person) # log statement 
person.pop('eye_color') #dictionary, delete value
print(person) # log statement 

for topping in pizza_toppings: # for loop, start
    if topping == 'Pepperoni': # conditional, if
        continue #for loop, continue
    print('After 1st if statement')  # log statement 
    if topping == 'Olives': # conditional, if
        break #for loop, break

def print_hello_ten_times(): # function,
    for num in range(10): # for loop, start
        print('Hello') # log statement 

print_hello_ten_times() # log statement 

def print_hello_x_times(x): # function,
    for num in range(x): # for loop, start
        print('Hello') # log statement 

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # function,
    for num in range(x):  # for loop, start
        print('Hello') # log statement 

print_hello_x_or_ten_times() # log statement 
print_hello_x_or_ten_times(4) # log statement 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)