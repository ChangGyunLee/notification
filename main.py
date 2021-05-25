from fastapi import FastAPI
import uvicorn
from dataclasses import asdict

from database.conn import db
from routes import index
from common.config import conf
from typing import Optional

# print(conf)
print(db)
print(index)


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    # print(c)
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 데이터 베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터 정의
    app.include_router(index.router)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
