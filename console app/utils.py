from diarybook import Diary
import json

def read_from_json_into_app(path, *kwargs):
    with open(path, 'r') as file:
        data = json.load(file)
        if not kwargs:  
            return data
        username = kwargs[0]  
        user_data = data[0]["users"].get(username)
        if user_data:
            diaries_data = user_data.get("diaries", [])
            diaries = [Diary(entry["memo"], entry["tags"]) for entry in diaries_data]
            return diaries
        else:
            print("\nUser not found or has no diaries.\n")
            return None

            


def insert_diary_into_json(path, username, password=None, diaries=None):
    with open(path, 'r+') as file:
        data = json.load(file)
        users = data[0]["users"]
        
        if username in users:
            if diaries:
                for diary in diaries:
                    users[username]["diaries"].append({"memo": diary.memo, "tags": diary.tags})
                print("New user registered and diary inserted into JSON file.")
        else:
                print("New user registered. No diary inserted.")
        
        file.seek(0)
        json.dump(data, file, indent=4)

