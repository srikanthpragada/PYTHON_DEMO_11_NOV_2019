def print_details(*values, **details):
    print(values)
    for t in details.items():
        print(t)


print_details(10, 20, 30, a=10, b=20, c='Abc')
