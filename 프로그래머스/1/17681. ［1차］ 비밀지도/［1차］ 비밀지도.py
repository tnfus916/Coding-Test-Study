def to_bin(num, n):
    arr=[]
    
    a = num
    while a != 0:
        a, b = divmod(a, 2)
        arr.insert(0, b)
    
    if len(arr) != n:
        arr = [0]*(n-len(arr)) + arr
        
    return arr
    
    
def solution(n, arr1, arr2):
    answer = []
    
    graph1 = []
    graph2 = []
    
    for num1 in arr1:
        graph1.append(to_bin(num1,n))
        
    for num2 in arr2:
        graph2.append(to_bin(num2,n))
    
    for i in range(n):
        string = ""
        for j in range(n):
            if graph1[i][j] + graph2[i][j] == 0:
                string += " "
            else:
                string += "#"
        answer.append(string)
    return answer