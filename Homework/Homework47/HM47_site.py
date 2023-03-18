from flask import Flask, render_template, url_for, request, flash, session, abort, redirect, g
import sqlite3
import os
from FDataBase_HM47 import FDataBase_HM47

DATABASE = "/tmp/HM47.db"
DEBUG = True
SECRET_KEY = 'bd21ad05ac494f2ee36ad5a5a1b047eaddcaa498'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'HM47.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('hm47_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
@app.route('/main')
def main():
    db = get_db()
    dbase = FDataBase_HM47(db)
    return render_template('main.html', title='Курсы', menu=dbase.get_menu(), courses=dbase.get_courses_announce())


@app.route('/add_post', methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase_HM47(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash("Статья добавлена успешно", category='success')
        else:
            flash("Ошибка добавления статьи", category='error')

    return render_template("add_post.html", title="Добавление статьи", menu=dbase.get_menu())


@app.route("/courses/<int:id_courses>")
def show_post(id_courses):
    db = get_db()
    dbase = FDataBase_HM47(db)
    title, price, info = dbase.get_courses(id_courses)
    if not title:
        abort(404)

    return render_template('courses.html', title=title, info=info, menu=dbase.get_menu())


@app.route('/about')
def about():
    db = get_db()
    dbase = FDataBase_HM47(db)
    return render_template('about.html', title='О нас', menu=dbase.get_menu())


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно", category='success')
        else:
            flash("Ошибка отправки", category='error')
    db = get_db()
    dbase = FDataBase_HM47(db)

    return render_template('contact.html', title='Обратная связь', menu=dbase.get_menu())


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "admin" and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    db = get_db()
    dbase = FDataBase_HM47(db)
    return render_template('login.html', title="Авторизация", menu=dbase.get_menu())


@app.errorhandler(404)
def page_Not_Found(error):
    db = get_db()
    dbase = FDataBase_HM47(db)
    return render_template('error_404.html', title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
