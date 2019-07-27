try:
    with open("data.txt") as f:
        lines = f.readlines()
        for line in lines :

            print(line,end="")

except Exception as e:
    print(f"file is not found check path {e}")