class PoliceNodeAmtCompare:
    def compare(self, nodeone, nodesecond):
        if nodeone.fineAmt < nodesecond.fineAmt:
            return -1
        elif nodeone.fineAmt > nodesecond.fineAmt:
            return 1
        else:
            return -1 # if amount is equal then it should go to left side
