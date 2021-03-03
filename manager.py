from sys import argv


class Manager:
    def __init__(self):
        self.actions = {}

    def assign(self, action):
        def decorate(callback):
            self.actions[action] = callback
        return decorate

    def execute(self, action, *args, **kwargs):
        if action not in self.actions:
            print("Error")
        else:
            self.actions[action](*args, **kwargs)


class FileManager:
    def __init__(self):
        self.data = []
        self.file_path = argv[1]

    def open_file(self):
        with open(self.file_path) as fp:
            for line in fp:
                self.data.append(line.strip())

    def save_data(self):
        with open(self.file_path, 'w') as fp:
            for line in self.data:
                fp.write(line + "\n")


class Account:
    def __init__(self):
        self.balance = 0


class Warehouse():
    def __init__(self):
        self.stock = {}


    def open_stock(self, data):
        for line in data:
            command = line.split(" ")
            action = command[0]
            product = command[1]
            if action == "zakup":
                quantity = int(command[3])
                if product not in self.stock:
                    self.stock[product] = quantity
                else:
                    self.stock[product] += quantity
            if action == "sprzedaz":
                quantity = int(command[3])
                if product not in self.stock:
                    print("Brak produktu w magazynie")
                else:
                    self.stock[product] -= quantity
