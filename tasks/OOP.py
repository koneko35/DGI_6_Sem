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

# class Song:
#     def __init__(self, title, artist, release_year) -> None:
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#
#     def introduce(self):
#         print('Какая-то песня',self.title , 'Кто-то', self.artist, self.release_year)
#
#     def __str__(self):
#         string_info = str(self.__dict__)
#         return string_info
#
# some_song = Song('Manabreak', 'ZXCursed', '2022')
# print(some_song)

# zadanie 4
# class Podcast_Episode:
#     def __init__(self, title, artist, duration, guest):
#         self.title = title
#         self.artist = artist
#         self.guest = guest
#         self.o3m = self.co3m(duration)
#
#     def co3m(self, duration):
#         if duration >= 30:
#             return True
#
#     def __str__(self):
#         string_info = str(self.__dict__)
#         return string_info
#
#
# some_podcast = Podcast_Episode ('Какой-то подкаст', 'Кто-то', 123456, 'Кто-то другой')
# print(some_podcast)

# zadanie 5 6

class Audio_Item:
    def __init__(self,title, artist, is_liked=False):
        self.artist = artist
        self.title = title
        self.is_liked = is_liked
    def like(self):
        return not self.is_liked
    def __str__(self):
        string_info = str(self.__dict__)
        return string_info

class Song(Audio_Item):
        def __init__(self, title, artist, release_year):
            super().__init__(title, artist)
            self.release_year = release_year

class Podcast_Episode(Audio_Item):
    def __init__(self, title, artist, duration, guest):
        super().__init__(title, artist)
        self.duration = duration
        self.guest = guest
        self.o3m = self.co3m(duration)

    def co3m(self, duration):
        if duration >= 30:
            return True


some_song = Song('Manabreak', 'ZXCursed', '2022')
print(some_song)

some_podcast = Podcast_Episode ('Какой-то подкаст', 'Кто-то', 123456, 'Кто-то другой')
print(some_podcast)