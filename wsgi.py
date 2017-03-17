from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from flask_mail import Message, Mail
import appconfig

application = Flask(__name__) 
 
application.config.from_object('appconfig.DevelopmentConfig')

mail = Mail()

mail.init_app(application)

@application.route('/')
def index():
	#return redirect(url_for('home'))
    return render_template('landing.html', page='landing')

@application.route('/home')
def home():
	return render_template('index.html', page='home')

@application.route('/about')
def about():
	return render_template('about.html', page='about')

@application.route('/portfolio')
def portfolio():
	return render_template('portfolio.html', page='portfolio')

@application.route('/services')
def services():
	return render_template('services.html', page='services')

@application.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact-us.html', form=form, page="contact")
        else:
            msg = Message(form.subject.data, sender=appconfig.MailData.FROM, recipients=appconfig.MailData.TO)
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
        
if __name__ == "__main__":
    application.run()
