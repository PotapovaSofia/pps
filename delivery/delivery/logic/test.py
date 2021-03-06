from .graph import Graph
from .item import Item
from .order import Order, Criteria
from .oper import Operator
import sys
#from leg import Leg

g = Graph()
sys.exit(0)
items = [Item(1, 4, "chma", 15), Item(2, 5, "chma2", 10)]
for item in items:
    print(item)
order = Order(0, 0, items, None, 0, 2)
op = Operator()
route, _ = op.makeRoute(order, g)
assert route.getLegsIds() == [0, 1]

order2 = Order(0, 0, items, None, 0, 2, Criteria("cost"))
route2, _ = op.makeRoute(order2, g)
print(route2.getLegsIds())
assert route2.getLegsIds() == [2]
