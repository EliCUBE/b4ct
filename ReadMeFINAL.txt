To use the program type of the valid responses from the printed list. choosing an invalad response
will promt you to close the program. once you select an action the program will ask for an input 
which you then give.
	The binary search works by checking every interger in the list to check if it is the interger
being searched for which is why it is called a binary search, it either returns a yes or no
value when checking an interger. the recursive search uses the sorted list //2 to find a mid point. 
it then sees if the mid piont is the interger being searched for. if it is it returns that integer
if it is between the loest value and the mid piont it makes the mid the new high and find mid agian.
if x is not in mid and low it makes mid the new low. it then calls itself in to repeat this until x is found.
the interitive search does the same thing but uses a loop to perform the functions instead of
calling itself in.
	the peice of custom code i wrote is
def ExitProgram():
    Exit = input("do you want to exit the program y/n?   ")
    if Exit.lower() == "y":
        quit()
this function is called whenever the user does an action that would normaly close the program. when it is c
called it asks the user for an input. of that input is y it closes the program. if it isnt it goes
back to the main program.