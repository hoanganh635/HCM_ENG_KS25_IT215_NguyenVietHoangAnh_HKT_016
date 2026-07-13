from pydantic import BaseModel
from database import base
from sqlalchemy import column,string,Integer

class task_db(base):
    __tablename__ = "task_db"
    id = column(Integer,primary_key=True)
    title = column(string(50))
    assignee_name = column(string(50))
    priority = column(string(50))
    status = column(string(50))
    
    
