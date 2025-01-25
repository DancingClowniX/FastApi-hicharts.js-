import sqlite3
from functools import wraps
import telebot
from telebot import types
'''
установить соединение с бд
запрос к бд
сохранить
закрыть
'''


def connect_with_DB(func):
    @wraps(func)
    def f(*args,**kwargs):
        conn = sqlite3.connect('school.db')
        cursor = conn.cursor()
        try:
            result = func(cursor, *args, **kwargs)
        except Exception as e:
            print('Error connect to', e)
        finally:
            conn.close()
        return result
    return f

@connect_with_DB
def show_teacher(cursor):
    cursor.execute('''
        SELECT FirstName,LastName,SubjectName
        FROM Teacher
        join Subject
        on Teacher.SubjectID == Subject.SubjectID
        ''')
    teachers = cursor.fetchall()
    teachers = '\n'.join([' '.join(teacher) for teacher in teachers])
    return teachers

@connect_with_DB
def show_teacher_predmet(cursor):
    cursor.execute('''
        SELECT FirstName,LastName,SubjectName
        FROM Teacher
        join Subject
        on Teacher.SubjectID == Subject.SubjectID
        ''')
    teachers = cursor.fetchall()
    teachers = '\n'.join([' '.join(teacher) for teacher in teachers])
    return teachers



@connect_with_DB
def is_existing_subject(cursor, subject_name):
    cursor.execute('SELECT SubjectName from subject')
    subjects = cursor.fetchall()
    subjects = [''.join(subject).lower() for subject in subjects]
    return subject_name.lower() in subjects


API_TOKEN = '7295540178:AAF9W6cL5XKLf1M6dKXCGk1nt5jaAUkmGl0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я бот, созданный с помощью библиотеки telebot.")

@bot.message_handler(commands=['show_teachers'])
def send_teachers(message):
    teachers = show_teacher()
    bot.send_message(message.chat.id, teachers)

@bot.message_handler(commands=['show_teachers_predmet'])
def send_teachers(message):
    teachers_predmet = show_teacher_predmet()
    bot.send_message(message.chat.id, teachers_predmet)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    subject = message.text
    if is_existing_subject(subject):
        bot.send_message(message.chat.id, 'Такой предмет есть и потом покажем преподов')
    else:
        bot.send_message(message.chat.id, 'такого предмета нет')


'''
написать код для получения всех преподавателей по заданному предмету 
и сделать отображения через бота
Сделать код, который показывать расписание выбранного преподавателя
'''
bot.polling(none_stop=True)