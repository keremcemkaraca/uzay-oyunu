def sinirla(alt, ust):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                deger = args[0]
                if not (alt <= deger <= ust):
                    raise ValueError(f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil")
            return func(*args, **kwargs)
        return wrapper
    return decorator