from sys import argv
from manager import Manager, FileManager, Account

manager = Manager()
my_account = Account()
file_manager = FileManager()


@manager.assign("konto")
def balance_update(account):
    for line in file_manager.data:
        command = line.split(" ")
        if command[0] == "saldo":
            account.balance += int(command[1])
    print("Stan konta: {}".format(account.balance))


file_manager.open_file()
manager.execute("konto", my_account)
