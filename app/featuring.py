from app import db

from .models import Artist, Song, ArtistSong


def build_graph():
    #https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/

def get_featuring(artist_1, artist_2):
    if db.session.query(Artist).filter_by(name=artist_1).exists():
        artist_1 = db.session.query(Artist).filter_by(name=artist_1).first()
    else:
        return {"artist": "Name of artist 1 does not exist"}
    if db.session.query(Artist).filter_by(name=artist_2).exists():
        artist_2 = db.session.query(Artist).filter_by(name=artist_2).first()
    else:
        return {"artist": "Name of artist 2 does not exist"}
