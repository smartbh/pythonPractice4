#subject 5

#상품 추가 함수 정의

def add_goods(name, price): #상품 추가 함수
    
    goods_dict[name] = price

def list_goods(): #리스트 확인용 출력 함수
    
    print(goods_dict)

def search_goods(name): #리스트 딕셔너리 내 키값 이용, 제품 확인 함수
    
    print("제품 ",name,"은 ",goods_dict[name],"원 입니다.")

    
def total_goods(): #리스트 딕셔너리 내 키값이용, 상품 갯수 확인 함수

    a = len(goods_dict)

    return a


#함수 호출
    

goods_dict = {"연필": 300, "칫솔": 500, "공책": 500 ,"지우개": 250, "과자":1200}

while True :
    print("1. 상품 추가")
    print("2. 상품 리스트")
    print("3. 상품 검색")
    print("4. 상품의 총계 출력")
    print("5. 종료")

    print("")
    
    menu = int(input("메뉴를 선택하세요"))

    print("")

    if menu == 1 : # 상품 추가
        
        print("")
        
        name = input("상품명을 입력하세요")

        print("")

        price = int(input("상품 가격을 입력하세요"))

        add_goods(name, price)

        print("")

        print(goods_dict)

        print("")

    elif menu == 2 : # 상품 리스트 출력
        
        print("")
        
        list_goods()

        print("")

    elif menu == 3 : #상품 검색

        name = input("상품명을 검색 하세요")

        print("")

        search_goods(name)

        print("")

    elif menu == 4 : #상품 총계 출력

        print("")

        print("상품 종류는 총 ",total_goods(),"개 있습니다.")
        
        print("")        

    elif menu == 5 : #프로그램 종료

        print("프로그램을 종료 합니다.")

        print("")
        
        break
