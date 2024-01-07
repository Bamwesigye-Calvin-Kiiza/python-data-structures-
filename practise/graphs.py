class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)
        
    def get_paths(self,start,end,path =[]):
            path.append(start)
            
            if start == end:
                return [path]
            
            if start not in self.graph_dict:
                return []
            
            paths = []
            for node in self.graph_dict[start]:
                if node not in path:
                    new_paths = self.get_paths(node,end,path)
                
                    for pathh in new_paths:
                        paths.append(pathh)
            return paths      
    def shortest_path(self,start,end,path=[]):
        path.append(start)
        
        if start == end:
            return path
        if start not in self.graph_dict:
            return f'{start} not in the graph cities'
        
        shortest_path = None
        
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp
                        
        return shortest_path
        
if __name__ == '__main__':
    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
            ]
    
    graph = Graph(routes)
    start = "Mumbai"
    end = "Bangaluru"

    print(f"All paths between: {start} and {end}: ",graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", graph.shortest_path(start,end))

    