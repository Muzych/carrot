# 程序入口文件
import uvicorn
from fastapi import FastAPI
from utils.logger import logger



app = FastAPI()

app.include_router()