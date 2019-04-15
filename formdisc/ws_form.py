from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine , MetaData, Table, Column, Integer

from wtforms_sqlalchemy.orm import model_form

from flask_wtf import FlaskForm
from wtforms import Form, RadioField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Required
from wtforms.fields import TextField
from wtforms_components import Email

from flask_bootstrap import Bootstrap

import sys
from flask import Flask, request, Response, jsonify, render_template
import time
from flask_jsonpify import jsonify
import json
from flask_sqlalchemy import SQLAlchemy
import mercadopago
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string
from random import *
from flask_api import status
import os
from subprocess import call


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiles.sqlite'

app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'CHANGE_THIS_KEY_NOW'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bootstrap = Bootstrap(app)

class Application(Flask):
    def ready():
        db1.init_app(self)

# create multiple sqlalchemy engines
db1 = SQLAlchemy(app)



class Car(db1.Model):
    __tablename__ = 'disc'
    id = db1.Column(db1.Integer, primary_key=True)
    username = db1.Column(db1.String(50))   
    emailadr = db1.Column(db1.String(50))
    hashkey = db1.Column(db1.String(50), nullable=True)
    sex = db1.Column(db1.String(50))
    perg1 = db1.Column(db1.String(50))
    perg2 = db1.Column(db1.String(50))
    perg3 = db1.Column(db1.String(50))
    perg4 = db1.Column(db1.String(50))
    perg5 = db1.Column(db1.String(50))
    perg6 = db1.Column(db1.String(50))
    perg7 = db1.Column(db1.String(50))
    perg8 = db1.Column(db1.String(50))
    perg9 = db1.Column(db1.String(50))
    perg10 = db1.Column(db1.String(50))
    perg11 = db1.Column(db1.String(50))
    perg12 = db1.Column(db1.String(50))
    perg13 = db1.Column(db1.String(50))
    perg14 = db1.Column(db1.String(50))
    perg15 = db1.Column(db1.String(50))
    perg16 = db1.Column(db1.String(50))
    perg17 = db1.Column(db1.String(50))
    perg18 = db1.Column(db1.String(50))
    perg19 = db1.Column(db1.String(50))
    perg20 = db1.Column(db1.String(50))
    perg21 = db1.Column(db1.String(50))
    perg22 = db1.Column(db1.String(50))
    perg23 = db1.Column(db1.String(50))
    perg24 = db1.Column(db1.String(50))
    perg25 = db1.Column(db1.String(50))
    perg26 = db1.Column(db1.String(50))
    perg27 = db1.Column(db1.String(50))
    perg28 = db1.Column(db1.String(50))
    perg29 = db1.Column(db1.String(50))
    perg30 = db1.Column(db1.String(50))
    perg31 = db1.Column(db1.String(50))
    perg32 = db1.Column(db1.String(50))
    perg33 = db1.Column(db1.String(50))
    perg34 = db1.Column(db1.String(50))
    perg35 = db1.Column(db1.String(50))
    perg36 = db1.Column(db1.String(50))
    perg37 = db1.Column(db1.String(50))
    perg38 = db1.Column(db1.String(50))
    perg39 = db1.Column(db1.String(50))
    perg40 = db1.Column(db1.String(50))
    enviado = db1.Column(db1.String(50), nullable=True)
    def __unicode__(self):
        return self.name

#CarForm = model_form(Car)


cho1=[('A','Sou o animador da festa '),
      ('B','Correr riscos é comigo '),
      ('C','Analiso os detalhes sempre '),
      ('D','Eu me adapto com facilidade ')] 

cho2=[ ('A','Brinco muito com as pessoas '),
       ('B','Convenço os outros facilmente '),
       ('C','Não mudo de opinião facilmente '),
       ('D','Sou uma pessoa calma ')]   

cho3=[ ('A','Adoro me misturar '),
       ('B','Sou ligado(a) na tomada '),
       ('C','Minha missão é servir '),
       ('D','Não nasci para ser chefe ')]   

cho4=[ ('A','Dizem que tenho lábia '),
       ('B','Luto para ser o Nº1 '),
       ('C','Sou muito concentrado(a) '),
       ('D','Raramente me descontrolo ')]   

cho5=[ ('A','Estimulo o melhor nos outros '),
       ('B','Sinto que tenho potencial de crescer'),
       ('C','Sou de poucos(as) amigos(as) '),
       ('D','O Respeito sempre vem primeiro ')]   

