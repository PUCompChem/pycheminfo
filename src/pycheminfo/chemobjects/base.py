from pydantic import BaseModel

class Atom(BaseModel):
    symbol: str = "C"
    charge: int = 0
    