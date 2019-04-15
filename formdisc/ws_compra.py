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

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'CHANGE_THIS_KEY_NOW'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'payments'
    _id = db.Column(db.Integer, primary_key=True)
    mpid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(120), nullable=False)
    time = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    usado = db.Column(db.String(120), nullable=True)
    def __repr__(self):
        return '<User %r>' % self.username


# gerar senha

@app.route('/oisadj123120daowee58', methods=['GET', 'POST'])
def notifications():
    mtopic = request.args.get('topic')
    idmp = request.args.get('id')

    if mtopic != 'payment':
      sys.exit('Error - wrong topic')
    else:
      stime = time.asctime()
      result = {'topic': 'payment','id': idmp,'time':stime}
      js = json.dumps(result)
      resp = jsonify(result)
      #resp.status_code = 200
      
      mp = mercadopago.MP("CHANGE_THIS_KEY_NOW", "CHANGE_THIS_KEY_NOW")
      accessToken = mp.get_access_token()

      mp = mercadopago.MP(accessToken)
      link = '/v1/payments/'
      val = '%s%s' % (link,idmp)
      payment = mp.get (val)
      useremail = payment['response']['payer']['email']
      statuscod = payment['response']['status']
      
      if statuscod != 'approved':
        dados2 = User(mpid=idmp, time=stime , status=statuscod,email=useremail,password=None)

        db.session.add(dados2)
        db.session.commit()
        return resp, status.HTTP_200_OK
      else:
        if useremail == None:
          return resp, status.HTTP_200_OK
      
        else:  
      # senha:
      
         n_char = 8
         allchar = string.ascii_letters + string.digits
         passwd = "".join(choice(allchar) for x in range(randint(n_char,n_char)))
       
         quizlink = "http://quiz.inova.life/form?pword="+passwd
       # LOCALHOST (para testes): 
       #quizlink =  "http://127.0.0.1:5000/form?pword="+passwd
    
      # ENVIAR E-MAIL:
 
         fromaddr = 'relatoriodisc@gmail.com'
         toaddr = useremail
         msg = MIMEMultipart()
         msg['From'] = fromaddr
         msg['To'] = toaddr
         msg['Subject'] = 'Bem-vindo ao MindSet!'
  
         body = "Olá! Parabéns pelo seu investimento! \n Para você entrar em nossa plataforma, siga as instruções abaixo: \n\n - Clique no link: %s \n - Preencha o formulário \n\n - Pronto! Em alguns instantes, você receberá por e-mail seu Perfil MindSet.\n\n Um abraço! \n Equipe Mindset. \n ATENÇÃO - Não responda a este e-mail.  Caso precise de ajuda, envie uma mensagem para suporte@inova.life" % (quizlink)
         msg.attach(MIMEText(body, 'plain'))
  
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login(fromaddr, 'CHANGE_THIS_KEY_NOW')
         text = msg.as_string()
         server.sendmail(fromaddr, toaddr, text)
         server.quit()

         dados = User(mpid=idmp, time=stime , status=statuscod,email=useremail,password=passwd)
    
         db.session.add(dados)
         db.session.commit()

         return resp, status.HTTP_200_OK

#if __name__ == '__main__':
#     db.create_all()
#     app.run(port=5001,debug = True)


