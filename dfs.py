import collections

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
stack = []



def dfs(graph,visited,src,dest):
  if(src not in visited):
    visited.append(src);
    
    print(src,end = " ")
  for neighbour in graph[src]:
    if(neighbour == dest):
      print(dest,end = " ")
      
      break;
    dfs(graph,visited,neighbour,dest)
  
  
  
  
  
print("Path from 5 to 8 = ",end="")  
dfs(graph,visited,"5","8")  
  
  
