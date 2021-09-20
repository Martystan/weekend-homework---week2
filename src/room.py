

class Room:
    def __init__(self, input_name, input_capacity, input_fee):
        self.name = input_name
        self.capacity = input_capacity
        self.fee = input_fee
        self.guest = []
        self.song = []
        self.queue = []

    def guest_count(self):
        return len(self.guest)

    def check_in_guest(self, guest):
        self.guest.append(guest)

    def check_out_guest(self, guest):
        self.guest.remove(guest)

    def add_song(self, song):
        self.song.append(song)

    def room_capacity(self):
        return self.capacity
    
    def guests_queue(self):
        return len(self.queue)

    def add_to_queue(self, guest):
        self.queue.append(guest)

    def remove_from_queue(self, guest):
        self.queue.remove(guest)

    def guest_can_enter(self, guest):
        self.add_to_queue(guest)
        if self.guests_queue() <= self.capacity:
            self.remove_from_queue(guest)
            self.check_in_guest(guest)

    
        
        




    

        


