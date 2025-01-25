from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

def get_cats():
  con = sqlite3.connect('flask_bd.db')
  cursor = con.cursor()
  results = cursor.execute('SELECT * from cats')
  results_all = results.fetchall()
  data = {
    'cats': results_all
  }
  print(data)
  return data

@app.route('/')
def hello():
  data = get_cats()
  print(data)
  return render_template('hello.html',info=data)

if __name__ == '__main__':
  app.run(debug=True)