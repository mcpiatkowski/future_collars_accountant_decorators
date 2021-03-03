from sys import argv
from manager import Manager, FileManager, Account
manager = Manager()
my_account = Account()
file_manager = FileManager()
file_path = argv[1]


@manager.assign("zakup")
def buy(file_manager):
    file_manager.data.append("zakup {} {} {}".format(
        argv[2], 
        argv[3], 
        argv[4],
        ))


file_manager.open_file()
manager.execute("zakup", file_manager)
file_manager.save_data()