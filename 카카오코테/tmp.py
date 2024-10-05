def solution(edges):
    answer = [0,0,0,0]

    global graph, visit, num

    graph={}
    for a,b in edges:
        if a not in graph:
            graph[a]=[b]
        else:
            graph[a].append(b)
    print(graph)
    
    visit=[0]*(max(graph)+1)
    
    num=[]
    # i: 1 ~ max(graph)
    for i in range(1,max(graph)+1):
        if i in graph and visit[i]==0:
            if len(graph[i])>2: # 새로 생성된 정점(간선을 3개 이상 가짐)
                for node in graph[i]:
                    if visit[node]==0:
                        dfs(node) # 각각 무슨 그래프였는지 반환
                        for number in num:
                            answer[number]+=1
                        num=[]
                answer[0]=i

            else: # 3가지 그래프의 정점일 때 
                dfs(i)
                for number in num:
                    answer[number]+=1
                num=[]
    print(answer)
    return answer

def dfs(pre):
    visit[pre]=1
    
    if pre in graph:
        for post in graph[pre]:
            print(num)
            if post not in graph and 2 not in num:
                num.append(2)

            if visit[post]==0:
                dfs(post)
            else:
                leng=len(graph[post])
                if leng==1 and 1 not in num: # visit가 걸렸는데 뻗어나가는 간선이 1개이므로 도넛 그래프.
                    num.append(1)
                elif leng==2 and 2 not in num:
                    num.append(3) # visit가 걸렸는데 뻗어나가는 간선이 2개이므로 8자 그래프.

    return
    
    
    
solution([(2,3),(4,2),(1,1),(2,1)])

print(max([[4,7],[3,5]]))

def solution(edges):
    answer = [0,0,0,0]

    global graph, visit, num

    graph={}
    for a,b in edges:
        if a not in graph:
            graph[a]=[b]
        else:
            graph[a].append(b)
    
    visit=[0]*(max(graph)+1)
    
    num=[]
    # i: 1 ~ max(graph)
    for i in range(1,max(graph)+1):
        if i in graph and visit[i]==0:
            print(i)
            # if len(graph[i])>2: # 새로 생성된 정점(간선을 3개 이상 가짐)
            #     for node in graph[i]:
            #         if node in graph and visit[node]==0:
            #             dfs(node,node) # 각각 무슨 그래프였는지 반환
            #             for number in num:
            #                 answer[number]+=1
            #             num=[]
            #             for i in range(1,max(graph)+1):
            #                 if visit[i]==1:
            #                     visit[i]=2

            #     answer[0]=i

            # else: # 3가지 그래프의 정점일 때 
            dfs(i,i)
            for number in num:
                answer[number]+=1
            num=[]
            for i in range(1,max(graph)+1):
                if visit[i]==1:
                    visit[i]=2
            print('a',answer)
            
    print(answer)
    return answer

