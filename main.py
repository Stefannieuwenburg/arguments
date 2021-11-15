# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# part 1:
def greet(name:str, greeting:str = 'Hello, <name>!'):
    return greeting.replace('<name>', name)

greet('Bob')
print(greet('Bob', "What's up, <name>!"))
greet('Stefan')
print(greet('Stefan', "What's up, <name>!"))

# part 2: 

def force(mass:float, body:str = 'earth'):
    gravitylist = dict([
        ('sun', 274),
        ('jupiter',  24.9),
        ('neptune',  11.2),
        ('saturn',  10.4),
        ('earth', 9.8),
        ('uranus', 8.9),
        ('venus', 8.9),
        ('mars', 3.7),
        ('mercury', 3.7),
        ('moon', 1.6),
        ('pluto', 0.6)
    ])
    return (mass * gravitylist[body])


force(18.2)

# part 3

G = 6.674 * (10**-11)

def pull(m1:float, m2:float, d:float):
    return (G * (m1 * m2) / (d**2))
    


pull(100,200,0.5)
