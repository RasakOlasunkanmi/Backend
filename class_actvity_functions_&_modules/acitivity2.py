# Acitivity 2: Function with parameter
# Task: create a function called table_of(number) that prints the multiplication of any number passed as a parameter.

def table_of(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
        
if __name__ == "__main__":
    table_of(2)
    