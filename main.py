
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from typing import List, Union
from pydantic import BaseModel
from typing import Optional,List,Dict
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount('/static', StaticFiles(directory='static'), name='static')

users = [{'id':1,'name':'Jhon','age':23},
         {'id':2,'name':'Kevin','age':33},
         {'id':3,'name':'bob','age':45}]

posts = [{'id':1,'title':'news1','body':'text1','author':users[0]},
         {'id':2,'title':'news2','body':'text2','author':users[1]},
         {'id':3,'title':'news3','body':'text3','author':users[2]}]


@app.get("/")
async def read_user(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

# @app.post("/posts/add")
# async def add_item(post:PostCreate)->Post:
#     author = next((user for user in users if user['id'] == post.author_id),None)
#     if not author:
#         raise HTTPException(status_code=404,detail='user_not found')
#     new_post_id = len(posts)+1
#     new_post = {'id':new_post_id,'title':post.title, 'body':post.body,'author':author}
#     posts.append(new_post)
#     return Post(**new_post)
#
# @app.get("/posts/{id}")
# async def post(id:int)->Post:
#     for post in posts:
#         if post['id'] ==id:
#             return Post(**post)
#
#
# @app.get("/search")
# async def search(post_id: Optional[int]=None)-> Dict[str,Optional[Post]]:
#     if post_id:
#         for post in posts:
#             if post['id'] == post_id:
#                 return {"data":Post(**post)}
#     else:
#         return {"data": "no post id"}
