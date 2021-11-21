class supplier():
    level = 1

class distributor():
    level = 1

class shop_warehouse(supplier, distributor):
    level = 2

class shop_dispatch(shop_warehouse):
    level = 3

class shelf(shop_dispatch, distributor):
    level = 3

print(shelf.level)

