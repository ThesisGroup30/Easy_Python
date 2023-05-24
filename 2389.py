class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort the input array in non-decreasing order
        nums.sort()

        # Initialize an array to store the maximum size of a subsequence
        # for each query
        answer = [0] * len(queries)

        # Iterate over each query and find the maximum size of a subsequence
        # that has a sum less than or equal to the corresponding query value
        for i, q in enumerate(queries):
            # Initialize the sum and count variables
            s = 0
            cnt = 0

            # Iterate over the input array from left to right and add each element
            # to the sum until the sum is greater than the query value
            for j in range(len(nums)):
                s += nums[j]
                if s > q:
                    break
                cnt += 1

            # Store the maximum size of a subsequence for the current query
            answer[i] = cnt

        return answer
