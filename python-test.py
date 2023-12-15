print ("This is a tttsting code to check error catching")

def simple_fn(range, seed):
    if range >= 0 and seed == 1:
        for i in range(range):
            print("Hi!")
    else:
        prnt("Zro entered, aborting")
        
if __name__ == "__main__":
    simple_fn(10)