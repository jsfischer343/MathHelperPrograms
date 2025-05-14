import math
import random
import copy

#Startup Functions#
def generateRandomMatrix(m,n):
    M = [[0 for c in range(n)] for r in range(m)]
    for i in range(m):
        for j in range(n):
            M[i][j] = random.randint(-100,100)
    return M

def inputMatrix(m,n):
    M = [[0 for c in range(n)] for r in range(m)]
    for i in range(m):
        line = input()
        M[i] = list(map(int,line.split(',')))
    return M
            
def displayMatrix(M):
    for i in range(len(M)):
        print("\t\tC"+str(i),end="")
    print()
    for i in range(len(M)):
        print("R "+str(i)+"|",end="\t")
        for j in range(len(M[i])):
            print(""+"{:10.4f}".format(M[i][j])+"",end="\t")
        print("|",end="")
        print("\n",end="")
####

#Generic Row Functions#
def swapRows(M,rowIndex1,rowIndex2):
    rowLength = len(M[0])
    temp = [0 for x in range(rowLength)]
    for i in range(rowLength):
        temp[i] = M[rowIndex1][i]
    for i in range(rowLength):
        M[rowIndex1][i] = M[rowIndex2][i]
    for i in range(rowLength):
        M[rowIndex2][i] = temp[i]
    return M

def scaleRow(row,scaler):
    rowLength = len(row)
    for i in range(rowLength):
        row[i] = row[i]*scaler
    return row

def addRows(row1,row2):
    rowLength = len(row1)
    row = [0 for x in range(rowLength)]
    for i in range(rowLength):
        row[i] = row1[i]+row2[i]
    return row
    
def replaceRow(M,row,rowIndex):
    Q=copy.deepcopy(M)
    for i in range(len(row)):
        Q[rowIndex][i]=row[i]
    return Q

def copyRow(M,rowIndex):
    rowLength = len(M[0])
    row = [0 for x in range(rowLength)]
    for i in range(rowLength):
        row[i] = M[rowIndex][i]
    return row
####

#RREF Functions#
def rref(M):
    Q = copy.deepcopy(M)
    Q = organizeZeroRows(Q)
    m = len(Q)
    n = len(Q[0])
    #Lower Triangle
    for i in range(1,m):
        j=0
        while(i!=j and j<n):
            Q = singleIndexReduction(Q,i,j)
            j=j+1

    #Upper Triangle
    for i in range(1,m):
        j=0
        while(i!=j and j<n):
            Q = singleIndexReduction(Q,j,i)
            j=j+1
    for i in range(min(m,n)):
        if(Q[i][i]==0):
            break;
        Q = replaceRow(Q,scaleRow(copyRow(Q,i),1/Q[i][i]),i)
    return absoluteValueOfMatrix(Q)

def singleIndexReduction(M,rowToBeReduced,columnToBeReduced):
    if(M[rowToBeReduced][columnToBeReduced]==0 or M[columnToBeReduced][columnToBeReduced]==0):
        return M
    else:
        return replaceRow(M,addRows(copyRow(M,rowToBeReduced),scaleRow(copyRow(M,columnToBeReduced),(-1*M[rowToBeReduced][columnToBeReduced])/M[columnToBeReduced][columnToBeReduced])),rowToBeReduced)

def organizeZeroRows(M):
    rowIndex = len(M) #number of rows
    for i in range(rowIndex):
        M = organizeZeroRowsRecursive(M,rowIndex-1)
    return M
    
def organizeZeroRowsRecursive(M,rowIndex):
    if(rowIndex==0):
        return M
    else:
        if(isZeroRow(M[rowIndex])):
            return organizeZeroRowsRecursive(M,rowIndex-1)
        else:
            return organizeZeroRowsRecursive(swapRows(M,rowIndex,rowIndex-1),rowIndex-1)
        
def isZeroRow(row):
    sum = 0
    for i in range(len(row)):
        sum += row[i]
    if(sum==0):
        return True
    else:
        return False
####

#Matrix Functions#
def rank(M):
    rank=0
    m = len(M)
    n = len(M[0])
    M = rref(M)
    for i in range(m):
        for j in range(n):
            if(M[i][j]==1):
                rank+=1
    return rank

def nullity(M):
    m = len(M)
    return m-rank(M)
 
def trace(M):
    m = len(M)
    n = len(M[0])
    sum = 0
    for i in range(min(m,n)):
        sum += M[i][i]
    return sum

def linearlyIndependent(M):
    if(nullity(M)==0):
        return True
    else:
        return False
        
def appendColumnVector(M,v):
    m = len(M)
    n = len(M[0])
    if(m!=len(v)):
        raise Exception("Vector not the same length as matrix")
    newM = [[0 for c in range(n+1)] for r in range(m)]
    for i in range(m):
        for j in range(n):
            newM[i][j] = M[i][j]
    for i in range(m):
        newM[i][n] = v[i][0]
    return newM

def absoluteValueOfMatrix(M):
    m = len(M)
    n = len(M[0])
    for i in range(m):
        for j in range(n):
            M[i][j] = abs(M[i][j])
    return M
    
