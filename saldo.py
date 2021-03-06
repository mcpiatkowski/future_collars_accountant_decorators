from sys import argv
from manager import Manager, FileManager

manager = Manager()
file_manager = FileManager()
update = argv[2:]


@manager.assign("saldo", 2)
def balance_update(manager, amount, comment):
    if manager.balance + int(amount) >= 0:
        manager.balance += int(amount)


@manager.assign("zakup", 3)
def buy(manager, product_name, price, amount):
    if manager.balance - int(price)*int(amount) > 0:
        print("Zakup, price: {}, amount: {}".format(price, amount))
        manager.balance -= int(price)*int(amount)


@manager.assign("sprzedaz", 3)
def sell(manager, product_name, price, amount):
    print("Sprzedaz, price: {}, amount: {}".format(price, amount))
    manager.balance += int(price)*int(amount)


file_manager.open_file()
file_manager.file_process(manager)
print("balance after: ", manager.balance)
file_manager.data.append("saldo")
for change in update:
    file_manager.data.append(change)

print(file_manager.data)
