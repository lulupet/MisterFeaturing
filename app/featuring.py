from collections import defaultdict 

from app import db

from .models import Artist, Song, ArtistSong


    #https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/

def featuring_in_list(l, a, b):
    return [a, b] in l or [b, a] in l


# Function to build the graph 
def build_graph():
    edges = []
    for song in Song.query.all():
        for artist_song_1 in ArtistSong.query(song==song):
            for artist_song_2 in ArtistSong.query(song==song):
                if not featuring_in_list(edges, artist_1.id, artist_2.id) and artist_1.id != artist_2.id:
                    edges.append([artist_1.id, artist_2.id])
    graph = defaultdict(list)
      
    # Loop to iterate over every edge of the graph 
    for edge in edges:
        a, b = edge[0], edge[1]
          
        # Creating the graph as adjacency list 
        graph[a].append(b)
        graph[b].append(a)
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
  
# Driver Code 
if __name__ == "__main__": 
      
    # Graph using dictionaries 
    graph = {'A': ['B', 'E', 'C'], 
            'B': ['A', 'D', 'E'], 
            'C': ['A', 'F', 'G'], 
            'D': ['B', 'E'], 
            'E': ['A', 'B', 'D'], 
            'F': ['C'], 
            'G': ['C']} 
      
    # Function Call 
    BFS_SP(graph, 'A', 'D') 



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
    BFS_SP(graph, artist_1.id, artist_2.id) 
    return 'ok'
