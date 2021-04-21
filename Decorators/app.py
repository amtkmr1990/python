from functools import wraps
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


def decorator_wrapper(level):
    def check_permission(func):
        @wraps(func)
        def function_wrapper():
            if user['role'] == level:
                func()
            else:
                raise PermissionError('You do not have permission')
        return function_wrapper
    return check_permission

@decorator_wrapper('admin')
def delete_database():
    # perform deletion
    print('Database deleted!')

delete_database()
