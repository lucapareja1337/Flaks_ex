from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tarefas.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from models import Tarefa

@app.route('/')
def index():
    tarefas=Tarefa.query.all()

    return render_template('index.html',tarefas=tarefas)

@app.route('/nova_tarefa', methods=['GET','POST'])
def nova_tarefa():


    if request.method == 'GET':
        return render_template('form_tarefa.html')
    else:
        descricao=request.form['descricao']

        tarefa = Tarefa(descricao = descricao)
        db.session.add(tarefa)

        db.session.commit()

        return redirect(url_for('index'))


@app.route('/concluirtarefa<id>',methods=['GET'])
def concluir_tarefa(id):
    tarefa=Tarefa.query.filter_by(id=id)
    tarefa.delete()

    db.session.commit()

    return index()



if __name__ == '__main__':
    app.run()


