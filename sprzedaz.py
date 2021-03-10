from sys import argv
from lib.accountant import manager, file_manager


update = argv[2:]
update.insert(0, "sprzedaz")


file_manager.open_file()
for change in update:
    file_manager.data.append(change)
file_manager.file_process(manager)
if manager.input_error:
    file_manager.data = file_manager.data[:-4]
print("stock: ", manager.stock)
print("balance after: ", manager.balance)
file_manager.save_data()

