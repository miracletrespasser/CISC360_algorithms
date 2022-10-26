'''
Function island_hopping(List c):
    ListofTuple mindistancetable
    Integer n = length of c
    fill mindistancetable with n+1 empty tuple
    mindistancetable[0]=(0,'0')
    mindistancetable[1]=(c[0],'0-1')
    Integer d=1
    Integer x,y
    Do{
        Increment d
        String k =concatenate('-',IntegertoString(d))
        x=c[d-2]+mindistancetable[d-2][0]
        y=c[d-1]+mindistancetable[d-1][0]
        if x <=y:
            mindistancetable[d][1]= concatenate(mindistancetable[d-2][0],k)
            mindistancetable[d][0]=x
        else:
            mindistancetable[d][1]=concatenate(mindistancetable[d-1][0],k)
            mindistancetable[d][0]=y
    }while (d<n)
    return mindistance[n]
'''
'''
Complexity is O(n),every step in the loop takes constant time and the loop takes linear time to loop through the list c0
For steps outside the loop, "fill mindistancetable with n+1 empty tuple" may take O(n) time but the others take constant time
Thus the algorithm is T(n)=O(n)+O(n)+O(1),we have the overall complexity O(n)
'''
def island_hopping(c):
    mindistancetable=[]
    n=len(c)
    #initilize for basecase0 :stay at c0, basecase 1: go from c
    mindistancetable.append((0,'0'))
    mindistancetable.append((c[0],'0-1'))
    for i in range(2,n+1):
        k='-'+str(i)
        x=c[i-2]+mindistancetable[i-2][0]
        y=c[i-1]+mindistancetable[i-1][0]
        #compare adn get the minimum distance to travel from c0 to ci
        if x<=y:
            mindistancetable.append((x,mindistancetable[i-2][1]+k))
        else:
            mindistancetable.append((y,mindistancetable[i-1][1]+k))
    return mindistancetable[n]
    