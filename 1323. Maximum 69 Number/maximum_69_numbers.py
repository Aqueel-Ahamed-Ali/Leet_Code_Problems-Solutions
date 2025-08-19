class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert number to string for digit manipulation
        num_str = str(num)
        # Convert string to list to allow modification
        num_list = list(num_str)
        
        # Find the first '6' and change it to '9'
        for i in range(len(num_list)):
            if num_list[i] == '6':
                num_list[i] = '9'
                break  # Only change the first '6'
        
        # Convert back to integer and return
        return int(''.join(num_list))
