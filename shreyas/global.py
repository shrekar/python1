class MaxLimitError(Exception):

    def __init__(self,message):
        self.message = message
    
    def __str__(self):
        return f"(self.__class__.__name__) : {self.emessage}""
        
c = 0
def Login(usernamer,password):
    global c
    if username == "abc" and password =="cha" :
        print("login is successfully")
        else:
            print("bad creditial")
        c +=1
        if c > 2: