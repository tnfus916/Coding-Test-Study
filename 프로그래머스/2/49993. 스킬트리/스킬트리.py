def check(skilltree, skill):
    ptr=0
    for letter in skilltree:
        if letter in skill:
            if skill.index(letter)==ptr:
                ptr+=1
            else:
                return False
    return True
    
    
def solution(skill, skill_trees):
    answer = 0
    
    # skill=list(skill)
        
    for skilltree in skill_trees:
        if check(skilltree,skill):
            answer+=1
                
    return answer
