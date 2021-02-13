from collections import defaultdict 

from app import db

from .models import Artist, Song, ArtistSong


def featuring_in_list(l, a, b):
    return [a, b] in l or [b, a] in l


# Function to build the graph 
def build_graph():
    edges = []
    for song in Song.query.all():
        for artist_song_1 in ArtistSong.query.filter(ArtistSong.song_id==song.id):
            for artist_song_2 in ArtistSong.query.filter(ArtistSong.song_id==song.id):
                if not featuring_in_list(edges, artist_song_1.artist_id, artist_song_2.artist_id) and artist_song_1.artist_id != artist_song_2.artist_id:
                    edges.append([artist_song_1.artist_id, artist_song_2.artist_id])
    graph = defaultdict(list)
      
    # Loop to iterate over every edge of the graph 
    for edge in edges:
        a, b = edge[0], edge[1]
          
        # Creating the graph as adjacency list 
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    return graph


# Python implementation to find the  
# shortest path in the graph using  
# dictionaries  
  
# Function to find the shortest 
# path between two nodes of a graph 
def BFS_SP(graph, start, goal): 
    explored = [] 
      
    # Queue for traversing the  
    # graph in the BFS 
    queue = [[start]] 
      
    # If the desired node is  
    # reached 
    if start == goal: 
        print("Same Node") 
        return
      
    # Loop to traverse the graph  
    # with the help of the queue 
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
          
        # Codition to check if the 
        # current node is not visited 
        if node not in explored: 
            neighbours = graph[node] 
              
            # Loop to iterate over the  
            # neighbours of the node 
            for neighbour in neighbours: 
                new_path = list(path) 
                new_path.append(neighbour) 
                queue.append(new_path) 
                  
                # Condition to check if the  
                # neighbour node is the goal 
                if neighbour == goal: 
                    print("Shortest path = ", *new_path) 
                    return
            explored.append(node) 
  
    # Condition when the nodes are not connected 
    print("So sorry, but a connecting path doesn't exist :(")

    return


def get_featuring(artist_1, artist_2):
    if Artist.query.filter_by(name=artist_1).count() != 0:
        artist_1 = db.session.query(Artist).filter_by(name=artist_1).first()
    else:
        return {"artist": "Name of artist 1 does not exist"}
    if Artist.query.filter_by(name=artist_2).count() != 0:
        artist_2 = db.session.query(Artist).filter_by(name=artist_2).first()
    else:
        return {"artist": "Name of artist 2 does not exist"}
    graph = build_graph()
    BFS_SP(graph, str(artist_1.id), str(artist_2.id)) 
    return 'ok'
