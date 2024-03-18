from diarybook import Diary
import json

def read_from_json_into_app(path):
    with open(path, 'r') as file:
        data = json.load(file)
        data = data[0]["users"]
        return data


            



def insert_diary_into_json(path, username, password=None, diaries=None):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = [{"users": {}}]

    users = data[0]["users"]
    
    if username in users:
        user = users[username]
        if diaries:
            user_diaries = user.get("diaries", [])
            user_diaries.extend(diaries)
            user["diaries"] = user_diaries
            print("Diaries inserted into existing user's record.\n")
    else:
        users[username] = {"password": password, "diaries": [] if not diaries else diaries}
        print("New user registered and diaries inserted into JSON file.\n")

    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

