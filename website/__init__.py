from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'icebreaker.asm'
    app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcBOu0lAAAAAGDeecAdY2kYxSuhah_mQDxOo5y5'
    app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcBOu0lAAAAABxwJ7Cg8H8Ffc15rqjOj4H5yIZD'
    from .views import views

    app.register_blueprint(views,url_prefix = '/')
    return app