cho6=[ ('A','Tenho uma personalidade marcante '),
       ('B','Preciso de pouca ajuda nas tarefas'),
       ('C','Percebo as coisas nas entrelinhas '),
       ('D','Sou grato(a) ao que tenho ')]   

cho7= [('A','Levo tudo na esportiva '),
       ('B','Sempre faço as coisas darem certo '),
       ('C','Gosto de planejar tudo '),
       ('D','Penso sempre a longo prazo ')]

cho8= [ ('A','Primeiro falo para depois pensar'),
        ('B','Sou muito confiante '),
        ('C','Gosto das coisas arrumadas '),
        ('D','Sou do bastidor ')]

cho9= [ ('A','Acredito que tudo dará certo no final '),
        ('B','Gosto da sinceridade '),
        ('C','Fidelidade é a coisa mais importante '),
        ('D','Amo ajudar os outros')]
      
cho10= [ ('A','Gosto de jogar charme '),
         ('B','Sou incansável '),
         ('C','Bagunça me incomoda '),
         ('D','Faço amigos facilmente ')]
       
cho11= [ ('A','Estou sempre de bem '),
         ('B','Creio que grandes riscos trazem grandes vitórias '),
         ('C','Gosto de entender a fundo as coisas que me interessam '),
         ('D','Resolvo as coisas com diplomacia ')]
      
cho12= [ ('A','Procuro encantar as pessoas '),
         ('B','Confio no meu taco '),
         ('C','Amo ler '),
         ('D','Sou uma pessoa tranquila ')]

cho13= [ ('A','Gosto de inspirar os outros '),
         ('B','Vivo a vida de modo independente '),
         ('C','Faço tudo de acordo com meus ideais '),
         ('D','Procuro trazer a paz ao meu redor ')]
      
cho14= [ ('A','Não escondo meus sentimentos '),
         ('B','Minhas decisões são firmes'),
         ('C','Vou a fundo para ter a verdade '),
         ('D','Sou uma pessoa previsível')]
      
cho15= [ ('A','Não tenho vergonha de nada '),
         ('B','Tenho muita energia '),
         ('C','Minha vida é uma trilha sonora '),
         ('D','Vivo e deixo viver ')]
       
cho16= [ ('A','Sou cheio de vida '),
         ('B','Não volto atrás no que digo '),
         ('C','Sou muito reflexivo '),
         ('D','Me divirto falando com ironia ')]
  
cho17= [ ('A','Adoro conversar '),
         ('B','Tenho facilidade em liderar '),
         ('C','Não traio a confiança de ninguém '),
         ('D','Escuto os outros antes de falar ')]
       
cho18= [ ('A','Geralmente sou o centro da rodinha '),
         ('B','Gosto de ter o comando '),
         ('C','Busco a perfeição no que faço '),
         ('D','Sou uma pessoa feliz ')]

cho19= [ ('A','Falem bem ou mal - falem de mim! '),
         ('B','Preciso ser produtivo no que faço '),
         ('C','Quero saber todos os detalhes '),
         ('D','Busco ser uma companhia agradável ')]
       
cho20= [ ('A','Sou cheio de vida '),
         ('B','Sou destemido '),
         ('C','Sou disciplinado(a) '),
         ('D','Sou ponderado(a) ')]
       
cho21= [ ('A','Dizem que sou metido '),
         ('B','Dizem que dou ordens demais '),
         ('C','Sou muito envergonhado(a) '),
         ('D','Às vezes sinto que sou vazio(a) ')]
       
cho22= [ ('A','Dizem que não sigo regras '),
         ('B','As pessoas me acham frio(a) '),
         ('C','Os outros dizem que sou rancoroso(a) '),
         ('D','Às vezes pareço sem interesse ')]

cho23= [ ('A','Eu vivo repetindo as coisas '),
         ('B','Sou sincero demais '),
         ('C','Sou uma pessoa difícil de entender '),
         ('D','Mudo de opinião facilmente ')]
       
cho24= [ ('A','Esqueço com facilidade '),
         ('B','Sou teimoso '),
         ('C','Guardo rancor dos outros '),
         ('D','Tenho medo de arriscar ')]
  
cho25= [ ('A','Não tenho filtro '),
         ('B','Não tenho paciência '),
         ('C','Às vezes não confio em mim mesmo '),
         ('D','Tenho dificuldade em decidir ')]

