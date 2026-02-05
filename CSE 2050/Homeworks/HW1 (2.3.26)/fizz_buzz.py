def fizz_buzz(start, finish):
    
    # Loop through every number from start to finish (inclusive)
    for i in range(start, finish + 1):
        
        """
        Convert i to a string so we can check if it contains '3' or '5'
        """ 
        s = str(i)
        
        # Check both conditions for 3 and 5 at the same time
        has_3 = (i % 3 == 0) or ('3' in s)
        has_5 = (i % 5 == 0) or ('5' in s)

        # Logic for printing based on what we found
        if has_3 and has_5:
            print("fizzbuzz")
        elif has_3:
            print("fizz")
        elif has_5:
            print("buzz")
        else:
            print(i)

fizz_buzz(1, 15)