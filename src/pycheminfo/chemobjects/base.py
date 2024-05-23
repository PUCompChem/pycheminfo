from pydantic import BaseModel
from typing import List

class ChemObjectModel(BaseModel):
    pass


class Atom(ChemObjectModel):
    symbol: str = "C"
    charge: int = 0
    hCount: int = 0

    def __str__(self):
        return self.symbol


class Bond(ChemObjectModel):
    atom1 : Atom = None
    atom2 : Atom = None
    order : int = 1

    def __str__(self):
        s = (str(self.atom1) if self.atom1 else "None")
        s += " " + (self.atom2.__str__() if self.atom2 else "None")
        s += " " + str(self.order)
        return s


class ConTable(ChemObjectModel):
    atoms: List[Atom] = []
    bonds: List[Bond] = []
