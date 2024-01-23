from pydantic import BaseModel, Field
from typing import List, Dict


class TableName(BaseModel):
    table_name: str = Field(min_length=3, max_length=20)


class DatabaseCredentials(BaseModel):
    username: str = Field(min_length=5, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=5, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    host: str = Field(min_length=2, max_length=20)
    db_name: str = Field(min_length=5, max_length=20)

class ResponseConnection(BaseModel):
    message: str
    status_code: int
    
class Column(BaseModel):
    column_name: str
    data_type: str
    is_nullable: str

class DatabaseSchema(BaseModel):
    database_name: str
    tables: Dict[str, List[Column]]
    
class TableSchema(BaseModel):
    table_name: str
    columns: List[Column]