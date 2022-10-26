'''
Q1
Function Findsingle(String A):
    // this is used when f is in the right substring
    //and a pair of characters were cut in the middle when the string is splitted
    Integer cutcount=0
    If there is only one chracter in the string:
        return 0
    midpoint =length of A divided by 2
    equally Partition String A into String B,String C from the midpoint
    If notequal(last character in StringB,first character in StringC):
        if either B or C only have one element:
            return 0
        if last two characters of StringB is not equal:
            return midpoint
        else if first two characters of StringC is not equal:
            return midpoint+1
    else:
        delete the last Character in StringB
        delete the first Character in StringC
        cutcount=2
    If length of StringB is not divisible by 2:
        return Findsingle(String B)
    else if length of StringC is not divisible by 2:
        return lengthof(StringB)-1 + cutcount+ Findsingle(String C)
    else:
        return None
'''
'''
Q2
The best case is it find the single character around the middle point or the length of two strings are equal, 
the complexity at the best case is Omega(1),since the algorithm can solve in constant time.
The worst case is it finds the single character at the start or end of String,at this time
T(1)=c1
T(n)=T(n/2)+c2
we can write T(n)=(c2)log(n)+c1
thus the time complexity is O(log(n))
'''
def find_single(A):
    cutcount=0
    #if this is the only element found
    if len(A)==1:
        return 0
    #find the mid point
    midpoint=len(A)//2;
    #divide the string into two substrings
    B=A[0:midpoint]
    C=A[midpoint:]
    if B[-1]!= C[0]:
        #if the one of the substring is a single character
        if len(B)==1 or len(C)==1:
            return 0;
        #if on either substring there is a element doesn't match its neighbour
        if B[-1]!=B[-2]:
            return midpoint-1
        elif C[0]!=C[1]:
            return midpoint
    else:
        B=B[0:-1]                                                                                                                                                                                    
        C=C[1:]
        #because we eliminated a pair of characters, we need to add this number on 
        #if the target character is at the right half substring
        cutcount=2
    #if the length of substring is an odd number, then the single character must in this substring
    if len(B)%2 == 1:
        return find_single(B);
    elif len(C)%2 == 1:
        return len(B)+cutcount+find_single(C)
    #if the lengths of both substring are even number, then there is no single character
    else:
        return None