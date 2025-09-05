class Solution:
  def romanToInt(self, s:str) ->int:
    #map Roman values into integer value
    roman_map = {'I':1,'V':5,'X':10,'L':50,'c:100,'D'=500,'M':1000}
    result=0
    #iterate rgeough the string
    For i in range(len(s)):
      #if current value is less than next value subtract it 
            if i < len(s)-1 and roman_map[s[i]] < roman_map[s[i+1]]:
                result -= roman_map[s[i]]
            #otherwise add it
            else:
                result += roman_map[s[i]]

        return result






























                 
