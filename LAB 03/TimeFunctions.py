import time # 🙂 Importing the built-in time module so we can track seconds

def time_function(func, args, n_trials=10): # 🙂 Added the arguments and the n_trials parameter, defaulting to 10
    """Takes a function and its single argument, returning the lowest time out of n_trials.""" # 🙂 Added the required docstring
    best_time = float('inf') # 🙂 Setting the starting lowest time to infinity so any real time will easily beat it
    for _ in range(n_trials): # 🙂 Looping exactly n_trials times to run multiple tests
        start = time.time() # 🙂 Grabbing the exact current time before the function runs
        func(args) # 🙂 Running the function that was passed in, using its single argument
        end = time.time() # 🙂 Grabbing the exact current time right after it finishes
        elapsed = end - start # 🙂 Subtracting start from end to find out how many seconds it took
        if elapsed < best_time: # 🙂 Checking if this specific run was faster than our previous best record
            best_time = elapsed # 🙂 If it was faster, we save this new elapsed time as the best_time
    return best_time # 🙂 Giving back the absolute fastest time after all trials are finished

def time_function_flexible(f, args, n_trials=10): # 🙂 Creating the flexible version expecting a tuple for args
    """Takes a function and a tuple of arguments, unpacking them to find the min execution time.""" # 🙂 Added the required docstring
    best_time = float('inf') # 🙂 Starting the best time at infinity again
    for _ in range(n_trials): # 🙂 Looping n_trials times for multiple tests
        start = time.time() # 🙂 Noting the start time
        f(*args) # 🙂 The * magically "unpacks" the tuple into separate arguments so the function f can read them
        end = time.time() # 🙂 Noting the end time
        elapsed = end - start # 🙂 Calculating how long it took
        if elapsed < best_time: # 🙂 Checking for a new speed record
            best_time = elapsed # 🙂 Updating the speed record if we found one
    return best_time # 🙂 Returning the lowest recorded time

if __name__ == '__main__': # ❤️ Checking if this Python file is being run directly (and not imported by another file)
    # ❤️ Some tests to see if time_function works
    def test_func(L): # ❤️ Defining a simple test function that takes a list called L
        for item in L: # ❤️ Going through every single item inside the list L
            item *= 2 # ❤️ Multiplying the current item by 2

    L1 = [i for i in range(10**5)] # ❤️ Using a list comprehension to quickly create a list of 100,000 numbers
    t1 = time_function(test_func, L1) # ❤️ Calling our new time_function to time test_func using L1, saving the result as t1

    L2 = [i for i in range(10**6)] # ❤️ Making a list 10x bigger (1,000,000 numbers)
    t2 = time_function(test_func, L2) # ❤️ Calling time_function again for the bigger list to see the speed difference

    print("t(L1) = {:.3g} ms".format(t1*1000)) # ❤️ Converting t1 to milliseconds by multiplying by 1000, formatting to 3 sig figs, and printing
    print("t(L2) = {:.3g} ms".format(t2*1000)) # ❤️ Converting t2 to milliseconds by multiplying by 1000, formatting to 3 sig figs, and printing