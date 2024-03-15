import sys
from diarybook import DiaryBook
import utils


class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()   
        self.username = ''
        self.password = ''
        self.logged_in = False
        self.current_user = None
        self.path = 'data.json'

        self.choices = {
            "1": self.show_all_diaries,
            "2": self.add_diary,
            "3": self.search_diaries,
            "4": self.sort_memos,
            "5": self.populate_db,
            "6": self.quit
        }

        self.auth_choices = {
            "1": self.login_user,
            "2": self.register_user,
            "3": self.quit
        }
    def search_user(self, username, password):
        data = utils.read_from_json_into_app(self.path)
    
        for user_username, user_info in data[0]['users'].items():
            if username == user_username and password == user_info['password']:
                return True
        return False
       
                
    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        utils.insert_diary_into_json(self.path,username,password)
    def login_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if self.search_user(username,password):
            self.logged_in = True
            self.username = username
            self.password = password
        else:
            print("Username or password is not correct")
    def show_all_diaries(self):
        if len(self.diarybook.diaries)==0:
            print("0 diaries")
        for diary in self.diarybook.diaries:
            print(f"{diary.id}-{diary.memo}")

    def add_diary(self):
        memo = input("enter a memo: ")
        tags = input("enter a tags: ")
        self.diarybook.new_diary(memo,tags)

        data = []
        for diary in self.diarybook.diaries:
            data.append({"memo": diary.memo, "tags": diary.tags})

        utils.insert_diary_into_json(self.path, self.username,diaries=self.diarybook.diaries)
        print("Diary entry added successfully.")
        
    def search_diaries(self):
        keyword = input("enter keyword: ")
        diaries,n = self.diarybook.search_diary(keyword)
        if n == 0:
            print("\n0 match found")
        else: 
            print(f"\n{n} match found\n")
            for diary in diaries:
                print(f"{diary.id}-{diary.memo}")
    

    def sort_memos(self):
        lst = self.diarybook.diaries
        """
        აქ სორტის გამოყენებაც შეიძლებოდა მაგრამ ჩაშენებული ფუნქცია რადგანაც არ შეიძლება 
        ცოტა იმპროვიზაციას მივმართე
        """
         
        if len(lst) !=0:
            for i in range(0, len(lst)):
                for j in range(i+1, len(lst)):
                    if lst[i].id >= lst[j].id:
                        lst[i].id, lst[j].id = lst[j].id,lst[i].id
        print(f"{lst.id} - {lst.memo}")

        
    def populate_db(self):
        try:
            data = utils.read_from_json_into_app(self.path,self.username)
            if not data:
                raise FileExistsError
            for diary in data:
                self.diarybook.diaries.append(diary)
            print("diaries added to the database")
        except FileExistsError:
            pass
        
    def quit(self):
        sys.exit(0)

    def display_menu(self, *args):
        if len(args) == 0: 
            print(
"""Diarybook Menu:

1. Show diaries
2. Add diary
3. Filter using keyword
4. Sort memos by id
5. Populate database
6. Current User
7. Quit program
    \n""")
        else:
            print(
"""
Authentication Menu:
                
1. Login
2. Register
3. Quit program
\n""")
            
    def run(self):
        while True:
            if self.logged_in:
                self.display_menu()
                choise = input("enter an option: ")
                action = self.choices.get(choise)
                if action:
                    action()
                else:
                    print(f"{action} is not valid choice")
            else:
                self.display_menu("auth menu")
                choise = input("enter an option: ")
                action = self.auth_choices.get(choise)
                if action:
                    action()
                else:
                    print(f"{action} is not valid choice")
if __name__=="__main__":
    Menu().run()