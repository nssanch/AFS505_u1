'''
EX 40 Modules, Classes, and Objects
Natalie Sanchez
2-16-21
'''

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)
        print('')

    def count_lines(self):
        i = 0
        for line in self.lyrics:
            i += 1
        return i

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
bulls = Song(["They rally around the family",
                "With pockets full of shells"])

starship = Song(["SN8 flew up into the blue sky",
                "and came crashing down with flames of green",
                "SN9 also went up high",
                "But couldn't get over its lean"])

print(happy_bday.count_lines())
happy_bday.sing()

bull_lines = bulls.count_lines()
print(bull_lines)
bulls.sing()

starship.sing()
