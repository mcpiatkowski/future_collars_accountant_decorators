from sys import argv
from lib.accountant import manager, file_manager

products_to_view = argv[2:]

file_manager.open_file()
file_manager.file_process(manager)
for product in products_to_view:
    print("{}: {}".format(product, manager.stock[product]))
