class song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
        list_lyrics = lyrics.split(',')
        self.list_lyrics = list_lyrics
    def sing_me_a_song(self):
        for line in self.list_lyrics:
            print(line)
x = input("pls type a happy bday song:\n")
happy_bday = song(x)
#bull_on_parade = song(["They rally around the family",
#                       "With pocket full of shells"])
import time
time.sleep(2)
happy_bday.sing_me_a_song()
#bull_on_parade.sing_me_a_song()