def dfs(srt,pre):
    visit[pre]=1
    
    for post in graph[pre]:
        if len(graph[pre])==2 and pre!=srt: # 처음 시작 정점이 아닌 다른 정점이 2개 간선을 가지면 무조건 8자 그래프
            if 3 not in num:
                num.append(3)

        if visit[post]==0:
            if post not in graph: # post는 막대그래프의 마지막 정점
                visit[post]=1
                if 2 not in num:
                    num.append(2)
            else:
                dfs(srt,post)
        elif visit[post]==1:
            if 3 not in num:
                if post in graph and len(graph[post])==1: # visit가 걸렸는데 뻗어나가는 간선이 1개이므로 도넛 그래프 또는 막대 그래프.
                    if post==srt and 1 not in num: 
                        num.append(1)
                    elif post!=srt and 2 not in num:
                        num.append(2)
        else:
            visit[pre]=2
            continue

            





        # if post in graph and len(graph[post])==2:
        #     leng==2 and 3 not in num:
        #             num.append(3) # visit가 걸렸는데 뻗어나가는 간선이 2개이므로 8자 그래프.
        #             visit[post]=2

        # if visit[post]==0:
        #     if post not in graph and 2 not in num: # 끝값일 때, 막대 그래프 
        #         num.append(2)
        #         visit[post]=2
        #         continue

        #     dfs(srt,post)

        # else:
        #     if post in graph: # 그래프가 사이클이 있거나 중간에 시작된 막대그래프의 앞 정점.
        #         print('1',visit)
        #         if visit[post]==2: # 이미 count한 그래프이므로 패스
        #             continue
        #         leng=len(graph[post])
        #         if leng==1: # visit가 걸렸는데 뻗어나가는 간선이 1개이므로 도넛 그래프 또는 막대 그래프.
        #             if post==srt and 1 not in num: 
        #                 num.append(1)
        #             elif post!=srt and 2 not in num:
        #                 num.append(2)
        #             visit[post]=2
        #         elif 
        #         print('2',visit)

    return
    

    def solution(edges):
    answer = [0,0,0,0]

    global graph, visit, num

    graph={}
    for a,b in edges:
        if a not in graph:
            graph[a]=[b]
        else:
            graph[a].append(b)
    
    visit=[0]*(max(graph)+1)
    
    num=[]
    # i: 1 ~ max(graph)
    for i in range(1,max(graph)+1):
        if i in graph and visit[i]==0:
            print(i)
            # if len(graph[i])>2: # 새로 생성된 정점(간선을 3개 이상 가짐)
            #     for node in graph[i]:
            #         if node in graph and visit[node]==0:
            #             dfs(node,node) # 각각 무슨 그래프였는지 반환
            #             for number in num:
            #                 answer[number]+=1
            #             num=[]
            #             for i in range(1,max(graph)+1):
            #                 if visit[i]==1:
            #                     visit[i]=2

            #     answer[0]=i

            # else: # 3가지 그래프의 정점일 때 
            dfs(i,i)
            for number in num:
                answer[number]+=1
            num=[]
            for i in range(1,max(graph)+1):
                if visit[i]==1:
                    visit[i]=2
            print('a',answer)
            
    print(answer)
    return answer

def dfs(srt,pre):
    visit[pre]=1
    
    for post in graph[pre]:
        if len(graph[pre])==2 and pre!=srt: # 처음 시작 정점이 아닌 다른 정점이 2개 간선을 가지면 무조건 8자 그래프
            if 3 not in num:
                num.append(3)

        if visit[post]==0:
            if post not in graph: # post는 막대그래프의 마지막 정점
                visit[post]=1
                if 2 not in num:
                    num.append(2)
            else:
                dfs(srt,post)
        elif visit[post]==1:
            if post in graph:
                if len(graph[post])==2:
                    if 3 not in num:
                        num.append(3)
                elif len(graph[post])==1: # visit가 걸렸는데 뻗어나가는 간선이 1개이므로 도넛 그래프 또는 막대 그래프.
                    if post==srt and 1 not in num: 
                        num.append(1)
                    elif post!=srt and 2 not in num:
                        num.append(2)
        else:
            if len(graph[pre])==1:
                visit[pre]=2
                continue

    return       





        # if post in graph and len(graph[post])==2:
        #     leng==2 and 3 not in num:
        #             num.append(3) # visit가 걸렸는데 뻗어나가는 간선이 2개이므로 8자 그래프.
        #             visit[post]=2

        # if visit[post]==0:
        #     if post not in graph and 2 not in num: # 끝값일 때, 막대 그래프 
        #         num.append(2)
        #         visit[post]=2
        #         continue

        #     dfs(srt,post)

        # else:
        #     if post in graph: # 그래프가 사이클이 있거나 중간에 시작된 막대그래프의 앞 정점.
        #         print('1',visit)
        #         if visit[post]==2: # 이미 count한 그래프이므로 패스
        #             continue
        #         leng=len(graph[post])
        #         if leng==1: # visit가 걸렸는데 뻗어나가는 간선이 1개이므로 도넛 그래프 또는 막대 그래프.
        #             if post==srt and 1 not in num: 
        #                 num.append(1)
        #             elif post!=srt and 2 not in num:
        #                 num.append(2)
        #             visit[post]=2
        #         elif 
        #         print('2',visit)


    