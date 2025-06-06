class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment total song count
        Song.count += 1
        
        # Track genres and their count
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0
        Song.genre_count[genre] += 1
        
        # Track artists and their count
        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0
        Song.artist_count[artist] += 1

    @classmethod
    def genres(cls):
        # Return the keys of genre_count as a list
        return list(cls.genre_count.keys())

    @classmethod
    def artists(cls):
        # Return the keys of artist_count as a list
        return list(cls.artist_count.keys())
