# Python3 program to find if there is path
# from top left to right bottom
from types import resolve_bases


# to find the path from
# top left to bottom right
def isPath(arr) :
	row = len(arr)
	col = len(arr[0])

	# directions
	Dir = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
	visited = []
	# queue
	que = []
	path_count = 0
	# insert the top right corner.
	que.append((0, 0))
	
	# until queue is empty
	while(len(que) > 0) :
		p = que[0]
		que.pop(0)
		
        # add count to 
		# mark as visited
		visited.append(("y" + str(p[0]), "x" + str(p[1]), arr[p[0]][p[1]]))
		path_count += arr[p[0]][p[1]]
		arr[p[0]][p[1]] = -1

		
		# destination is reached.
		if(p == (row - 1, col - 1)) :
			return (visited, path_count)
			
		# check all four directions
		for i in range(4) :
		
			# using the direction array
			a = p[0] + Dir[i][0]
			b = p[1] + Dir[i][1]
			
			# not blocked and valid
			if(a >= 0 and b >= 0 and a < row and b < col and arr[a][b] != -1) :		
				que.append((a, b))
	return False

# Given array
arr = [ [ 0, 0, 0, -1, 0 ],
		[ -1, 0, 0, -1, -1 ],
		[ 0, 0, 0, -1, 0 ],
		[ -1, 0, -1, 0, -1 ],
		[ 0, 0, 0, 0, 0 ] ]

arr2 = [ [ 0, -1, 0 ],
		[ 0, -1, -1 ],
		[ 0, 0, 0 ],
		[ -1, -1, 0 ]]

# path from arr[0][0] to arr[row][col]
result = isPath(arr2)
if (result == False) :
	print("No")
else :
	print(str(result[1]))

	# This code is contributed by divyesh072019
