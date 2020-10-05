# Taking The Input From The User
nC = int(input("Enter The Number Which You Want To Check\n"))  

# Checks If nC Is A Prime Number  
def isPrime(nC):
    if nC > 1:  
        for i in range(2,nC):  
            if (nC % i) == 0:  
                print("%s is not a prime number"%nC)  
                break  
        else:  
            print(nC,"is a prime number")           
    else:  
        print(nC,"is not a prime number") 

# This algorithm has a time complexity of O(sqrt(n))
# It applies the concept that every Prime number can be represented in the form of 6k + 1 or 6k - 1 for k = [0,1,2,..] except 2 and 3.
def optimisedIsPrime(nC):
    if nC <= 1:
        return False
    if nC <= 3:
        return True

    if nC%2 == 0 or nC%3 == 0:
        return False

    i = 5
    while i*i <= nC:
        if nC%i == 0 or nC%(i+2) == 0:
            return False
        i += 6
    return True


# Driver
isPrime(nC)

prime = optimisedIsPrime(nC)
if prime:
    print("Optimised: {} is a prime number.".format(nC))
else:
    print("Optimised: {} is not a prime number.".format(nC))