cho26= [ ('A','Sou pouco previsível '),
         ('B','Os outros dizem que sou insensível '),
         ('C','Não sou popular '),
         ('D','As pessoas me acham desligado ')]
       
cho27= [ ('A','Não respeito formalidades '),
         ('B','Dizem que sou orgulhoso'),
         ('C','É difícil me satisfazer '),
         ('D','Às vezes tenho muitas dúvidas ')]
      
cho28= [ ('A','Vou entrando sem pedir licença '),
         ('B','Sou cabeçudo '),
         ('C','Acham que sou alienado '),
         ('D','Sou simplório ')]
       
cho29= [ ('A','Sou passional '),
         ('B','Gosto de ter a razão '),
         ('C','Sou cauteloso demais '),
         ('D','Tenho poucas certezas nas minhas escolhas ')]
       
cho30= [ ('A','Algumas pessoas me acham egoísta'),
         ('B','Alguns me acham atrevido(a) '),
         ('C','Vejo sempre o lado ruim primeiro '),
         ('D','Por vezes, pareço Indiferente ao que acontece ')]
       
cho31= [ ('A','Às vezes sou Ingênuo demais '),
         ('B','Meu segundo nome é trabalho '),
         ('C','Prefiro me retirar para me concentrar '),
         ('D','Eu me preocupo demais com os outros ')]
       
cho32= [ ('A','É difícil que eu fique quieto '),
         ('B','Às vezes pareço indelicado '),
         ('C','Eu me emociono com facilidade'),
         ('D','Tenho muita timidez ')]

cho33= [ ('A','Tenho dificuldade para organização '),
         ('B','É fácil saber o que precisa ser feito '),
         ('C','As pessoas acham que sou deprimido '),
         ('D','Por vezes, pareço confuso ')] 

cho34= [ ('A','Dizem que sou convencido demais'),
         ('B','Tenho pouca tolerância '),
         ('C','Tenho poucos amigos '),
         ('D','Algumas pessoas me acham resmungão ')]   

cho35= [ ('A','Preciso me concentrar para manter a ordem '),
         ('B','Os outros me acham manipulador '),
         ('C','As pessoas me acham alguém triste '),
         ('D','Levo muito tempo para fazer escolhas ')]   

cho36= [ ('A','Às vezes pareço inconstante nas minhas decisões '),
         ('B','Vou até as últimas consequências em tudo que faço '),
         ('C','Só acredito em algo vendo as provas '),
         ('D','As pessoas me acham preguiçoso')]

cho37= [ ('A','Por vezes, sou agitador demais '),
         ('B','Preciso cuidar com o excesso de autoridade'),
         ('C','Prefiro ficar sozinho '),
         ('D','Costumo resmungar com frequência')]   

cho38= [ ('A','Preciso cuidar para não perder o foco '),
         ('B','Eu me irrito com facilidade '),
         ('C','Não confio em quase ninguém '),
         ('D','Dizem que sou devagar ')]   

cho39= [ ('A','Sou inquieto '),
         ('B','Às vezes, corro risco demais '),
         ('C','Devolvo o troco na mesma moeda '),
         ('D','Sou generoso demais ')]

cho40= [ ('A','Minhas emoções são uma montanha-russa '),
         ('B','Os outros me acham um espertalhão '),
         ('C','Critico demais os outros e a mim mesmo '),
         ('D','Eu pareço às vezes muito acomodado ')]

Label = "Qual das 4 opções abaixo melhor define você?"

