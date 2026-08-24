def main()->None:
    print("Hello from foorm-server!")

예)"인기 있는 식당의 분업 시스템"
작은 1인 분식집에서는 주방장이 손님 마중, 주문 받기, 요리, 설겆이, 계산, 재고 관리를 혼자 다합니다.
가게가 작을 땐 문제없지만, 손니이 하누 1000명씩 오면 가게 운영에 차질이 생깁니다.
따라서 역할을 업격하게 나ㅇ누어 분업해야합니다.

1단계 Presentation Layer (Controller / Router)
-역할 : 카운터 점원
-업무 : 손님(클라이언트)를 맞이하고, 주문서(DTO)가 올바른지 검증한 뒤, 결과를 예쁘게 포장해 응답

2단계 Service Layer(Business Logic)
-역할 : 메인 세프
-업무 : 주문에 맞춰 레시피(비즈니스 규칙)대로 요리함. (예 : 중복 회원 검한, 비밀번호 암호화 등)

3단게 Persistence Layer(Repository / DB)
-역할 : 창고/재고 관리자
-업무 : 냉장고(DB)에서 재고(데이터)를 가져오거나 새로운 재고를 저장

# ======* ======*
[Client(Browser / App)]
⬇️
⬇️ 01. HTTP Request (JSON)
⬇️
⬇️ 08. HTTP 