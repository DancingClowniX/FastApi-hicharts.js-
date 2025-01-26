
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime
from typing import List, Union
from pydantic import BaseModel
from typing import Optional,List,Dict
import sqlite3
from fastapi.staticfiles import StaticFiles
app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def read_user(request:Request):
    import os
    import sqlite3
    import openpyxl

    def export_to_sqlite():
        '''Экспорт данных из xlsx в sqlite'''

        # 1. Создание и подключение к базе

        # Получаем текущую папку проекта
        prj_dir = os.path.abspath(os.path.curdir)

        a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Имя базы
        base_name = 'auto.sqlite3'

        # метод sqlite3.connect автоматически создаст базу, если ее нет
        connect = sqlite3.connect(prj_dir + '/' + base_name)
        # курсор - это специальный объект, который делает запросы и получает результаты запросов
        cursor = connect.cursor()

        # создание таблицы если ее не существует
        cursor.execute('CREATE TABLE IF NOT EXISTS table_data (bp, id int, status, plan_date date,prognoz_date date, filial,check_plan, check_fact,plan_month int,plan_year int,min_date_fact_month int,min_date_fact_year int)')

        # 2. Работа c xlsx файлом

        # Читаем файл и лист1 книги excel
        file_to_read = openpyxl.load_workbook('bd_file.xlsx', data_only=True)
        sheet = file_to_read['Лист1']

        # Цикл по строкам начиная со второй (в первой заголовки)

        for row in range(2, sheet.max_row + 1):
            # Объявление списка
            data = []
            # Цикл по столбцам от 1 до 4 ( 5 не включая)
            for col in range(1, 13):
                # value содержит значение ячейки с координатами row col
                value = sheet.cell(row, col).value
                # Список который мы потом будем добавлять
                data.append(value)

            # 3. Запись в базу и закрытие соединения

            # Вставка данных в поля таблицы
            cursor.execute("INSERT INTO table_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (data[0], data[1], data[2], data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]))

        # сохраняем изменения
        connect.commit()
        # закрытие соединения
        connect.close()
    export_to_sqlite()
    return templates.TemplateResponse("home.html",{"request":request})
