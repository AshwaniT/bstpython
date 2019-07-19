class PoliceNodeCompare:
    def compare(self,nodeone,nodesecond):
        if nodeone.policeId < nodesecond.policeId:
            return -1
        elif nodeone.policeId>nodesecond.policeId:
            return 1
        else:
            return 0

