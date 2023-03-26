from Music import Music
from DataBase import DataBase


def menu():
    
    print("1. Add music")
    print("2. Update music")
    print("3. Delete music")
    print("4. Display all musics")
    print("5. Quit")
    secim = input("Your choice:  ")
    return secim

def add_music(database):
    name = input("name: ")
    artist = input("artist: ")
    lyrics = input("lyrics: ")
    release_date = input("release date: ")
    
    music = Music(name,artist,lyrics,release_date)
    database.add_music(music)

def update_music(database):
    name = input("name: ")
    artist = input("artist: ")
    lyrics = input("lyrics: ")
    release_date = input("release date: ")

    music = Music(name,artist,lyrics,lyrics)
    database.update_music(music)

def delete_music(database):
    name =input()
    database.delete_music(name)

def display_musics(database):
    musics = database.display_musics()
    i = 0
    for music in musics:
        i = i + 1
        print(f"name: {music[0]}")
        print(f"artist: {music[1]}")
        print(f"lyrics: {music[2]}")
        print(f"release date: {music[3]}")
        print("\n")

def main():
    database = DataBase("database_music.db")

    while True:
        choice = menu()

        if choice == "1":
            add_music(database)
        elif choice == "2":
            update_music(database)
        elif choice == "3":
            delete_music(database)
        elif choice == "4":
            display_musics(database)
        elif choice == "5":
            print("bye :)")
            break
        else:
            print("please enter a valid number (1,2,3,4,5)")

main()