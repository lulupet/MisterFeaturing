from app import db


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return self.name


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)

    def __repr__(self):
        return self.id + ' - ' + self.name


class ArtistSong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(64), db.ForeignKey('artist.id'))
    song = db.Column(db.String(64), db.ForeignKey('song.id'))

    def __repr__(self):
        return self.song + ' - ' + self.artist
