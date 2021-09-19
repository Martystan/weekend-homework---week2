import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Friends Karaoke", 5, 10)

        self.guest_1 = Guest("Rachel Green", 20, "Copacabana")
        self.guest_2 = Guest("Monica Geller",15, "YMCA")
        self.guest_3 = Guest("Phoebe Buffay", 7, "Smelly cat")
        self.guest_4 = Guest("Ross Geller", 15, "Baby got back")
        self.guest_5 = Guest("Chandler Bing", 25, "Space oddity")
        self.guest_6 = Guest("Joey Tribbiani", 1, "The lion sleeps tonight")


        self.song_1 = Song("Copacabana")
        self.song_2 = Song("YMCA")
        self.song_3 = Song("Smelly cat")
        self.song_4 = Song("The lion sleeps tonight")
        self.song_5 = Song("Baby got back")
        self.song_5 = Song("Space oddity")

    def test_room_has_name(self):
        self.assertEqual("Friends Karaoke", self.room.name)
    
    def test_guest_added(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room.guest))

    def test_song_added(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, len(self.room.song))

    def test_guests_added_to_queue(self):
        self.room.add_to_queue(self.guest_1)
        self.assertEqual(1, len(self.room.queue))

    def test_guest_can_be_checked_in(self):
            self.room.guest_can_enter(self.guest_1)
            self.assertEqual(1, len(self.room.guest))
            self.assertEqual(0, len(self.room.queue))
        
    


    
        


    


    def test_room_has_capacity(self):
            self.assertEqual(5, self.room.capacity)
            
            

    
    

        



