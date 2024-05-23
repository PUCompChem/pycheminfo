import sys  
sys.path.append("./src/")
sys.path.append("../src/")

from pycheminfo.chemobjects.base import *

a1 = Atom(symbol = "C")
a2 = Atom(symbol = "N")
print(a1)
print(a2)

b = Bond(atom1 = a1)
print(b)