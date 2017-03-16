from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Message, Mail
import config

app = Flask(__name__) 
 
app.config.from_object('config.DevelopmentConfig')

mail = Mail()

mail.init_app(app)

@app.route('/')
def index():
	return redirect(url_for('home'))

@app.route('/home')
def home():
	return render_template('index.html', page='home')

@app.route('/about')
def about():
	return render_template('about.html', page='about')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html', page='portfolio')

@app.route('/services')
def services():
	return render_template('services.html', page='services')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact-us.html', form=form, page="contact")
        else:
            msg = Message(form.subject.data, sender=config.MailData.FROM, recipients=config.MailData.TO)
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            try:
            	mail.send(msg)
            	return render_template('contact-us.html', success=True, page="contact")
            except:
            	form=ContactForm()
            	return render_template('contact-us.html',  form=form, error=True, page="contact")
            

    elif request.method == 'GET':
        return render_template('contact-us.html', form=form, success=None, page="contact")
        
