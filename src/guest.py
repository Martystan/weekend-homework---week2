





class Guest:
    def __init__(self, input_name, input_wallet, input_favourite_song):
        self.name = input_name
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def has_sufficient_funds(self, room):
        return self.wallet >= room.fee 
        
    def pays(self, room):
        self.wallet -= room.fee   

    def is_favourite_song_on_the_list(self,song):
        for item in song:
            if item.title == self.favourite_song:
                return "Whoo!"
        



    