def matrixMulti(M1,M2):
    #m1xn1 * m2xn2 = m1xn2 (as long as n1==m2)
    m1 = len(M1)
    n1 = len(M1[0])
    m2 = len(M2)
    n2 = len(M2[0])
    if(n1!=m2):
        raise Exception("Invalid dimensions for matrix multiplication")
    else:
        newM = [[0 for c in range(n2)] for r in range(m1)]
        for i in range(m1):
            for j in range(n2):
                sum=0
                for k in range(m1):
                    sum += M1[i][k]*M2[k][j]
                newM[i][j] = sum
        return newM
                
    
####

#Column Vector Functions#
def dotProduct(v1,v2):
    m1 = len(v1)
    n1 = len(v1[0])
    m2 = len(v2)
    n2 = len(v2[0])
    dotProduct = 0
    if(n1!=1 or n2!=1):
        raise Exception("Not a vector")
    elif(m1!=m2):
        raise Exception("Vectors must be same size to compute dot product")
    else:
        for i in range(m1):
            dotProduct += v1[i][0]*v2[i][0]
        return dotProduct

def scaleVector(v,scaler):
    q = copy.deepcopy(v)
    m = len(q)
    n = len(q[0])
    norm = 0
    if(n!=1):
        raise Exception("Not a vector")
    else:
        for i in range(m):
            q[i][0] = q[i][0]*scaler
        return q

def addVectors(v1,v2):
    m1 = len(v1)
    n1 = len(v1[0])
    m2 = len(v2)
    n2 = len(v2[0])
    if(n1!=1 or n2!=1):
        raise Exception("Not a vector")
    elif(m1!=m2):
        raise Exception("Vectors must be same size to add")
    else:
        v = [[0 for c in range(1)] for r in range(m1)]
        for i in range(m1):
            v[i][0] = v1[i][0]+v2[i][0]
        return v

def norm(v):
    q = copy.deepcopy(v)
    m = len(q)
    n = len(q[0])
    norm = 0
    if(n!=1):
        raise ValueError("Error: not a vector")
    else:
        return math.sqrt(dotProduct(q,q))

def seperateColumnVector(M,columnIndex):
    m = len(M)
    n = len(M[0])
    v = [[0 for c in range(1)] for r in range(m)]
    for i in range(m):
        v[i][0] = M[i][columnIndex]
    return v

def orthagonal(v1,v2):
    m1 = len(v1)
    n1 = len(v1[0])
    m2 = len(v2)
    n2 = len(v2[0])
    if(n1!=1 or n2!=1):
        raise Exception("Not a vector")
    elif(m1!=m2):
        raise Exception("Vectors must be same size to add")
    else:
        temp = dotProduct(v1,v2)
        if(temp<0.000001 and temp>-0.000001):
            return True
        else:
            return False
    
####

#Gram-Schmidt Functions# (orthanormalization of a basis)
def gramSchmidt(M):
    if(linearlyIndependent(M)==False):
        raise Exception("Not Linearly Independent")
    m = len(M)
    n = len(M[0])
    orthanormalM = [[] for r in range(m)] #intilize empty column vector
    a = seperateColumnVector(M,0) #pull a0
    orthanormalM = appendColumnVector(orthanormalM,scaleVector(a,1/norm(a))) #q1 = a0/norm(a0)
    for i in range(1,n):
        a = seperateColumnVector(M,i) #seperate each column "a" out of the original matrix
        normOfA = norm(a)
        p = projection(a,orthanormalM) #find the projection onto the current orthanormal span
        aMinusProjection = addVectors(a,scaleVector(p,-1)) #define a-p where a is the current column vector and p is the projection
        aMinusProjectionNorm = norm(aMinusProjection)
        orthanormalM = appendColumnVector(orthanormalM,scaleVector(aMinusProjection,1/aMinusProjectionNorm)) #add a-p/norm(a-p) to the orthanormal matrix
        #print("a"+str(i)+": ",end="")#
        #print(a)#
        #print("p"+str(i-1)+": ",end="")#
        #print(p)#
        #print("||a"+str(i)+"-p"+str(i-1)+"||: ",end="")#
        #print(aMinusProjectionNorm)#
    return orthanormalM
    

def projection(vector,orthanormalM):
    #projection of vector onto the column space of M
    m = len(orthanormalM)
    n = len(orthanormalM[0])
    if(m!=len(vector)):
        raise Exception("Vector and span not in same space")
    p = [[0 for c in range(1)] for r in range(m)]
    q = [[0 for c in range(1)] for r in range(m)]
    for i in range(n):
        q = seperateColumnVector(orthanormalM,i)
        p = addVectors(p,scaleVector(q,dotProduct(vector,q)))
    return p
####

#Determinant Functions#
def det(M):
    m = len(M)
    n = len(M[0])
    if(m!=n or m==1):
        raise Exception("Invalid matrix")
    elif(m==2):
        return M[0][0]*M[1][1]-M[1][0]*M[0][1]
    else:
        sum=0
        for i in range(n):
            sum+=((-1)**i)*(M[0][i])*det(detMatrixReduction(M,i))
            #print("M[0]["+str(i)+"]: "+str(M[0][i]))
            #print("-1^"+str(i)+": "+str(-1**i))
            #print(sum)
        return sum
            
def detMatrixReduction(M,skippedColumn):
    m = len(M)
    n = len(M[0])
    Q = [[0 for c in range(n-1)] for r in range(m-1)]
    for i in range(1,m):
        for j in range(n-1):
            if(j<skippedColumn):
                Q[i-1][j] = M[i][j]
            elif(j>=skippedColumn):
                Q[i-1][j] = M[i][j+1]
    return Q
####