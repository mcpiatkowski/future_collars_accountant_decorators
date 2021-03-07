from sys import argv
from lib.manager import Manager, FileManager

manager = Manager()
file_manager = FileManager()
update = argv[2:]
update.insert(0, "saldo")


@manager.assign("saldo", 2)
def balance_update(manager, amount, comment):
    if manager.balance + int(amount) >= 0:
        manager.balance += int(amount)


@manager.assign("zakup", 3)
def buy(manager, product_name, price, amount):
    if manager.balance - int(price)*int(amount) >= 0:
        manager.balance -= int(price)*int(amount)
        if product_name not in manager.stock:
            manager.stock[product_name] = int(amount)
        else:
            manager.stock[product_name] += int(amount)
    else:
        print("Brak wystarczającej ilość gotówki.")
        manager.input_error = True


@manager.assign("sprzedaz", 3)
def sell(manager, product_name, price, amount):
    if product_name not in manager.stock:
        print("Brak produktu w magazynie!")
    elif manager.stock[product_name] >= int(amount):
        manager.stock[product_name] -= int(amount)
        manager.balance += int(price)*int(amount)
    else:
        print("Brak wystrczającej ilości produktu w magazynie.")
        manager.input_error = True


file_manager.open_file()
for change in update:
    file_manager.data.append(change)
file_manager.file_process(manager)
print("balance after: ", manager.balance)
file_manager.save_data()