class CarForm(FlaskForm):
    username = TextField('Nome', validators=[DataRequired()])
    emailadr = TextField('e-mail', validators=[Email(),DataRequired()])
    hashkey = TextField('Validation Hash', validators=[DataRequired()])
    sex = RadioField('Sexo', validators=[Required()] ,
        choices=[('F', 'Feminino'), ('M', 'Masculino')])   
    perg1 = RadioField(Label, validators=[Required()] , choices=cho1)
    perg2 = RadioField(Label, validators=[Required()] , choices=cho2)
    perg3 = RadioField(Label, validators=[Required()] , choices=cho3)
    perg4 = RadioField(Label, validators=[Required()] , choices=cho4)
    perg5 = RadioField(Label, validators=[Required()] , choices=cho5)
    perg6 = RadioField(Label, validators=[Required()] , choices=cho6)
    perg7 = RadioField(Label, validators=[Required()] , choices=cho7)
    perg8 = RadioField(Label, validators=[Required()] , choices=cho8)
    perg9 = RadioField(Label, validators=[Required()] , choices=cho9)
    perg10 = RadioField(Label, validators=[Required()] , choices=cho10)
    perg11 = RadioField(Label, validators=[Required()] , choices=cho11)
    perg12 = RadioField(Label, validators=[Required()] , choices=cho12)
    perg13 = RadioField(Label, validators=[Required()] , choices=cho13)
    perg14 = RadioField(Label, validators=[Required()] , choices=cho14)
    perg15 = RadioField(Label, validators=[Required()] , choices=cho15)
    perg16 = RadioField(Label, validators=[Required()] , choices=cho16)
    perg17 = RadioField(Label, validators=[Required()] , choices=cho17)
    perg18 = RadioField(Label, validators=[Required()] , choices=cho18)
    perg19 = RadioField(Label, validators=[Required()] , choices=cho19)
    perg20 = RadioField(Label, validators=[Required()] , choices=cho20)
    perg21 = RadioField(Label, validators=[Required()] , choices=cho21)
    perg22 = RadioField(Label, validators=[Required()] , choices=cho22)
    perg23 = RadioField(Label, validators=[Required()] , choices=cho23)
    perg24 = RadioField(Label, validators=[Required()] , choices=cho24)
    perg25 = RadioField(Label, validators=[Required()] , choices=cho25)
    perg26 = RadioField(Label, validators=[Required()] , choices=cho26)
    perg27 = RadioField(Label, validators=[Required()] , choices=cho27)
    perg28 = RadioField(Label, validators=[Required()] , choices=cho28)
    perg29 = RadioField(Label, validators=[Required()] , choices=cho29)
    perg30 = RadioField(Label, validators=[Required()] , choices=cho30)
    perg31 = RadioField(Label, validators=[Required()] , choices=cho31)
    perg32 = RadioField(Label, validators=[Required()] , choices=cho32)
    perg33 = RadioField(Label, validators=[Required()] , choices=cho33)
    perg34 = RadioField(Label, validators=[Required()] , choices=cho34)
    perg35 = RadioField(Label, validators=[Required()] , choices=cho35)
    perg36 = RadioField(Label, validators=[Required()] , choices=cho36)
    perg37 = RadioField(Label, validators=[Required()] , choices=cho37)
    perg38 = RadioField(Label, validators=[Required()] , choices=cho38)
    perg39 = RadioField(Label, validators=[Required()] , choices=cho39)
    perg40 = RadioField(Label, validators=[Required()] , choices=cho40)
    
    submit = SubmitField('Enviar Respostas')

    
    

    

    
@app.route('/form', methods=['GET', 'POST'])

def create_car():
    car = Car()
    success = False
    pwd = request.args.get('pword')
    engine = create_engine('sqlite:///transactions.db')
    connection = engine.connect()
    qry = engine.execute('SELECT password FROM payments').fetchall()
    qlist = [i[0] for i in qry]
    
    enginef = create_engine('sqlite:///profiles.sqlite')
    connectionf = enginef.connect()
    qryf = enginef.execute('SELECT hashkey FROM disc').fetchall()
    qlistf = [i[0] for i in qryf]
    if pwd not in qlist:
          blok = 'feito'
    else:
        if pwd in qlistf:
            blok = 'feito'
        else:
            blok = 'fazer'
    if request.method == 'POST':
        form = CarForm(request.form, obj=car)
        form.hashkey.data = pwd
        if form.validate():
            form.populate_obj(car)
            db1.session.add(car)
            db1.session.commit()
            success = True
            
            engine2 = create_engine('sqlite:///transactions.db')
            connection2 = engine2.connect()
            upd= "UPDATE payments SET usado='sim' WHERE password="+"'"+pwd+"'"
            qry2 = engine2.execute(upd)
            
            # enviar o call para API REST R 
            
            call(["curl", "http://localhost:7234/mailxpto?phash="+pwd])
            
            return redirect('/fim')
    else:
        form = CarForm(obj=car)

    return render_template('form.html', form=form, success=success, blok=blok)

@app.route('/fim')
def final():
    return render_template('fim.html', title='MindSet')

@app.route('/')
def fim():
    return render_template('comprar.html', title='MindSet')

#if __name__ == '__main__':
#    db1.create_all()
#    app.run(debug=True)
#    app.run(host='i.inova.life' , debug=True)
