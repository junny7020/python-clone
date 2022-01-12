def plus(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a)+float(b))
    else:
        return "Please enter numbers."

def minus(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a)-float(b))
    else:
        return "Please enter numbers."

def div(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a)/float(b))
    else:
        return "Please enter numbers."

def times(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a)*float(b))
    else:
        return "Please enter numbers."

def negate(a):
    if a.isdecimal():
        a = float(a)
        return -a
    else:
        return "Please enter a number."

def pow(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a)**float(b))
    else:
        return "Please enter numbers."

def remainder(a, b):
    if a.isdecimal() and b.isdecimal():
        return (float(a) % float(b))
    else:
        return "Please enter numbers."

a = input("First number:")
b = input("Second number:")
print(plus(a, b))
print(minus(a, b))
print(div(a, b))
print(times(a, b))
print(negate(a))
print(pow(a, b))
print(remainder(a, b))