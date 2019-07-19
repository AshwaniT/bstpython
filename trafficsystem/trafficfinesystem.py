from fileio.filehelper import FileHelper
from policetree.policenodecomparer import PoliceNodeCompare
from policetree.PoliceNodeAmtComparer import PoliceNodeAmtCompare
from policetree.policenode import PoliceNode
from policetree.bst import PoliceTree
from violator import Violator


class TrafficFineSystem:
    def __init__(self):
        self.policeIdBasedTree = PoliceTree(PoliceNodeCompare())
        self.fineBasedTree = PoliceTree(PoliceNodeAmtCompare())
        self.size = 10
        self.driverHash = [None] * self.size

    def _hashCode_(self, licenseNum):
        return licenseNum % self.size

    def initializeHash(self):
        self.driverHash = [None] * self.size

    def insertHash(self, licenseNum, fineAmt):
        hashKey = self._hashCode_(licenseNum)
        if self.driverHash[hashKey] is None:
            self.driverHash[hashKey] = []
            self.driverHash[hashKey].append(Violator(licenseNum, fineAmt))
        else:
            violatorTuple = self._binarySearch_(self.driverHash[hashKey], licenseNum, 0, len(self.driverHash[hashKey]))
            if violatorTuple[0] is None:
                list.insert(self.driverHash[hashKey], violatorTuple[1], Violator(licenseNum, fineAmt))
            else:
                violatorTuple[0].addFine(fineAmt)

    def printViolators(self):
        file = None
        try:
            file = open("../violators.txt", "w")
            file.write("--------------Violators-------------\n")
            for drivers in self.driverHash:
                if drivers is None:
                    continue
                for driver in drivers:
                    if driver.getViolationCount() > 3:
                        file.write(str(driver.getLicenseNum()) + ", " + str(driver.getViolationCount()) + "\n")
        except Exception:
            print("error occured in writing file.")
        finally:
            if file is not None:
                file.close()

    def printDriverHashOnConsole(self):
        for i in range(0, len(self.driverHash)):
            if self.driverHash[i] is not None:
                print("hash::" + str(i) + "->", *self.driverHash[i], sep=", ")

    def insertByPoliceId(self, policeRoot, policeId, amount):
        newnode = PoliceNode(policeId, amount)
        self.policeIdBasedTree.insert(policeRoot.root, newnode)
        return self.policeIdBasedTree

    def reorderByFineAmount(self, policeRoot):
        self.fineBasedTree = PoliceTree(PoliceNodeAmtCompare())
        orderl = self.policeIdBasedTree.bsf()
        for x in orderl[::-1]:
            newnode = PoliceNode(x.policeId, x.fineAmt)
            self.fineBasedTree.insert(self.fineBasedTree.root, newnode)
            self.policeIdBasedTree.delete(self.policeIdBasedTree.root, newnode)
        return self.fineBasedTree.root

    def destroyPoliceTree(self, policeRoot):
        orderl = self.policeIdBasedTree.bsf()
        for x in orderl[::-1]:
            newnode = PoliceNode(x.policeId, x.fineAmt)
            self.policeIdBasedTree.delete(self.policeIdBasedTree.root, newnode)
        self.policeIdBasedTree = PoliceTree(PoliceNodeCompare())

    def printPoliceTree(self, policeRoot):
        self.policeIdBasedTree.inorderlist = []
        order = self.policeIdBasedTree.inOrder(policeRoot)
        for x in order:
            print(x)

    def printBonusPolicemen(self, policeRoot):
        self.policeIdBasedTree.inorderlist = []
        order = self.policeIdBasedTree.inOrder(self.policeIdBasedTree.root)
        max = self.policeIdBasedTree.max(self.policeIdBasedTree.root)
        bonus_files = list(filter(lambda x: float(x.fineAmt) > float(0.9) * float(max.fineAmt), order))
        with open(r'../bonus.txt', 'w+') as fh:
            fh.writelines('--------------Bonus-------------' + "\n")

            for x in bonus_files:
                fh.writelines("{0}\n".format('{},{}'.format(x.policeId, x.fineAmt)))
            fh.truncate()

    def _initializetree_(self):
        fh = FileHelper()
        res = fh.readLines(r"../inputPS3.txt")
        for x in res:
            tup = x.split(r'/')
            self.insertByPoliceId(self.policeIdBasedTree.root, tup[0].strip(), tup[2].strip())

    def processFileData(self, parsedData):
        for data in parsedData:
            self.insertHash(data[1], data[2])
            self.insertByPoliceId(self.policeIdBasedTree, data[0], data[2])

    def fileReader(self):
        parsedData = [];
        file = None
        try:
            file = open("../inputPS3.txt", "r")
            fileLines = file.readlines()
            for line in fileLines:
                token = line.split("/")
                parsedData.append((int(token[0].strip()), int(token[1].strip()), float(token[2].strip())))
        except Exception:
            print("error occured in reading file.")
        finally:
            if file is not None:
                file.close()
            return parsedData

    def _binarySearch_(self, objList, licenseNum, startIndex, endIndex):
        if len(objList) == 0:
            return (None, 0)
        midIndex = int((startIndex + endIndex) / 2)
        insertIndex = midIndex
        if objList[midIndex].licenseNum == licenseNum:
            return (objList[midIndex], midIndex)
        elif objList[midIndex].licenseNum > licenseNum:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
            insertIndex = startIndex;
        if startIndex > endIndex or startIndex >= len(objList):
            return (None, insertIndex)
        return self._binarySearch_(objList, licenseNum, startIndex, endIndex)
