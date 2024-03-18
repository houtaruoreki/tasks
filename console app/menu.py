import sys
from diarybook import DiaryBook
import utils
from usermanager import UserManager


class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()
        self.usermanager = UserManager()
        self.logged_in = False
        self.current_user = None
        self.path = "data.json"

        self.choices = {
            "1": self.show_all_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.sort_memos,
            "5": self.populate_db,
            "6": self.print_username,
            "7": self.quit,
        }

        self.auth_choices = {
            "1": self.login_user,
            "2": self.register_user,
            "3": self.quit,
        }

    def print_username(self):
        print(self.current_user)

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.usermanager.registerUser(username, password):
            utils.insert_diary_into_json(self.path, username, password)
            self.logged_in = True
            self.current_user = username

    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.usermanager.loginUser(username, password):
            self.logged_in = True
        else:
            print("username or password is incorrect \n")

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("0 diaries")
        for diary in self.diarybook.diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        memo = input("enter a memo: ")
        tags = input("enter a tags: ")
        self.diarybook.new_diary(memo, tags)

        data = []
        for diary in self.diarybook.diaries:
            data.append({"memo": diary.memo, "tags": diary.tags})

        utils.insert_diary_into_json(
            self.path, self.current_user, diaries=self.diarybook.diaries
        )
        print("Diary entry added successfully.\n")

    def search_diaries(self):
        keyword = input("enter keyword: ")
        diaries, n = self.diarybook.search_diary(keyword)
        if n == 0:
            print("0 match found")
        else:
            print(f"{n} match found\n")
            for diary in diaries:
                print(f"{diary.id}-{diary.memo}")

    def sort_memos(self):
        lst = self.diarybook.diaries

        if len(lst) != 0:
            for i in range(0, len(lst)):
                for j in range(i + 1, len(lst)):
                    if lst[i].id >= lst[j].id:
                        lst[i].id, lst[j].id = lst[j].id, lst[i].id
        print(f"{lst.id} - {lst.memo}")

    def populate_db(self):
        try:
            data = utils.read_from_json_into_app(self.path)
            if not data:
                raise FileExistsError

            for username, info in data.items():  # Iterate over each user
                diaries = info.get('diaries', [])  # Retrieve diaries or an empty list if not present
                self.usermanager.add_new_user(username, info['password'])  # Add user
                for diary in diaries:  # Iterate over each diary for the current user
                    self.diarybook.new_diary(memo=diary['memo'], tags=diary['tags'])  # Add diary to diarybook

        except FileExistsError:
            print("data does not exists")

    def quit(self):
        sys.exit(0)

    @staticmethod
    def display_menu():

        print(
            """Diarybook Menu:

1. Show diaries
2. Add diary
3. Filter using keyword
4. Sort memos by id
5. Populate database
6. Current User
7. Quit program
    \n"""
        )

    @staticmethod
    def display_auth_menu():
        print(
            """
Authentication Menu:
                
1. Login
2. Register
3. Quit program
\n"""
        )

    def run(self):
        self.populate_db()
        while True:

            menu = self.display_menu if self.logged_in else self.display_auth_menu
            menu()
            choice = input("Enter an option: ")

            action_dict = self.choices if self.logged_in else self.auth_choices
            action = action_dict.get(choice)

            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")


if __name__ == "__main__":
    Menu().run()
