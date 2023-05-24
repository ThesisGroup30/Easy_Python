class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create two dictionaries to store the frequency of numbers in nums1 and nums2
        freq1 = {}
        freq2 = {}
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
        for num in nums2:
            freq2[num] = freq2.get(num, 0) + 1
        
        # Create a list to store the intersection
        intersection = []
        
        # Iterate through the keys of freq1 and check if they are also in freq2
        for num in freq1.keys():
            if num in freq2:
                # Append the number to the intersection list the minimum number of times it appears in both arrays
                intersection.extend([num]*min(freq1[num], freq2[num]))
        
        return intersection
