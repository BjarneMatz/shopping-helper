#JSON Datenbank zum Speichern der Daten

import json

PATH = "./data/"

class Database:
    def __init__(self, dbname:str) -> None:
        
        self.db = dbname
        
        # Wenn die Datenbank nicht existiert, wird sie erstellt
        try:
            self.load()
        except FileNotFoundError:
            self.data = {}
            self.save()
    
    
    def load(self):
        with open(f"{PATH}{self.db}.json", "r") as file_data:
            self.data = json.load(file_data)

    def save(self):
        with open(f"{PATH}{self.db}.json", "w") as file_data:
            json.dump(self.data, file_data, indent=4)

    def get(self, key):
        return self.data[key]
    
    def set(self, key, value):
        self.data[key] = value
    
    def delete(self, key):
        del self.data[key]
    
    def exists(self, key):
        return key in self.data
    