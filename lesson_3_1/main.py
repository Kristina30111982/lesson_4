from flask import Flask, render_template, request
from flask_wtf import CSRFProtect


from models import db, User
from forms import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_1.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        user = User(firstname=firstname, lastname=lastname, email=email, password=password)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return f'Вы успешно зарегистрированы!'
    return render_template('register.html', form=form)

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = User.query.all()
    return f'{list(users)}'
