# write program for maximum sum of hours glass in 2D array

def hourglass(arr , i , j):
    sum = 0
    for k in range(3):
        sum += arr[i][j+k]
        sum += arr[i+2][j+k]
    sum += arr[i+1][j+1]
    return sum

# q: what does this function do?
# a: it returns the maximum sum of hourglass in 2D array