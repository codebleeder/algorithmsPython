assumptions: 
    string inputs are of same length.
    string inputs are limited to lower case alphabets. 

solution01CheckingOff:
    compares each letter in first string with each letter in second string.
    complexity = O(n^2)
    
solution02SortAndCompare:
    sorts the strings and then compares letter by letter. 
    complexity is either O(nlogn) or O(n^2) depending on the sort steps. 
    
solution03CountAndCompare:
    counts the alphabets in both strings, and compares. 
    complexity is O(n) 
    
