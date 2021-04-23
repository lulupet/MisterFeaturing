from collections import defaultdict

from .models import Song, ArtistSong


def featuring_in_list(elements_list, a, b):
    return [a, b] in elements_list or [b, a] in elements_list


def build_graph():
    edges = []
    for song in Song.objects.all():
        for artist_song_1 in ArtistSong.objects.filter(song_id=song.id):
            for artist_song_2 in ArtistSong.objects.filter(song_id=song.id):
                if (not featuring_in_list(edges, artist_song_1.artist_id, artist_song_2.artist_id) and
                        artist_song_1.artist_id != artist_song_2.artist_id):
                    edges.append([artist_song_1.artist_id, artist_song_2.artist_id])
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph


def find_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        return 'same artists'
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.append(node)
    return 'no existing path'


def get_common_song(artist_1, artist_2):
    for song_artist_1 in ArtistSong.objects.filter(artist=artist_1):
        for song_artist_2 in ArtistSong.objects.filter(artist=artist_2):
            if song_artist_1.song == song_artist_2.song:
                return song_artist_1.song.name


def get_detailed_path(path):
    detailed_path = []
    for i in range(len(path) - 1):
        artist_1 = int(path[i])
        artist_2 = int(path[i + 1])
        detailed_path.append({
            'artist_1': artist_1.name,
            'song': get_common_song(artist_1, artist_2),
            'artist_2': artist_2.name
        })
    return detailed_path
