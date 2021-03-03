from sys import argv
from manager import Manager, FileManager, Account, Warehouse

manager = Manager()
my_account = Account()
file_manager = FileManager()
warehouse = Warehouse()
file_path = argv[1]


@manager.assign("magazyn")
def print_stock(warehouse, file_manager):
    warehouse.open_stock(file_manager.data)


file_manager.open_file()
manager.execute("magazyn", warehouse, file_manager)
for product in warehouse.stock.items():
    print("{}: {}".format(product[0], product[1]))