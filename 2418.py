class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # create a dictionary to map names to their heights
        name_height_map = {}
        for i in range(len(names)):
            name_height_map[names[i]] = heights[i]

        # sort the names based on their heights in descending order
        sorted_names = sorted(name_height_map, key=name_height_map.get, reverse=True)

        return sorted_names
