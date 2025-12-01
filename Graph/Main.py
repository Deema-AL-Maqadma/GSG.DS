#============================================================
# Deema Mohammed AL-Maqadma
# Graph Assignment
# The Implementation
#============================================================
from Graph import Graph
# Create the city map
city_map = Graph()

# Add locations
city_map.add_vertex("Hospital")
city_map.add_vertex("School")
city_map.add_vertex("Store")
city_map.add_vertex("Park")
city_map.add_vertex("Mall")
city_map.add_vertex("Station")

# Add roads with travel times
city_map.add_edge("Hospital", "School", 5)
city_map.add_edge("School", "Store", 3)
city_map.add_edge("Store", "Mall", 4)
city_map.add_edge("Mall", "Park", 2)
city_map.add_edge("Park", "Station", 6)
city_map.add_edge("Station", "Hospital", 7)
city_map.add_edge("Hospital", "Mall", 10)
city_map.add_edge("School", "Park", 8)
city_map.add_edge("Store", "Station", 9)
city_map.add_edge("Mall", "School", 1)

#======================================================
# Usage
# Test BFS
print("---> Reachable locations from Hospital:")
print(city_map.bfs("Hospital"))

# Test Dijkstra
print("\n---> Shortest travel times from Hospital:")
shortest_paths = city_map.dijkstra("Hospital")
for location, time in shortest_paths.items():
    print(f"{location}: {time}")

print("\n ---> Thx ^_^ <---\n")
    
    