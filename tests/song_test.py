import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Copacabana")
        self.song_2 = Song("Delta dawn")
        self.song_3 = Song("Smelly cat")

    def test_song_has_title(self):
        self.assertEqual("Copacabana", self.song_1.title)