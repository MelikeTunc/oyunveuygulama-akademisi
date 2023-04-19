"""


def least_difference(a, b, c):

    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)

    min(diff1,diff2,diff3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)
mystery = print()
print(mystery)

print(1,2,3,sep='<')

print(1,2,3)

def greet(who="Colin"):
    print("Hello",who)
greet()

greet(who="Kaggle")
greet("World")

def mult_by_five(x):
    return 5*x

def call(fn,arg):
    return fn(arg)

def squared_call(fn,arg):
    return fn(fn(arg))

print(
    call(mult_by_five,1),
    squared_call(mult_by_five,1),
    sep='\n'
)
def mod_5(x):
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)

def can_run_for_president(age):
    return age >= 35
print("Can a 19 years old run for president",can_run_for_president(19))
print("Can a 45 years old run for president",can_run_for_president(45))

def is_odd(n):
    return(n%2)==1
print("Is 100 odd",is_odd(100))
print("Is -1 odd",is_odd(-1))

def can_run_for_president( age, is_natural_born_citizen):
    return is_natural_born_citizen and (age>=35)

print(can_run_for_president(19,True))
print(can_run_for_president(55,False))
print(can_run_for_president(55,True))

def inspect(x):
    if x == 0:
        print(x,"is zero")
    elif x > 0:
        print(x,"is positive")
    elif x < 0:
        print(x,"is negative")
    else:
        print(x,"is unlike anything I've ever seen..")

def f(x):
    if x>0:
        print("Only printed when x is positive;x=",x)
        print("Also onlu printed when x is positive; x=",x)
    print("Always printed,regarless of x's value;x=",x)
f(1)
f(0)

print(bool(1))
print(bool(0))
print(bool("asf"))
print(bool(""))

if 0:
    print(0)
elif "spam":
    print("spam")
primes = [2,3,5,7]

planets =['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[0:4])

planets [3]= 'Melike'
print(planets)

len(planets)
print(len(planets))
print(sorted(planets))

primes =(2,3,5,7)
print(sum(primes))
print(max(primes))

x=12

print(x.imag)

c=12+3j
print(c.imag)

#print(x.bit_length())
#help(x.bit_length)

print (planets.append('Pluto'))
help(planets.append)
print(planets)

print(planets.pop())
print(planets)
print(planets.index('Earth'))

print("Earth" in planets)
print("CAN"in planets)

t=(1,2,3)

print(t)
x = 0.125
print(x.as_integer_ratio())
numerator,denominator =x.as_integer_ratio()
print(numerator/denominator)

a=1
b=0

a,b=b,a
print(a,b)

from ast import Mult


planets =['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

for planet in planets:
    print( planet , end=' ')

multiplicands = (2,2,2,3,3,5)
product=1
for mul in multiplicands:
    product = product * mul
print(product)
"""