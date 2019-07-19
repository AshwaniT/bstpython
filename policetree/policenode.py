from filecmp import cmp


class PoliceNode:
    def __init__(self, policeId, fineAmt):
        self.left = None
        self.right = None
        self.policeId = policeId
        self.fineAmt = float(fineAmt)

    def __str__(self):
        if self is None:
            return 'empty'
        else:
            return 'PoliceId: %s, Fine: %s'%(self.policeId,self.fineAmt)


