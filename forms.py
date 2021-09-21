import photos as photos
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, IntegerField, SubmitField, SelectField, TextField, FileField
from wtforms.validators import DataRequired, URL


class WishForm(FlaskForm):
    name = StringField("Ваше имя:", validators=[DataRequired()])
    url = StringField("Ссылка на подарок", validators=[URL()])
    description = TextField('Описание', validators=[DataRequired()])
    image = FileField('Изображение', validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
    cost = IntegerField("Стоимость, $")
    submit = SubmitField("Разместить")


class Sort(FlaskForm):
    sorting = SelectField(
        'Сортировать по: ',
        coerce=int,
        choices=[
            (0, 'порядку'),
            (1, 'стоимости дешевле'),
            (2, 'стоимости дороже'),
        ],
        render_kw={
            'class': 'form-control'
        },
    )
    submit = SubmitField("Сортировать")
