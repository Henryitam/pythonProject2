def fun(**kwargs):
    for m,bal in kwargs.items():
        print(f"{m}={bal}")

fun(name="bassy",age="12",sex="male")

# In Python, *args and **kwargs are used to allow functions to accept an
# arbitrary number of arguments. These features provide great flexibility when designing
# functions that need to handle a varying number of inputs.

#                ARGS
# multiplying multiple numbers using the arg functions

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result


print(multiply_numbers(2,3,4,5))
