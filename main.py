from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB


# Конфигурации приложения
DEBUG = True
SECRET_KEY = 'adsgt5478ffh3h13duj0'
DB_HOST = "localhost"
DB_NAME = "inputs_db"
DB_USER = "postgres"
DB_PASS = "hfmcjdh563"
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'

# Создание приложения Flask и БД с указанной выше конфигурацией
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)


# Создание модели для БД
class InputTable(db.Model):
    """Таблица для хранения отправленных инпутов в формате jsonb"""
    __tablename__ = 'inputs'

    id = db.Column(db.Integer, primary_key=True)
    attrs = db.Column(JSONB)

    def __init__(self, attrs):
        self.attrs = attrs

    def __repr__(self):
        return f'<Input №{self.id} - {self.attrs}>'


@app.route('/', methods=['GET', 'POST'])
def index():
    """Главная страница с динамическими инпутами и добавлением их в БД"""
    if request.method == 'POST':
        flash('Ваш текст успешно сохранен')
        db.create_all()
        inputs = dict(request.form.items())

        for value in inputs:
            arg = InputTable(attrs={value: inputs[value]})
            db.session.add(arg)
            db.session.commit()

    return render_template('index.html')


@app.route('/all_inputs', methods=['GET'])
def show_inputs():
    """Страница с отображением сохраненного текста"""
    input_table = InputTable.query.all()
    return render_template('all_inputs.html', input_table=input_table)

if __name__ == '__main__':
    app.run(debug=True)
