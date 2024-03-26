# 1. FastAPI 설치
from fastapi import FastAPI
from fastapi.responses import FileResponse

# FastAPI 인스턴스 생성
app = FastAPI()

# uvicorn main:app --reload (터미널에서 실행)
# --reload: 코드 변경 시 자동으로 서버 재시작. 개발 시에만 사용.
# /docs, /redoc (자동생성된 API 문서 확인)

# 경로는 엔드포인트 또는 라우트라고 불림 -> API 설계할 때 경로는 관심사와 리소스를 분리하는 주요 방법
# Operation은 http 메서드로 작동이라고 부름, get, post, put, delete, options, head, patch 등이 있음
# post : 데이터 생성, put : 데이터 업데이트, delete : 데이터 삭제, get : 데이터 조회
@app.get("/example") # 이 문법은 파이썬에서 데코레이터라고 부름 : 아래 있는 함수를 받아 그것으로 무언가를 함
def 실습용():
    return {"Hello, World"}

@app.get("/issue")
def 실습용():
    issue = "이슈: mac에서는 pip으로 설치 못해요. 왜냐하면 pip3으로 해야합니다."
    solve = "해결: pip3 install fastapi (자세한건 구글링)"
    last = "pip3 install \"uvicorn[standard]\""
    return {"issue": issue, "solve": solve, "last": last}

# html 파일 보내기
@app.get("/")
async def html():
    await FileResponse("index.html") # async, await로 비동기 처리 가능
    return FileResponse("index.html")

# 유저에게 데이터 보내기
from pydantic import BaseModel

class Model(BaseModel):
    name: str
    age: int

@app.get("/user")
def user(data: Model):
    print(data)
    return "전송 완료"