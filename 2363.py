class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = {}
        
        # Iterate over items1 and add them to the items dictionary
        for item in items1:
            if item[0] in items:
                items[item[0]] += item[1]
            else:
                items[item[0]] = item[1]
        
        # Iterate over items2 and add them to the items dictionary
        for item in items2:
            if item[0] in items:
                items[item[0]] += item[1]
            else:
                items[item[0]] = item[1]
        
        # Convert the items dictionary to a list of lists and sort it by value
        ret = [[k, v] for k, v in items.items()]
        ret.sort()
        
        return ret
