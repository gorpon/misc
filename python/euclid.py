
def is_prime(a):
    return all(a % i for i in range(2, a))


def number_check(num):
    """
    validate a number is whole and greater than zero
    """
    if not isinstance(num, int):
        print("num %s is not an integer" % str(num))
        return False
    elif num <= 0:
        print("num %s is not greater than zero" % str(num))
        return False
    elif is_prime(num):
        print("%s is a prime number!" % str(num))
    else:
        return True


def get_numbers():
    """
    input two different whole numbers, sort and return
    """
    print("please enter two different, whole, non-prime numbers")
    num1 = int(input("enter first number: "))
    if not number_check(num1):
        get_numbers()
    num2 = int(input("enter second number: "))
    if not number_check(num2):
        get_numbers()

    if num1 > num2:
        return num1, num2
    elif num2 > num1:
        return num2, num1
    else:
        print("I didn't like your answers. try again.") 
        get_numbers()


def get_gcd(x, y):
    """
    given larger and smaller number
    :param x: the bigger of the two numbers
    :param y: the lesser of the two numbers
    :return gcd: the greated common denominator of the two numbers
    """
    if x % y == 0:
        return y
    
    temp_x = x
    while (temp_x - y) > 0:
        temp_x -= y

    return get_gcd(y, temp_x) 
    

x, y = get_numbers()
print("the gcd is %s" % str(get_gcd(x, y)))

