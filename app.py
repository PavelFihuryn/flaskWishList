import os.path

from flask import Flask, render_template, request, redirect, flash, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import *
from forms import WishForm, Sort

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Wish


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Sort()
    if request.method == 'POST':
        sorting = request.form.get('sorting')
        if sorting == '0':
            wishes = db.session.query(Wish).all()
        elif sorting == '1':
            wishes = db.session.query(Wish).order_by(Wish.cost).all()
        elif sorting == '2':
            wishes = db.session.query(Wish).order_by(db.desc(Wish.cost)).all()
        return render_template("index.html", wishes=wishes, form=form)
    wishes = db.session.query(Wish).all()
    return render_template("index.html", wishes=wishes, form=form)


@app.route('/wishform', methods=['GET', 'POST'])
def wish():
    form = WishForm()
    return render_template("wish.html", form=form)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = request.form.get('name')
    url = request.form.get('url')
    cost = request.form.get('cost')
    description = request.form.get('description')

    if 'image' not in request.files:
        flash('Фото не найдено')
        return redirect(request.url)
    image = request.files['image']
    img_name = str(db.session.query(Wish).order_by(db.desc(Wish.id)).first().id + 1) + '.' + \
               image.filename.rsplit('.', 1)[1].lower()
    if image.filename == '':
        flash('Не выбрано изображение для загрузки')
        return redirect(request.url)
    if image and allowed_file(image.filename):
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], img_name))
    else:
        flash('Рашширение изображения должно быть - pnd, jpg, jpeg, gif')
        return redirect(url_for('wish'))

    db.session.add(Wish(name=name, url=url, cost=cost, description=description, image=img_name))
    db.session.commit()

    return redirect('/')


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run()
