class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name}-{self.duration}'

    def __lt__(self, other):
        return self.duration < other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __ge__(self, other):
        return self.duration >= other.duration


class Album:
    def __init__(self, band_name, album_name):
        self.band_name = band_name
        self.album_name = album_name
        self.tracks = []

    def __str__(self):
        result = ''
        for track in self.tracks:
            result += ('\n\t\t' + str(track))
        return f'Name Group: \"{self.band_name}\" \nName Album: \"{self.album_name}\" \nTracks: {result}'

    def get_duration(self):
        result = 0
        for track in self.tracks:
            result += track.duration
        return result

    def add_track(self, name, duration):
        self.tracks.append(Track(name, duration))


album1 = Album('Metallica', 'Load')
album2 = Album('Metallica', 'Reload')

album1.add_track('Ain\'t My Bitch', 5)
album1.add_track('Until it sleeps', 4)
album1.add_track('Hero of the day', 4)

album2.add_track('Better than you', 5)
album2.add_track('Fuel', 4)
album2.add_track('Prince Charming', 6)

print(album1)
print(album2)

print(album1.tracks[0] > album2.tracks[2])
