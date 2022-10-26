'''
Function pacman(2-dList ghost):
    2-dList result
    Integer r=length of  row of ghost
    Integer c=length of column of ghost
    fill result with r*c Integers with value 0
    Integer index_row =0
    Integer index_column =0
    Do{
        Do{
            if ghost[index_row][index_column] is not equal to 1:
            //meaning that there is no ghost at this position
                if index_column-1>=0 AND index_row-1>=0:
                    result[index_row][index_column]+=result[index_row][index_column-1]+result[index_row-1][index_column]
                else if index_column-1>=0:
                    result[index_row][index_column]+=result[index_row][index_column-1]
                else if index_row-1>=0:
                    result[index_row][index_column]+=result[index_row-1][index_column]
                else:
                    result[index_row][index_column]=1
            Increment index_row
        }while(index_row<c)
        index_row=0
        Increment index_column
    }while(index_column<r-1)
    return result[r-1][c-1]
'''
'''
Complexity is O(n^2)
filling the list of result may take O(n^2) time
the nested loop takes O(R*C) time, since all the operation in the inner loop takes constant time, 
the inner loop loops c time and the outerloop loops r time, where r and c are rows and columns value
since ghost is a n*n 2-dlist, r=c=n, the nested loop takes O(n^2) time
Thus T(n)=O(n^2)+O(n^2), the algorithm has O(n^2) complexity
'''
def pacman(ghost):
    rows=len(ghost)
    columns=len(ghost[0])
    #result stores the number of legal paths that could be directed from 0,0 to that point
    result=[[0 for i in range(columns)]for j in range(rows)]
    #row and column index
    #nested loop 
    for column_i in range(0,columns):
        for row_i in range(0,rows):
            #if a ghost is at the point,there should be no path that direct to it or pass it
            if ghost[row_i][column_i] !=1:
                #case the point is at the left most edge
                if column_i==0 and row_i!=0:
                    result[row_i][column_i]=result[row_i-1][column_i]
                #case the point is at the top edge
                elif row_i==0 and column_i!=0:
                    result[row_i][column_i]=result[row_i][column_i-1]
                #normal cases
                elif column_i-1>=0 and row_i-1>=0:
                    result[row_i][column_i]=result[row_i-1][column_i]+result[row_i][column_i-1]
                #base case for 0,0
                else:
                    result[row_i][column_i]=1
    return result[rows-1][columns-1]