import collections

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}


queue = []
visited = []
def bfs(visited,graph,src,dest):
    visited.append(src)
    queue.append(src);
    while queue:
        current = queue.pop(0)
        print(current,end=" ")
        if(current == dest):
          break
        for neighbour in graph[current]:
            if(neighbour not in visited):
                queue.append(neighbour)
                visited.append(neighbour)
            

print("Path from 5 to 4 = ",end="")
bfs(visited,graph,"5","4")
    
