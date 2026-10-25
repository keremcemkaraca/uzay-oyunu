import time
from functools import wraps

def sure_olc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        print(f"{func.__name__}: {bitis - baslangic:.4f} sn")
        return sonuc
    return wrapper
