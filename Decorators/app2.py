from functools import wraps

user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


def check_permission(func):
    @wraps ( func )
    def function_wrapper():
        if user['role'] == 'admin':
            func ()
        else:
            raise PermissionError ( 'You do not have permission' )

    return function_wrapper


@check_permission
def delete_database():
    # perform deletion
    print ( 'Database deleted!' )


delete_database ()
