def raise_exception():
    
    me = "my" * "me"

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")