# main.py에 들어가는 주요 코드 구성
# 1. FastAPI 인스턴스 생성: 애플리케이션 객체 생성 및 메타데이터(제목, 버전 등) 설정
# 2. CORS 및 미들웨어 설정: 도메인 간 요청 허용, 요청/응답 로깅, 인증 미들웨어 등
# 3. 생명주기 이벤트: 애플리케이션 시작시 DB 테이블 생성/연결, 종료시 DB 연결해제
# 4. 라우터(Router) 등록: api/ 디렉토리에 분리해 둔 엔드포인트들을 앱에 연결
# 5. 전역 예외 처리기 (Exception Handler): 앱 전체에서 발생하는 공통 에러 핸들링
# 6. 기본 헬스체크 엔드포인트: 서버 상태 확인용 테스트 API (GET /)

from fastapi import FastAPI

# 변수명이 반드시 'app'이어야 fastapi CLI가 자동으로 인식합니다.
# app = FastAPI()

# title : API 문서의 최상단 제목을 지정합니다.
# description : API 문서의 상세 설명을 적습니다. (Markdown 지원)
# version : 현재 배포된 API의 버전을 명시합니다.
# docs_url : API를 직접 테스트(Try it out)해볼 수 있는 실습용 인터페이스입니다.
# redoc_url : 깔끔하고 가독성이 뛰어난 읽기 전용(Read-only) 명세서 페이지입니다.

# FastAPI는 코드를 작성하면 두 가지 종류의 API 문서 페이지를 자동으로 생성해 줍니다.
# 이 두 문서 페이지의 접속 주소(Path)를 개발자가 원하는 대로 바꾸거나, 아예 비활성화할 수 있게 해주는 옵션입니다.

app = FastAPI(
    title="9Diin Online Class API",
    description="유튜버 9Diin의 온라인 클래스 플랫폼을 위한 백엔드 API 서비스입니다.",
    version="1.0.0",
    # docs_url="/swagger",  # 기본값 '/docs' 대신 '/swagger'로 주소 변경
    # redoc_url="/api-docs",  # 기본값 '/redoc' 대신 '/api-docs'로 주소 변경
)

# @app이 뭔가요? (데코레이터, Decorator)
# 파이썬에서 @ 기호는 "이 함수에 특별한 기능을 덧붙이겠다"라는 표시입니다.
# 이를 데코레이터(Decorator)라고 부릅니다.
# 아래 작성한 main() 함수는 그저 파이썬 코드일 뿐이라, 웹 브라우저가 접속할 수 있는 URL을 모릅니다.
# @app.get("/")을 붙여줌으로써 "FastAPI야, 누군가 인터넷 주소창에 / 경로로 들어오면
# 바로 아래에 있는 main() 함수를 실행해줘!"라고 등록하는 역할을 합니다.

# .get은 무슨 뜻인가요? (HTTP Request Method)
# 인터넷 세상에서 클라이언트(브라우저, 앱)가 서버와 대화할 때 사용하는 "행동 지침(HTTP 메서드)" 중 하나입니다.
# GET (조회): 서버에게 "정보를 보여줘/가지고 와줘"라고 요청할 때 씁니다.
# 브라우저 주소창에 URL을 치고 엔터를 누르는 행위가 모두 GET 요청입니다.

# - POST: 새로운 데이터를 생성/등록해줘 (예: 회원가입, 글쓰기)
# - PUT / PATCH: 데이터를 수정해줘
# - DELETE: 데이터를 삭제해줘

# async def는 왜 쓰나요? (비동기 처리, Async/Await)
# 파이썬의 기본 함수 선언인 def 앞에 async가 붙으면 비동기(Asynchronous) 함수가 됩니다.
# 동기 (def): 주문을 받고 음식이 나올 때까지 손님과 점원이 카운터 앞에서 멍하니 기다립니다. (앞 손님이 끝날 때까지 뒤 손님 대기)
# 비동기 (async def): 주문을 받고 진동벨을 건넨 뒤, 음식이 조리되는 동안 다음 손님의 주문을 바로 받습니다.

# FastAPI에서 쓰는 이유:
# 웹 서버는 동시 접속자가 수백, 수천 명에 달합니다.
# DB에서 데이터를 조회하거나 외부 API를 호출하는 등 "기다리는 시간"이 발생할 때,
# 서버가 멈추지 않고 다른 요청을 동시에 처리할 수 있도록 만들어주는 FastAPI의 핵심 성능 비결입니다.

# @app.get("/"): 주소창에 /를 입력하여 접속했을 때,
# async def main():: 서버가 쉬지 않고 빠르게(비동기로) 실행할 전용 함수를 정의하고,
# return {"status": "OK"}: 그 결과를 JSON 형태로 응답해준다!


@app.get("/")
async def main():
    return {"status": "OK"}

