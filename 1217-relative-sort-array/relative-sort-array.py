class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the elements of arr2 and their indices
        arr2_dict = {num: i for i, num in enumerate(arr2)}
        
        # Sort the elements of arr1 that are in arr2 based on their order in arr2
        sorted_arr1 = sorted(
            [num for num in arr1 if num in arr2_dict],
            key=lambda x: arr2_dict[x]
        )
        
        # Sort the elements of arr1 that are not in arr2 in ascending order
        sorted_remaining = sorted([num for num in arr1 if num not in arr2_dict])
        
        # Combine the two sorted lists
        result = sorted_arr1 + sorted_remaining
        
        return result