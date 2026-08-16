class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):

                # Don't use the same element twice
                if used[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                # Undo the choice
                path.pop()
                used[i] = False

        backtrack([])
        return result