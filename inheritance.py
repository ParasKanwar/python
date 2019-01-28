from abc import ABC, abstractclassmethod
from Hackerrank import leftRotation


class superset(ABC):
    Superset_cardinality = 0

    @abstractclassmethod
    def addElement(self, key, value):
        pass


class makeset(superset):
    Superset_cardinality = 0

    def addElement(self, key, value):
        self.set[key] = value
        self.Superset_cardinality = len(self.set)

    def __init__(self, set1):
        self.set = set1
        self.Superset_cardinality = len(set1)
    pass


o1 = makeset([1, 2, 3, 4])
print(o1.set)

# class animamal(superset):

set2 = makeset({" paras ": 2, " kanwar ": 3})
set2.addElement(key="karan", value=3)
print(set2.set)
print(set2.Superset_cardinality)
