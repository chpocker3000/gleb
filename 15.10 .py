def quarter_of(month):
    # your code here
    return (month + 2) // 3

def greet(name, owner):
    # Add code here
    return 'Hello boss' if name == owner else 'Hello guest'

def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    return length * width * height

def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

def string_to_number(s):
    # your code here
    return int(s)

def get_middle(s):
    return s[len(s)//2] if len(s) % 2 != 0 else s[len(s)//2-1:len(s)//2+1]

def sum_mix(arr):
    #your code here
    return sum([int(n) for n in arr])
