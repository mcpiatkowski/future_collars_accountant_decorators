from sys import argv
from lib.accountant import manager, file_manager


file_manager.open_file()
file_manager.file_process(manager)
print("Stan konta: ", manager.balance)