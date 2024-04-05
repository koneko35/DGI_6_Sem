# zadanie  1
# class Song:
#     def __init__(self, title, artist, release_year) -> None:
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#
#     def introduce(self):
#         print('Какая-то песня',self.title , 'Кто-то', self.artist, self.release_year)
#
# some_song = Song('Manabreak', 'ZXCursed', '2022')
# some_song.introduce()

# zadanie 2

# class Song:
#     def __init__(self, title, artist, release_year) -> None:
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#
#     def introduce(self):
#         print('Какая-то песня',self.title , 'Кто-то', self.artist, self.release_year)
#
#     def get_info(self):
#         info={"title" : self.title,
#         "artist" : self.artist,
#         "release_year" : self.release_year}
#         return info
# some_song = Song('Manabreak', 'ZXCursed', '2022')
# some_song.introduce()
# print(some_song.get_info())

# zadanie 3

class Song:
    def __init__(self, title, artist, release_year) -> None:
        self.title = title
        self.artist = artist
        self.release_year = release_year

    def introduce(self):
        print('Какая-то песня',self.title , 'Кто-то', self.artist, self.release_year)

    def __str__(self):
        string_info = self.title, self.artist, self.release_year
        return string_info

some_song = Song('Manabreak', 'ZXCursed', '2022')
print(some_song)