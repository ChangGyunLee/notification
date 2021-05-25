from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from database.conn import db
from database.schema import Users

print(db)
print(Users)

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    # """
    # ELB 상태 체크용 API
    # :return:
    # """
    user = Users(status='active', name="코알라")
    session.add(user)
    session.commit()
    # Users().create(session, auto_commit=True, name='코알라')
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")
