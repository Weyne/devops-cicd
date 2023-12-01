# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)
        else:
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"
    
class InvalidPermissions(Exception):
    pass

def validate_types(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Parameters must be numbers")
        return func(self, *args, **kwargs)
    return wrapper

def validate_permissions_user(func):
    def wrapper(self, x, y):
        if not validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        return func(self, x, y)
    return wrapper
