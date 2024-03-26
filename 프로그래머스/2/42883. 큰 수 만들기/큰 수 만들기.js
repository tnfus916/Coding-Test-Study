function solution(number, k) {
    var answer = '';
    const stack=[number[0]];
    
    cnt=0
    for (let i=1; i<number.length; i++){
        while (stack[stack.length-1]<number[i] && cnt < k){
            stack.pop()
            cnt+=1;
        }
        stack.push(number[i]);
    }
    
    
    while (cnt<k){
        stack.pop();
        cnt+=1
    }
    
    stack.forEach((num)=>answer+=num);
    
    return answer;
}