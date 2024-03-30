import copy

def Initialize(arr):
    return set(arr)

def Find(valset, val):
    return valset.find(val)

def Merge(valset, val1, val2):
    valset.merge(val1, val2)

class set:
    def __init__(self, arr):
        self.values = copy.deepcopy(arr)
        self.parent = copy.deepcopy(arr)
        self.size = [1] * (len(arr))

    def indexOf(self, val):
        return self.values.index(val)

    def member(self, val):
        for i in range(0, len(self.values)):
            if val == self.values[i]:
                return True
        return False

    def find(self, val):
        if self.member(val):
            i = self.indexOf(val)
            if self.parent[i] == val:
                return val
            else:
                ancestor = self.find(self.parent[i])
                self.parent[i] = ancestor
                return ancestor
        else:
            return val
    
    def merge(self, a, b):
        iParentA = self.indexOf(self.find(a))
        iParentB = self.indexOf(self.find(b))
        if iParentA == iParentB:
            return
        else:
            if self.size[iParentA] >= self.size[iParentB]:
                self.parent[iParentB] = self.values[iParentA]
                self.size[iParentA] += self.size[iParentB]
            else:
                self.parent[iParentA] = self.values[iParentB]
                self.size[iParentB] += self.size[iParentA]
        