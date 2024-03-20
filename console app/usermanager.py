class User:
    last_id = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.last_id += 1


class UserManager:
    def __init__(self):
        self.users = {}

    def add_new_user(self, username, password):
        self.users[username] = User(username, password)

    def search_user(self, username):
        return username in self.users

    def check_password(self, username, password):
        user = self.users[username]
        return user.password == password

    def loginUser(self, username, password):
        return self.search_user(username) and self.check_password(username, password)

    def registerUser(self, username, password):
        if username not in self.users:
            self.add_new_user(username, password)
            return True
        else:
            return False
