#import min-heap module
import heapq
import math
import itertools

def job_assignment(cost_matrix):
    #initialize all variables
    min_heap=[]
    n=len(cost_matrix)
    full_part_solutions=0
    #compute a global upper bound use get_ffO(n^2)
    #store the index removed from the list
    upperbound=get_ffc(cost_matrix,[])
    #initialize the minimum heap O(n)
    for i in range(0,n):
        #start from assigning tasks to P1
        solution=[i]
        csf=get_csf(cost_matrix,solution)
        gfc=get_gfc(cost_matrix,solution)
        ffc=get_ffc(cost_matrix,solution)
        print("solution: "+str(i))
        print("csf: "+str(csf))
        print("gfc: "+str(gfc))
        print("ffc: "+str(ffc))
        min_heap.append([csf+gfc,csf+ffc,solution])
    #use heapq to construct the min-heap
    heapq.heapify(min_heap)
    #the B&B algorithm structure
    while(min_heap):
        full_part_solutions+=1
        partsolution=min_heap[0][2]
        num=len(partsolution)
        #if a complete solution
        if (num==n):
            return min_heap[0][0],list(min_heap[0][2]),full_part_solutions
        #else expand from the solution
        else:
            heapq.heappop(min_heap)
            temp=cost_matrix[num].copy()
            #eliminate the chosen tasks from the list
            for e in partsolution:
                temp[e]=math.inf
            for j in range(0,n):
            #choose from the remaining choice
                if(math.isfinite(temp[j])):
                    next_solution=partsolution.copy()
                    next_solution.append(j)
                    csf=get_csf(cost_matrix,next_solution)
                    gfc=get_gfc(cost_matrix,next_solution)
                    ffc=get_ffc(cost_matrix,next_solution)
                    lower=csf+gfc
                    upper=csf+ffc
                    #update the min_heap
                    if(not (lower>upperbound)):
                        heapq.heappush(min_heap,[lower,upper,next_solution])
                        if(upper<upperbound):
                            upperbound=upper
    #return -1 when a solution cannot be found
    return -1
#compute csf
def get_csf(cost_matrix,partial_solution):
    csf=0
    l=len(partial_solution)
    for i in range(0,l):
        csf+=cost_matrix[i][partial_solution[i]]
    return csf

#compute gfc
def get_gfc(cost_matrix,partial_solution):
    x=len(partial_solution)
    n=len(cost_matrix)
    gfc=0
    while (x<n):
        temp=cost_matrix[x].copy()
        if(partial_solution):
            for e in partial_solution:
                temp[e]=math.inf
        gfc+=min(temp)
        x+=1
    return gfc
#compute the expected future cost use greedy
def get_ffc(cost_matrix,partial_solution):
    x=len(partial_solution)
    n=len(cost_matrix)
    ffc=0
    index_removed=partial_solution.copy()
    while (x<n):
        temp=cost_matrix[x].copy()
        if(index_removed):
            for e in index_removed:
                temp[e]=math.inf
        ffc+=min(temp)
        index_removed.append(temp.index(min(temp)))
        x+=1
    return ffc

#brute_force algorithm
def brute_force(cost_matrix):#O(n!*n)
    #initialize all variables
    min_cost=math.inf
    n=len(cost_matrix)
    full_solutions=0
    optimal_solution=[]
    options=[i for i in range(0,n)]
    #get all permutation of options and calculate the cost
    permutation=list(itertools.permutations(options))
    for item in permutation:
        cost=0
        for i in range(0,n):
            index=item[i]
            cost+=cost_matrix[i][index]
        if(cost<min_cost):
            optimal_solution=item
            min_cost=cost
    #the loop will go through n! solutions, which is permuation.length
    return min_cost,list(optimal_solution), len(permutation)