import os
from datetime import datetime

FILE_PATH="diary.txt"

def add_entry():
    try:
        entry=input("write a new diary entry:\n ")
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file=open(FILE_PATH,"a")
        file.write(timestamp +"\n"+ entry + "\n")
        print("Entry saved successfully!")
    
    except Exception as e:
        print(f"Error saving entry: {e}")


def view_entry():
    try:
        file=open(FILE_PATH)
        print("\n---Diary entries---\n")
        print(file.read())

    except Exception as e:
        print(f"Error reading entry: {e}")



add_entry()
view_entry()