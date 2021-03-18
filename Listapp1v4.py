
import random
MyList = []

def MainProgram():
    while True:
        try:
            print("HELLO. me ugg. me make list")
            print("type number to choose from optios below and me do that")
            choice = input("""1. add to list.
2.return the value index position.
3.random search
4.add a lot of intergers
5.print the list
6.Exit program""")
            if choice  == "1":
                AddToList()
            elif choice == "2":
                IndexValues()
            elif choice == "3":
                RandomSearch()
            elif choice == "69":
                print("nice")
            elif choice == "4":
                AddABnuch()
            elif choice == "5":
                Print()
            else:
                break
        except:
            print("You make error. Ugg can not understand error.")
# to add: 1 a way to loop action. 2 a way to quit. 3 think of repition
def AddToList():
    print("add item to list. yes. me do that!")
    NewItem = input("type an interger here")
    MyList.append(int(NewItem))

def AddABunch():
    print("u want add many interger. me can do that")
    NumToAdd = input("how many thing u want add    ")
    NumRange = input(" how high yoy wabt number to go?    ")
    for x in range(0, int(NumToAdd)):
        MyList.append(random.randit(0,int(NumRange)))
    print("Ugg has finished list")

def Print():
    print(MyList)

def IndexValues():
    print("OOOOUUAAAAGGGGHH. I hear you need certian peice of data.")
    indexPos = input ("ugg must know position of data")
    print(MyList[int(indexPos)])

def RandomSearch():
    print("ugg will random choose item")
    print(MyList[random.randit(0, len(MyList))-1])

def LinearSearch():
    print("Ugg will check every item on list for you. Ugg hate checking every item. every. item.   ")
    SearchItem = input = ("what you look for?    ")
    for x in range(len(MyList)):
        if MyList[x] == int(SearchItem):
            print("your item is at index position {}".format(x))

    
if __name__ == '__main__':
    MainProgram()
