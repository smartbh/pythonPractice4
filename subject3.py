#suject3

def get_bmi(kg,m):
    
    bmi = kg/((m/100)*(m/100))

    return bmi

# BMI 계산 함수 정의

def get_body_type(bmi):
    if bmi <18.5:
        print("마른 체형입니다.")

    elif bmi >=18.5 and bmi <25.0:
        print("표준 체형입니다.")

    elif bmi >=25.0 and bmi <30.0:
        print("비만 체형입니다.")

    elif bmi >=30.0:
        print("고도 비만 체형입니다.")

# BMI 기반 체질타입 반환 함수

kg = int(input("몸무게를 입력하세요(kg)"))
m = float(input("키를 입력하세요(cm)"))

a = get_bmi(kg,m)

print(a)

get_body_type(a)
