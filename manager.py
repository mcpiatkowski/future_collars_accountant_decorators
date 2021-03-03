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


class AccountManager(Manager):
    def __init__(self):
        self.balance = 0


