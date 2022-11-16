import pytest
def divide(a,b):
    print("divide method")
    if b!=0:
        div=a/b
    assert b!=0,"test passed"
    return div

print(divide(4,2))