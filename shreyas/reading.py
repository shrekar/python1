try:
    with open("data.txt") as fin ,open("u_data.txt","W") as fo:
        lines = fin.readlines()
        kines = [1.upper() for 1 in lines]
        fout.writelines(lines)
except Exception as e:
    print("file not fount plz check path {e}" )

    
