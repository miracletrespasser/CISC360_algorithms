'''
Function min_lamp(radius_list):
    list result
    List_of_list coverage_index
    List temp= radius_list
    Calculate the light coverage length in temp, store it back to temp
    pair the light coverage with the index of element in temp, store it in coverage_index
    sort coverage_index by the light coverage in descending order
    Current_lamp =0
    while not end of coverage_index or coverage_index[current_lamp].lightcoverage is not 0:
        if the street in the coverage of the current lamp is not all covered yet:
            add coverage_index[current_lamp].index into result
            mark all the lamps in the coverage of current lamp to true
        Increment current_lamp
    if not all lamps are covered
        return None
    else
        return result
'''
'''
caculate the coverage takes O(n)
pair the elements takes O(n)
sort takes O(nlog(n))
the loop takes O(n)
check through all lamps takes O(n)
T(n)=O(nlog(n))+O(n)+O(n)+O(n)+O(n)
the algorithm takes O(nlog(n))
'''
def min_lamp(r):
    result=[]
    coverage_index=[]
    radius_list=[]
    temp=r
    #calculate the coverage
    #the coverage of light near the edges may not be the diameter 
    for x in range(len(r)):
        temp[x]=min(x-0,temp[x])+min(len(r)-1-x,temp[x])
        coverage_index.append((temp[x],x))
        radius_list.append(False)
    #sort by light coverage range in descending order
    coverage_index.sort(reverse=True)
    Current_lamp =0
    while Current_lamp < len(r) and coverage_index[Current_lamp][0]!=0:
        #check if the street within the lamp's coverage is covered
        index=coverage_index[Current_lamp][1]
        leftcoverage= max(index-r[index],0)
        rightcoverage= min(index+r[index],len(r)-1)
        if not (radius_list[leftcoverage] and radius_list[rightcoverage]):
            result.append(index)
            #mark all lamps in coverage true
            #since the light coverage is a constant, the loop's complexity could be taken as constant time
            for x in range(leftcoverage,rightcoverage+1):
                radius_list[x]=True
        Current_lamp+=1
    #check if the street is covered
    for x in range(len(r)):
        #if not all covered ,return none
        if not radius_list[x]:
            return none
    return result