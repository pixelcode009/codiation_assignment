def nextGen(grid,m,n):
    future[m][n]=grid[m][n]
    for l in range (1,m-1):
        for m in range(1,n-1):
            aliveneighbor=0
            for i in range[-1,1]:
                for j in range[-1,1]:
                    aliveneighbor+=grid[l+i]
                    
            aliveneighbor-=grid[l][m]
            if ((grid[l][m] == 1)and(aliveneighbor < 2)):
                 future[l][m] = 0;
            elif ((grid[l][m] == 1) and (aliveneighbor > 3)):
                future[l][m] = 0;
            elif ((grid[l][m] == 0) and (aliveneighbor == 3)):
                future[l][m] = 1;
            else:
                future[l][m] = grid[l][m];

    print("Result:")
    for i in range(0,m):
     for j in range(0,n):
        if(future[i][j]==0):
            print(".")
        else:
            print("*")

        print(" ")

    print("  ")
                       					
m=10
n=10
grid=[                  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
			[ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
			[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
		]
print ("Orignal grid")
for i in range(0,m):
    for j in range(0,n):
        if(grid[i][j]==0):
            print(".")
        else:
            print("*")

    print(" ")

nextGen(grid,m,n)
