
MyList = []

def MainProgram():
    while True:
        print("HELLO. me ugg. me make list")
        print("type number to choose from optios below and me do that")
        choice = input("""1. add to list.
    2.return the value index position.
    3.Exit program    """)
        if choice  == "1":
            AddToList()
        elif choice == "2":
            IndecValues()
            break
# to add: 1 a way to loop action. 2 a way to quit. 3 think of repition
def AddToList():
    print("add item to list. yes. me do that!")
    NewItem = input("type and interger here")
    MyList.appened(int(NewItem))

def IndexValues():

    print("OOOOUUAAAAGGGGHH. I hear you need certian peice of data.")
    indexPos = input ("ugg must know position of data")
    print (MyList[int(indexPos)])

if __name__ == '__main__':
    MainProgram()
