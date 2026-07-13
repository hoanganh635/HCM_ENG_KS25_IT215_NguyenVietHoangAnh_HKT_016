from pydantic import BaseModel, Field

class infor(BaseModel):
    title : str  
    assignee_name : str 
    priority : str
    status : str

