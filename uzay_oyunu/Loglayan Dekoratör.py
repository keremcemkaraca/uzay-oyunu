def log_cagri(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"-> {func.__name__}({all_args})")
        sonuc = func(*args, **kwargs)
        print(f"<<- {func.__name__} {sonuc!r}")
        return sonuc

    return wrapper
