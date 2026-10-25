def say(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.cagri += 1
        return func(*args, **kwargs)
    wrapper.cagri = 0
    return wrapper