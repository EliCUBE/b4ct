def MainProgram():
    MyList = []
    print("Hello there! lets work with lists!")
    print("choose from one the the following options. Type a number below")
    choice = input("1. add to a list. 2.return the value at an index position.")
    if choice  == "1":
        AddToList()
    elif choice == "2":
        IndecValues()
# to add: 1 a way to loop action. 2 a way to quit. 3 think of repition
def AddToList():
    print("adding to a list, i love that!")
    NewItem = input("type and interger here")
    MyList.appened(int(NewItem))

def IndexValues():

if __name__ == '__main__':
    MainProgram()
