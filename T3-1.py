'''
Function platform_assignment(List trains)
    If trains is empty:
        return emptylist=[]
    Sort trains by the departure time in ascending order
    Integer Current_platform =0
    List platforms =[]
    append Current_platform to platforms
    Current_train=0
    while not at the end of trains:
        If trains[Current_train+1].starttime <= Current_time:
            If trains[Current_train+1].starttime <= the departure time of trains in the last occupied platform:
                open a new platform for the train
                Increment Current_train
            else
                Increment current_platform
                check if the next platform occupied is available
        else:
            Assign the train to the current_platform
            Current_platform=0
            Current_time = timelimit[0]
            Increment Current_train
    return platforms
'''
'''
sort the list takes O(nlog(n)) time complexity
the loop takes O(n) complexity on average cases
since there are k platforms maximum, checking through the platforms takes constant time complexity
T(n)=O(nlog(n))+O(n)=O(nlog(n))
thus the algorithm takes O(nlog(n))complexity
'''
def platform_assignment(trains):
    #base case for no trains 
    if len(trains)==0:
        return []
    #sort by departure time
    trains.sort(key=lambda x:x[1]);
    #initilize variables
    Current_train = 0
    Current_platform =0
    platforms =[]
    timelimit =[]
    #assign platform to the first train
    platforms.append(Current_platform)
    timelimit.append(trains[Current_train][1])
    Current_time=timelimit[0]
    #check through the list
    while Current_train+1 < len(trains):
        #if the current occupied platform is not available
        if trains[Current_train+1][0]<= Current_time:
            #check if any of the other occupied platform could be assigned
            if trains[Current_train+1][0] <= timelimit[-1]:
                platforms.append(Current_platform+1)
                timelimit.append(trains[Current_train][1])
                Current_platform=0
                Current_time=timelimit[0]
                Current_train+=1
            else:
            #check through the platforms and find a suitable platform to fit in
                Current_platform+=1
                Current_time=timelimit[Current_platform]
        else:
        #assign the occupied platform to the train
            platforms.append(Current_platform)
            timelimit[Current_platform]=trains[Current_train+1][1]
            current_platform=0
            Current_time = timelimit[0]
            Current_train+=1
    return platforms
   
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    