
def override(method):
    def wrapper(cls):
        if not any(method.__name__ in base.__dict__ for base in cls.__bases__):
            raise TypeError(
                f"El método '{method.__name__}' no sobrescribe ningún método en las clases base de '{cls.__name__}'."
            )
        return method
    return wrapper