class Violator:
    def __init__(self, licenseNum, fineAmt):
        self.licenseNum = licenseNum
        self.fineAmt = fineAmt
        self.violationCount = 1
    def getLicenseNum(self):
        return self.licenseNum
    def addFine(self, fineAmt):
        self.fineAmt += fineAmt
        self.violationCount+=1
    def getViolationCount(self):
        return self.violationCount;
    def getViolator(self):
        return (self.licenseNum, self.fineAmt)
    def __str__(self):
        return "license->"+str(self.licenseNum)+"/fine->"+str(self.fineAmt)+"/count->"+str(self.violationCount)
