def main() -> None:
    print("Hello from goorm-server!")


# 예) "인기 있는 식당의 분업 시스템"
# 작은 1인 분식집에서는 주방장이 손님 마중, 주문 받기, 요리, 설거리, 계산, 재고 관리를 혼자 다 합니다.
# 가게가 작을 땐 문제없지만, 손님이 하루 1,000명씩 오면 가게 운영에 차질이 생깁니다.
# 따라서 역할을 엄격하게 나누어 분업해야 합니다.

# 1단계. Presetation Layer (Controller / Router)
# - 역할 : 카운터 점원
# - 업무 : 손님(클라이언트)를 맞이하고, 주문서(DTO)가 올바른지 검증한 뒤, 결과를 예쁘게 포장해 응답

# 2단계. Service Layer (Business Logic)
# - 역할 : 메인 셰프
# - 업무 : 주문에 맞춰 레시피(비즈니스 규칙)대로 요리함. (예: 중복 회원 검한, 비밀번호 암호화 등)

# 3단계. Persistence Layer (Repository / DB)
# - 역할 : 창고/재고 관리자
# - 업무 : 냉장고(DB)에서 재고(데이터)를 가져오거나 새로운 재고를 저장

# ========== * ========== * ========== * ========== * ========== * ==========

# [Client (Browser / App)]

# ⬇️
# ⬇️ 01. HTTP Request (JSON)
# ⬇️
# ⬆️ 08. HTTP Response (JSON)

# [Presentation Layer(API / Controller)]
# - HTTP 요청(Request) 수신 및 상태 코드(200, 201, 400 등) 반환
# - Pydantic DTO를 통한 클라이언트 입력 데이터 유효성 검증
# - Service 계층 호출 및 결과 포맷팅

# ⬇️
# ⬇️ 02. DTO 전달 (Data Object)
# ⬇️
# ⬆️ 07. Domain Model / DTO 반환

# [Service Layer (Business / Application)]
# - 핵심 비즈니스 로직 처리 (이메일 중복 체크, 비밀번호 암호화 등)
# - 트랜잭션(Transaction) 범위 및 단위 관리
# - HTTP 프로토콜에 독립적 (순수 파이썬 로직으로 유닛 테스트 용이)

# ⬇️
# ⬇️ 03. Repository Method 호출
# ⬇️
# ⬆️ 06. Entity / ORM Model 반환

# [Persistence Layer (Data Access / Repository)]
# - 데이터베이스에 직접 접근하여 CRUD(생성·조회·수정·삭제) 쿼리 수행
# - SQLAlchemy ORM 및 AsyncSession을 활용한 데이터 입출력 캡슐화

# ⬇️
# ⬇️ 04. Async SQL Query
# ⬇️ 05. Raw Result Set

# [Database (SQLite / PostgreSQL)]