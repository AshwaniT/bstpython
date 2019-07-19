import os, sys, inspect
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
cmd_folder.replace(r"\trafficsystem","")
try:
    sys.path.index(cmd_folder.replace(r"\trafficsystem",""))  # Or os.getcwd() for this directory
except ValueError:
    sys.path.append(cmd_folder.replace(r"\trafficsystem",""))  # Or os.getcwd() for this directory
#print(sys.path)

from trafficfinesystem import TrafficFineSystem


def printMenu():
    print("*****availale options*****")
    print("1. Exit")
    print("2. Read From inputPS3.txt")
    print("3. printBonusPolicemen")
    print("4. Print Violators")
    print("5. reorderByFineAmount  >> run this only after 3 , bcz as it deletes element for reordering")
    print("6. Initialize Hash")
    print("7. Destroy Police Tree")
    print("8. Debug>>print Driver Hash On Console")
    print("9. Debug>>print Inorder PoliceTree On Console")


def main():
    print("Edit inputPS3.txt to update Violator or run with default data.")
    processor = TrafficFineSystem()
    while True:
        printMenu();
        try:
            userChoice = int(input("enter your choice :- "))
            if userChoice == 1:
                break
            elif userChoice == 2:
                parsedData = processor.fileReader();
                processor.processFileData(parsedData)
            elif userChoice == 3:
                processor.printBonusPolicemen(processor.policeIdBasedTree.root)
            elif userChoice == 4:
                processor.printViolators()
            elif userChoice == 5:
                orderByFineAmount = processor.reorderByFineAmount(processor.policeIdBasedTree.root)
                processor.printPoliceTree(orderByFineAmount)
            elif userChoice == 6:
                processor.initializeHash()
            elif userChoice == 7:
                processor.destroyPoliceTree(processor.policeIdBasedTree.root)
            elif userChoice == 8:
                processor.printDriverHashOnConsole()
            elif userChoice == 9:
                processor.printPoliceTree(processor.policeIdBasedTree.root)
            print("**Done**")
        except:
            print("pl enter valid input.")


if __name__ == '__main__':
    main()
