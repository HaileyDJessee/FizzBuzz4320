for fizzbuzz in range(1,101):

    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")

    if fizzbuzz % 3 == 0:
        print("fizz")

    if fizzbuzz % 5 == 0:
        print("buzz")

    print(fizzbuzz)
