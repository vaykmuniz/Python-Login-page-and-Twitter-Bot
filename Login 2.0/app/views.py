from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from .forms import RegistrationForm, LoginForm
from .models import Users
from app import app, db, login_manager


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        check = Users.query.filter_by(username=form.username.data).first()
        if check is None:
            flash(f'A conta {form.username.data} não existe!', 'danger')
            return redirect ('/login')
        else:
            if form.username.data == check.username and form.password.data == check.password:
                login_user(check)
                flash(f'Logou em {form.username.data}!', 'success')
                return redirect ('/')
            else:
                flash(f'Senha inválida!', 'warning')
                return redirect ('/login')

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        check = Users.query.filter_by(username=form.username.data).first()
        if check is None:
            tmp_usuario = Users(username = form.username.data, password = form.password.data)
            try:
                db.session.add(tmp_usuario)
                db.session.commit()
                flash(f'Conta criada para {form.username.data}!', 'success')
                return redirect ('/register')
            except:
                flash(f'A conta não conseguiu ser criada!', 'danger')
                return redirect ('/register')
        else:
            flash(f'O username utilizado já existe!', 'warning')
            return redirect ('/register')

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f'Você saiu da sua conta!', 'warning')
    return redirect('/')
