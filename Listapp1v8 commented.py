
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
7.recursive search
8.Iteritive search
9.clear the lsit
10. sort list
11.Exit program    """)
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
                
            elif choice == "9":
                ClearList()
            elif choice == "10":
                SortList(MyList)
            elif choice == "7":
                SearchItem = input("what you look for?   ")
                RecursiveSearch(NewList, 0, len(NewList)-1,int(SearchItem))
            elif choice =="8":
                SearchItem = input("what you look for?   ")
                result = IterativeSearch(NewList, int(SeacrchItem))
                if result != -1:
                    print("your number is at is at index {}.".format(result))
                else:
                    print("ugg cannot find number. it is ot in list.")
            else:
                break
        except:
            print("You make error. Ugg can not understand error.")
''' This fuction asks the user for an input which is then appened ito the list'''
def AddToList():
    print("add item to list. yes. me do that!")
    NewItem = input("type an interger here")
    MyList.append(int(NewItem))

"""the functio asks the user fir 2 inputs. one input is used for a random interger generator. the second runs that geerator a certian amount of times. the last line appends all the intergers to the list"""
def AddABunch():
    print("u want add many interger. me can do that")
    NumToAdd = input("how many thing u want add    ")
    NumRange = input(" how high you want number to go?    ")
    for x in range(0, int(NumToAdd)):
        MyList.append(random.randint(0,int(NumRange)))
    print("Ugg has finished list")

def Print():
    print(MyList)
'''this function asks for a n inut which is the tured into an index positio -1 and then returns the value at that position.'''
def IndexValues():
    print("OOOOUUAAAAGGGGHH. I hear you need certian peice of data.")
    indexPos = input ("ugg must know position of data")
    print(MyList[int(indexPos)])

'''this functions geerates a number between 0 and the length of the list -1 ad returns the value at that idex positio'''
def RandomSearch():
    print("ugg will random choose item")
    print(MyList[random.randit(0, len(MyList))-1])
'''this function checks every value in the list to see if it equals the number the user is looking for'''
def LinearSearch():
    print("Ugg will check every item on list for you. Ugg hate checking every item. every. item.   ")
    SearchItem = input("what you look for?    ")
    for x in range(len(MyList)):
        if MyList[x] == int(SearchItem):
            print("your item is at index position {}".format(x))


'''this functions takes the high and sees if its higher than the low. if it is it devides the high and low by 2 and makes that vid. it then checks to see if the number the user is looking for is
equal to the mid if it is it prints that number. it then checks to see if x is higher than mid. if it is it takes mid + high ad devides by 2. it the runs itsef agian with the ew high low and mid.'''
def RecursiveSearch(NewList, low, high, x):
    if high >= low:"
        mid = (high + low) // 2
            
        if NewList[mid] == x:
            prit("ugg found number at indedx position {}".format(mid))
        elif NewList[mid] > x:
            return RecursiveSearch(NewList, low, high, mid - 1, x)
        else:
            return RecursiveSearch(NewList, low, high, mid +1, x)
        
    else:
        print("ugg can not find number. it gone")

def IterativeSearch(NewList, x):
    low = 0
    high = len(NewList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if NewList[mid] < x:
            low = mid + 1
        elif NewList[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


    
#clear list thing i made
'''this just clears both lists'''
def ClearList():
    MyList.clear()
    NewList.clear()
    print("Ugg has cleared the lists")

''''this list takes every uqnie value from the mai list and copies in into a new list that it then sorts. then it asks the user if they want to print it'''
def SortList(MyList):
    print("you want sorted list. Ugg go do that")
    for x in MyList:
        if x not in NewList:
            NewList.append(x)
    NewList.sort()
    ShowMe = input("You want me to show new new list y/n?    ")
    if ShowMe.lower() == "y":
        print(NewList)


'''this function asks the user for an input to see which list it should print. it then prits the selcted list.'''
def PrintLists():
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