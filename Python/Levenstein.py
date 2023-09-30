s1 = input().lower()
s2 = input().lower()
def m(char1, char2):
    return int(not (char1 == char2))
#print([0, 1, 2, 3, 4])
def Levenstein(left, right):
    D = [0]*(len(left)+1)
    D[0] = [i for i in range(len(right)+1)]
    for i in range(1, len(D)):
        D[i] = [0]*(len(right)+1)
        D[i][0] = i

        for j in range(1, len(right)+1):
            D[i][j] = min([D[i][j-1]+1, D[i-1][j]+1, D[i-1][j-1] + m(left[i-1], right[j-1])])
        #print(D[i])
    return D[-1][-1]
print(Levenstein(s1, s2))
