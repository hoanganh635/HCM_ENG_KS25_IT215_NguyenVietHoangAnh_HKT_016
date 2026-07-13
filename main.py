from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import session
import database
import model
from chemas import infor

app = FastAPI()

@app.get("get/",tags=["GET"])
def get_health():
    return {"message": "API đang chạy"}
    
@app.get("get/tasks/",tags=["GET"])
def get_all_tasks(db: session Depends(get_db())):
    if(db.query("task_db")):
        return {"message":"lay thanh cong"}
    else:
        return {"message":" chưa có thông tin"}
    
@app.get("get/tasks/search",tags=["GET"])
def get_tasks_bystatus(status_find: str, db: session Depends(get_db())):
    mylist = []
    mylist = db.query("task_db").filter(status = status_find)
    if(mylist):
        return {"message": "thanh cong",
                "data" : mylist}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ko tim thay")
   
@app.get("get/tasks/{task_id}",tags=["GET"])
def get_task_id(db: session Depends(get_db()) , task_id: int):
    mylist = []
    mylist = db.query("task_db").filter(id = task_id)
    if(mylist):
        return {"message": "thanh cong",
                "data" : mylist}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ko tim thay")
    
@app.post("post/tasks",tags= ["POST"]) 
def post_task(db: session Depends(get_db()),mypost:infor):
    db.add("mypost")
    db.commit()
    