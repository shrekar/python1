def cast_vote(age):
    assert age >=18, f"age shouldnt be < 18,it was :{age}"
    print("thank you for voting...")
try:
    age = int(input("enter your age:"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print(f"you entered avalid age:{age}")
finally:
    print("end..")