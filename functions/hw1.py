custom_power = lambda x, e=1: x ** e

print(custom_power(3))

def custom_equation(x: int = 0, y: int = 0, a: int = 1, b: int = 1, c: int = 1): 
    result = (x ** a + y ** b) / c
    return float(result)

print(custom_equation(2, 5, 4, 5, 5))
"""
A function returns a tuple of an int and a dictionary
Function must count the number of calls with caller information
Returning integer is the total number of calls
Returning dictionary with string keys and integer values includes 
the caller ( _ _name_ _ ) as key, the number of call coming from 
this caller as value
"""
def fn_w_counter() -> (int, dict[str, int]):
    # Başlangıç değerlerini ayarla 
    if not hasattr(fn_w_counter, "call_count"):
        fn_w_counter.call_count = 0
    if not hasattr(fn_w_counter, "_dict"):
        fn_w_counter._dict = {}

    # Çağrayan fonksiyonun adını al 
    caller_name = __name__

    # Toplam çağrı sayısını artır
    fn_w_counter.call_count += 1

    # Çağrıları izlemek için sözlüğü güncelle
    if caller_name in fn_w_counter._dict:
        fn_w_counter._dict[caller_name] += 1
    else:
        fn_w_counter._dict[caller_name] = 1

    # Toplam çağrı sayısını ve çağrıları izleyen sözlüğü döndür
    return fn_w_counter.call_count, fn_w_counter._dict
