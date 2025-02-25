from pydantic import BaseModel,Field#Field用于给字段添加额外信息
from typing import List

class Xiaohongshu(BaseModel):
    titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    content: str = Field(description="小红书的正文内容")