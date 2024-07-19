class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False
        #create two maps
        first = {}
        second = {}

        for letter in s:
            first[letter] = 1 + first.get(letter, 0)
            second[letter] = 1 + second.get(letter, 0)
        print(first)
        print(second)
        
        if first == second:
            
            return True
       
        else:
            
            return False

    isAnagram(None, 'Hello1', 'Hello')
        

                
