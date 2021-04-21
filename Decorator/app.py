def argument_test_natural_number(f):
    def helper(x):
        if type ( x ) == int and x > 0:
            return f ( x )
        else:
            raise Exception ( "Argument is not an integer" )

    return helper


@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial ( n - 1 )


print ( factorial ( 2 ) )
