
import random
MyList = []
NewList = []

def MainProgram():
    while True:
        try:
            print("HELLO. me ugg. me make list")
            print("type number to choose from optios below and me do that")
            choice = input("""1. add to list.
2.return the value index position.
3.random search
4.add a lot of intergers
5.print the lists
6.linear search
7.clear the lsit
8. sort list
9.Exit program    """)
            if choice  == "1":
                AddToList()
            elif choice == "2":
                IndexValues()
            elif choice == "3":
                RandomSearch()
            elif choice == "4":
                AddABunch()
            elif choice == "5":
                Print()
            elif choice == "6":
                LinearSearch()
            #add some random easter eggs cuz why not
            elif choice == "69":
                print("nice")
            elif choice == "42":
                print("why does he like this number?")
            elif choice == "17":
                print("why such a random number? ugg no understand")
            elif choice == "7":
                ClearList()
            elif choice == "8":
                SortList(MyList)
            else:
                break
        except:
            print("You make error. Ugg can not understand error.")

def AddToList():
    print("add item to list. yes. me do that!")
    NewItem = input("type an interger here")
    MyList.append(int(NewItem))

def AddABunch():
    print("u want add many interger. me can do that")
    NumToAdd = input("how many thing u want add    ")
    NumRange = input(" how high you want number to go?    ")
    for x in range(0, int(NumToAdd)):
        MyList.append(random.randint(0,int(NumRange)))
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
    SearchItem = input("what you look for?    ")
    for x in range(len(MyList)):
        if MyList[x] == int(SearchItem):
            print("your item is at index position {}".format(x))
#clear list thing i made
def ClearList():
    MyList.clear()
    NewList.clear()
    print("Ugg has cleared the list")

def SortList(MyList):
    print("you want sorted list. Ugg go do that")
    for x in MyList:
        if x not in NewList:
            NewList.append(x)
    NewList.sort()
    ShowMe = input =("You want me to show new new list")
    if ShowMe.lower() == "y":
        print(NewList)

def PrintLists
    if len(NewList) == 0:
        print (MyList)
    else:
        WhichOne = input(" would you like the sorted list or unssorted list?   ")
        if WhichOne.lowerc == "sorted":
            print(NewList)
        else:
            print(MyList)

    
if __name__ == '__main__':
    MainProgram()
