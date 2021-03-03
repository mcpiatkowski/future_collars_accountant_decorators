from sys import argv
from manager import Manager, FileManager, Account

manager = Manager()
my_account = Account()
file_manager = FileManager()
file_path = argv[1]


@manager.assign("saldo")
def balance_update(file_manager):
    file_manager.data.append("saldo {} {}".format(argv[2], argv[3]))


file_manager.open_file()
manager.execute("saldo", file_manager)
file_manager.save_data()