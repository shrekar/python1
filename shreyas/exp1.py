try:
    num = 100 /0
except ZeroDivisionError as e:
    print("except block")
    print(f"{e}")
finally:
    print("final block")