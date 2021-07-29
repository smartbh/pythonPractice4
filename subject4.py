#subject4

#최댓값 반환 함수 정의

def get_max(data_list):

    max = data_list[0]
    
    for i in data_list:

        if i > max:
            
            max = i
    
    return max
    

#최솟값 반환 함수 정의

def get_min(data_list):

    min = data_list[3]

    for i in data_list:

        if i <min:

            min = i

    return min


#합 반환 함수 정의
    
def get_sum(data_list):

    sum = 0

    for i in data_list:

        sum +=i

    return sum



#함수 활용

    
data_list = [1,20,13,42,5]

print("리스트 원소 : ",data_list)

print("리스트의 최댓값은 = ",get_max(data_list))

print("리스트의 최솟값은 = ",get_min(data_list))

print("리스트의 합 = ",get_sum(data_list))


