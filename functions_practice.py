# Function to print a greeting
def hello():
    print("Hello! Nice to meet you.")

# Function that packs three arguments into a list
def pack(a, b, c):
    return [a, b, c]

# Function to simulate eating lunch from a list of items
def eat_lunch(my_lunch):
    if not my_lunch:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {my_lunch[0]}")
        for item in my_lunch[1:]:
            print(f"Next I eat {item}")

# Test the functions
hello()
print(pack("sandwich", "apple", "cookie"))
eat_lunch(["sandwich", "apple", "cookie"])
eat_lunch([])
