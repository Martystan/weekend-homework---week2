import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song




class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Rachel Green", 20, "Copacabana")
        self.guest_2 = Guest("Monica Geller",15, "YMCA")
        self.guest_3 = Guest("Phoebe Buffay", 7, "Smelly cat")
        self.guest_4 = Guest("Ross Geller", 15, "Baby got back")
        self.guest_5 = Guest("Chandler Bing", 25, "Space oddity")
        self.guest_6 = Guest("Joey Tribbiani", 1, "The lion sleeps tonight")

        self.room = Room("Friends Karaoke", 5, 10)

        self.song_1 = Song("Copacabana")
        self.song_2 = Song("Delta dawn")
        self.song_3 = Song("Smelly cat")

       
    

    def test_guest_has_a_name(self):
        self.assertEqual("Rachel Green", self.guest_1.name)

    def test_guest_has_a_wallet(self):
        self.assertEqual(1, self.guest_6.wallet)

    def test_guest_can_pay(self):
        self.guest_1.pays(self.room)
        self.assertEqual(10.00, self.guest_1.wallet)

    # def test_if_favourite_song_on_the_list(self):
    #     self.room.song = [self.song_1,self.song_2,self.song_3]
    #     self.guest_1.is_favourite_song_on_the_list(self.room.song)
    #     # self.assertEqual("Whoo", self.guest_1.is_favourite_song_on_the_list(self.room.song))


    

    

    
    
