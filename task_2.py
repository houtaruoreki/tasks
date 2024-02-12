def return_min(dictionary):
    minimal = dictionary[list(dictionary.keys())[0]]
    for key in dictionary:
        value = dictionary[key]
        if value<minimal:
            minimal = value
    return minimal


def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return n

#1
d = {"1": 2,
     "sadsa": -234,
     "2": 4,
     "3": 67}
print(return_min(d))

#2
print(factorial(6))