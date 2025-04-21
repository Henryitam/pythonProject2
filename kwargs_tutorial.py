def fun(**kwargs):
    for m,bal in kwargs.items():
        print(f"{m}={bal}")

fun(name="bassy",age="12",sex="male")

# In Python, *args and **kwargs are used to allow functions to accept an
# arbitrary number of arguments. These features provide great flexibility when designing
# functions that need to handle a varying number of inputs.