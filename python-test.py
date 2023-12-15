print ("This is a tttsting code to check error catching")

def simple_fn(range):
    if range > 0:
        for i in range(range):
            print("Hi!")
    else:
        prnt("Negative number entered, aborting")
        
if __name__ == "__main__":
    simple_fn(10)