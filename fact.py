class c1:
    def __init__(self):
        print("option1")
class c2:
    def __init__(self):
        print("option2")
class factory:
    def choose(options):
        if (options=="c"):
            return c1()
        elif(options=="d"):
            return c2()
object=factory.choose("d")