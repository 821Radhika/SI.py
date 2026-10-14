
def simple_interest(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = int(input("Enter the principal amount: "))
    r = int(input("Enter the rate of interest: "))
    t = int(input("Enter the time in months: "))
    print("The simple interest is:", simple_interest(p, r, t))
