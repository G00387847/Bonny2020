# Bonny Chimezie Nwosu

# Python program function that takes 
# positive floating-point number as input
# and outputs an approx. of its square root
# Using Newton square root method.

def newton_sq_rt(root_of):

# Start with initial guess of half the input value
    apxroot = root_of/2
    num1 = 0
    while abs(root_of - apxroot**2) > 0.01:
        
        apxroot  = (apxroot + root_of/apxroot)/2
        num1 += 1
    return apxroot

def get_input():
    root_of = float(input("Please enter a positive number: "))
    try:
        float(root_of)
    except:
        print("Non-numeric input.".format(end=''))
        return get_input()
    if float(root_of) < 0:
        print("Positive number; result type 'positive'.")
        return abs(float(root_of)), True
    return float(root_of), False

root_of, positive = get_input()
if positive:
    print("The square root of  {} is approx.  {}.j".format(root_of, round(newton_sq_rt(root_of),1)))
else:
    print("The square root of {} is approx.  {}.".format(root_of, round(newton_sq_rt(root_of),1)))
 


   