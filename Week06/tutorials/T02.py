class Song():
    # constructor
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # method/function
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# create a Song object lumberjack
lumberjack = Song(["I'm a lumberjack and I'm OK",
                   "I sleep all night",
                   "And I work all day"])

spam = Song(["SPAM, SPAM, SPAM, SPAM",
             "spam, spam, spam, spam"])

# activate the song object (sing_me_a_song)
lumberjack.sing_me_a_song()
spam.sing_me_a_song()
