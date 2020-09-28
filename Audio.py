class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        return f'<{self.name}--{self.duration}>'


class Album:
    def __init__(self, band_name, album_name):
        self.band_name = band_name
        self.album_name = album_name
        self.tracks = []

    def get_tracks(self):
        print(f'{self.album_name}: ')
        for track in self.tracks:
            print(track.show())

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

album1.get_tracks()

print(
    f'Длительность альбома \'{album1.album_name}\' группы \'{album1.band_name}\' '
    f'составляет {album1.get_duration()} минут.')

print(
    f'Длительность альбома \'{album2.album_name}\' группы \'{album2.band_name}\' '
    f'составляет {album2.get_duration()} минут.')
