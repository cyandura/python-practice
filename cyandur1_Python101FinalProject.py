#Python 101 Final Project by Cody Yandura

masterList = []

#Command Functions
def printErrorMessage():
    print("\nCommand not recognized\n")

def add(item):
    masterList.append(item)
    print("\n{} added to the list!\n".format(item))

def printList():
    print()
    if len(masterList) == 0:
        print("List is Empty!\n")
        return
    for i in range(len(masterList)):
        print("{}. {}".format(i+1, masterList[i]))
    print()

def deleteAt(index):
    if indexCheck(index):
        masterList.pop(index)
        print("\nDeleted index {} from the list!\n".format(index))

def clear():
    masterList.clear()
    print("\nList cleared\n")

def addAt(index, item):
    masterList.insert(index, item)
    print("\nInserted {} at index {}!\n".format(item, index))

def delete(item):
    for i in range(masterList.count(item)):
        masterList.remove(item)
    print("\nDeleted all instances of {} from the list!\n".format(item))

def modify(index, item):
    if indexCheck(index):
        masterList[index] = item
        print("\nModified list index {}\n".format(index))

def export():
    with open('output.txt', 'w') as f:
        for i in range(len(masterList)):
            f.write("{}. {}\n".format(i+1, masterList[i]))

#Utility functions
def cmdCheck(cmd, l):
    if len(command) < l:
        print("\nMissing command arguments\n")
        return False
    if len(command) > l:
        print("\nExtraneous command parameters were ignored.")
    return True

def indexCheck(index):
    if index > len(masterList) - 1 or index < 0:
        print("\nIndex not recognized\n")
        return False
    return True

#Main Functions
def getCommand():
    
    command = input("Enter a command: ")
    command = command.lower().strip().split()

    while len(command) == 0:
        print("\nNo command entered, type exit to stop program\n")
        command = input("Enter a command: ")
        command = command.lower().strip().split()
        
    return command

if __name__ == '__main__':

    print("This code belongs to: Cody\n")

    # Main project functionality goes here!
    command = [" "]
    while command[0] != "exit":
        command = getCommand()
        if command[0] == "print":
            printList()
        elif command[0] == "clear":
            clear()
        elif command[0] == "export":
            export()
        elif command[0] == "add":
            if cmdCheck(command,2):
                add(str(command[1]))
        elif command[0] == "addat":
            if cmdCheck(command,3):
                addAt(int(command[1]), str(command[2]))
        elif command[0] == "modify":
            if cmdCheck(command,3):
                modify(int(command[1]), str(command[2]))
        elif command[0] == "delete":
            if cmdCheck(command,2):
                delete(str(command[1]))
        elif command[0] == "deleteat":
            if cmdCheck(command,2):
                deleteAt(int(command[1]))
        elif command[0] == "exit":
            print("\nExit command entered. Exiting...")
            break
        else:
            printErrorMessage()
        
    