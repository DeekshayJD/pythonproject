# OrderedDict example
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print("OrderedDict:", list(od.items()))

# Regular dictionary example (Python 3.7+)
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
print("Regular Dict:", list(d.items()))
