# Fibonacci Sequence - Enter a number and have the program generate the 
# Fibonacci sequence to that number or to the Nth number.

def gen_fib():
    nterms = None

    # first two terms
    n1, n2 = 0, 1
    count = 0
    while type(nterms) != int:
        try:
            nterms = int(input("How many terms? "))
        except:
            print('Sorry, a bet must be a number!')
        else:
                if nterms <= 0:
                    print("Please enter a positive number")
                elif nterms == 1:
                    print("Fibonacci sequence upto",nterms,":")
                    print(n1)
                else:
                    print("Fibonacci sequence:")
                    while count < nterms:
                        print(n1)
                        nth = n1 + n2
                        # update values
                        n1 = n2
                        n2 = nth
                        count += 1
                gen_fib()



gen_fib()