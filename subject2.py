#subject 2

def add_start_to_end(start, end):
    
    sum = 0
    
    for i in range(start, end+1, 1): 
        sum += i

        #start 값부터 end값까지 1씩 증가 더하기

    return sum
        

#함수 정의

start = int(input("정수를 입력하세요"))
end = int(input("정수를 입력하세요"))

print("정수의 합은 = ",add_start_to_end(start,end))
