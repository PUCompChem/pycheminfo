from pydantic import BaseModel


class ChemObjectModel(BaseModel):
    pass


class Atom(ChemObjectModel):
    symbol: str = "C"
    charge: int = 0
    

class Bond(ChemObjectModel):
    atom1 : Atom = None
    atom2 : Atom = None
    order : int = 1
    pass

