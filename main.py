from fastapi import FastAPI, HTTPException
import nanoid
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

app = FastAPI()

type ItemId = str

@app.get("/")
def root():
    return{"message": "Hello World"}

class ItemColor(str, Enum):
    red = "red"
    blue = "blue"
    green = "green"
    yellow = "yellow"

class ItemBase(BaseModel):
    name: str = Field(description="상품명")
    color: Optional[ItemColor] = Field(default=None, description="상품 색상")
    

class Item(ItemBase):
    id: ItemId = Field(description="상품 ID")
    
temp_items = {
    "gege": Item(id="gege", name="아이템1", color=ItemColor.red),
    "gigi": Item(id="gigi", name="아이템2", color=ItemColor.blue),
}

def item_or_404(item_id: ItemId) -> Item:
    if item_id in temp_items:
        return temp_items[item_id]
    else:
        raise HTTPException(status_code=404, detail="아이템이 없어요.")

@app.get("/items/{item_id}")
def read_item(item_id: ItemId) -> Item:
    return item_or_404(item_id)


@app.post("/items", status_code=201, summary="상품 등록", description="상품을 등록합니다.")
def create_item(item: ItemBase) -> Item:
    item_id = nanoid.generate(size=10)
    if item_id in temp_items:
        raise HTTPException(status_code=400, detail="이미 존재하는 아이템입니다.")
    temp_items[item_id] = Item(id=item_id, **item.model_dump())
    return temp_items[item_id]

@app.put("/items/{item_id}", status_code=202, summary="상품 수정", description="상품을 수정합니다.")
def update_item(item_id: ItemId, item: ItemBase) -> Item:
    _ = item_or_404(item_id)
    update_item = Item(id=item_id, **item.model_dump())
    temp_items[item_id] = update_item
    return update_item

@app.delete("/items/{item_id}", status_code=204, summary="상품 삭제", description="상품을 삭제합니다.")
def delete_item(item_id: ItemId):
    _ = item_or_404(item_id)
    del temp_items[item_id]
    return {"deleted": True}