import sqlite3
import Music

class DataBase:
    def __init__(self,database):
        self.connect = sqlite3.connect(database)
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS musics(name TEXT, artist TEXT,lyrics TEXT,release_date DATE)")
        self.connect.commit()        
    
    def add_music(self,music):
        self.cursor.execute("INSERT INTO musics VALUES (?,?,?,?)",(music.name,music.artist,music.lyrics,music.release_date))
        self.connect.commit()

    def update_music(self,music):
        self.cursor.execute("UPDATE musics SET artist=?, lyrics=?,release_date=?,WHERE name=?",(music.artist,music.lyrics,music.release_date,music.name))
        self.connect.commit()

    def delete_music(self,name_of_music):
        self.cursor.execute("DELETE FROM musics WHERE name=?",(name_of_music,))
        self.connect.commit()
    
    def display_musics(self):
        self.cursor.execute("SELECT * FROM musics")
        musics = self.cursor.fetchall()
        return musics
    
    
    
    
    
    
    pass