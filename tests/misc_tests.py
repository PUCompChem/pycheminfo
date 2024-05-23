import sys  
sys.path.append("./src/")
sys.path.append("../src/")

from pycheminfo.chemobjects.base import *

a = Atom(symbol = "N")
print(a)