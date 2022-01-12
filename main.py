def plus(a, b):
    return (float(a)+float(b))

def minus(a, b):
    return (float(a)-float(b))
    
def div(a, b):
    return (float(a)/float(b))

def times(a, b):
    return (float(a)*float(b))

def negate(a):
    if a.isdecimal():
        a = float(a)
        return -a
    else:
        return "Please enter a number."

def pow(a, b):
    return (float(a)**float(b))

def remainder(a, b):
    return (float(a) % float(b))

a = input("First number:")
b = input("Second number:")
print(plus(a, b))
print(minus(a, b))
print(div(a, b))
print(times(a, b))
print(negate(a))
print(pow(a, b))
print(remainder(a, b))
    