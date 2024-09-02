class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_rev = x_str[::-1]

        return x_rev == x_str
    

'''
This is in O(n) time, where the original integer is 
converted to a string, and using the [::-1] method to 
reverse the string. If they are equal, "==", then the 
bool will be set to true. Otherwise, it will return False.
'''