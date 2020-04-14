from jinja2 import Template
from flask_mail import Message
from flask import Flask,request
from wtforms import Form,TextAreaField, StringField,SubmitField
from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField



class ContactForm(Form):
    name = StringField('name')
    email = EmailField('email')
    subject = StringField('subject')
    message = TextAreaField('message')
    submit = SubmitField("send")

class Validator():
    form = ContactForm()

    def __init__(self,name,email,subject,message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def Test(self):
        if self.message and self.name and self.email and self.subject:
            return True
        else:
            return False

class Manager():

    def __init__(self,name,email,subject,message,recipient):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.recipient = recipient

    def manager_sender(self):
        msg = Message(self.subject,
            sender=self.email,
            recipients=['%s'%self.recipient])
        msg.body = """
        De: %s; Assunto: %s
        Mensagem:
        %s
        """ % (self.name, self.subject, self.message)
        return msg

def form_validated():
    return Validator(request.form.get('name'),
        request.form.get('email'),
        request.form.get('subject'),
        request.form.get('message')).Test()

def prepare_msg():
    return Manager(request.form.get('name'),
        email = request.form.get('email'),
        subject = request.form.get('subject'),
        message = request.form.get('message'),
        recipient='your_mail_user_here').manager_sender()



def package():
    html = Template(
    """

    <html>
    <head><meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </head>
    <div class="container">
    <div class="form-group">
    <p>
        Nome:<br />
        <input type="text" class="form-control" size="30" placeholder="Seu nome" name="name" id="name">
    </p>
    </div>
    <div class="form-group">
    <p>
        E-mail:<br />
        <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Seu email" size="30" name="email" id="email">
    </p>
    </div>
    <div class="form-group">
    <p>
        Assunto:<br />
        <input type="text"class="form-control"placeholder="Tema da Mensagem" size="35" name="subject" id="subject">
    </p>
    </div>
    <div class="form-group">
    <p>
        Comentários:<br />
        <textarea id="message" class="form-control" name="message" required="required"></textarea>
    </p>
    </div>
    <div class="form-group">
    <p>
        <input type="submit" name="submit" value="Enviar" id="submit">
    </p>
    </div>
    </div>
    </html>

    """
    )
    form = ContactForm()
    contact = html.render(form=form) 
    return contact


