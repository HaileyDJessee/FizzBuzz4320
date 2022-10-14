for fizzbuzz in range(1,101):

 #takes the numbers that are multiples of 3 and 5
    
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")

#takes the numbers that are multiples of 3 
    
    elif fizzbuzz % 3 == 0:
        print("fizz")
        
#takes the numbers that are multiples of 3 

    elif fizzbuzz % 5 == 0:
        print("buzz")

    print(fizzbuzz)
