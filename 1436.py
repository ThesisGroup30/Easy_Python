class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegree = {}
        indegree = {}
        
        # Counting in and out degrees of each city
        for path in paths:
            outdegree[path[0]] = outdegree.get(path[0], 0) + 1
            indegree[path[1]] = indegree.get(path[1], 0) + 1
        
        # Finding the destination city with 0 outdegree
        for city in indegree.keys():
            if city not in outdegree:
                return city
