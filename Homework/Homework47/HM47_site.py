from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fgk32423jrr385hgfdsjaoht3hnfwue73t4bfnnmsswk3521952507'

menu = [
    {'name': 'Главная страница', 'url': 'main'},
    {'name': 'О нас', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'}
]


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', title='Главная страница', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О нас', menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение отправлено успешно", category='success')
        else:
            flash("Ошибка отправки", category='error')

    return render_template('contact.html', title='Обратная связь', menu=menu)


@app.errorhandler(404)
def page_Not_Found(error):
    return render_template('error_404.html', title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
