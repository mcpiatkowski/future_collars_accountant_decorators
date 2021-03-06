from sys import argv
from manager import Manager, FileManager

manager = Manager()
file_manager = FileManager()


@manager.assign("saldo", 2)
def balance_update(manager, amount, comment):
    if manager.balance + amount >= 0:
        file_manager.data.append("saldo {} {}".format(amount, comment))


print("balance: ", manager.balance)
print(manager.actions)
print(file_manager.file_path)
file_manager.open_file()
print(file_manager.data)
""" file_manager.open_file()
manager.execute("saldo", manager)
file_manager.save_data()
 """