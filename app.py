from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self) -> str:
        return f'<Todo {self.SNo} - {self.title}>'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['desc']
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/delete/<int:SNo>')
def delete(SNo):
    todo = Todo.query.get(SNo)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:SNo>', methods=['GET', 'POST'])
def update(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['desc']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', todo=todo)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)