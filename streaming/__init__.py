from flask import Flask

def CreateApp():
    app = Flask(__name__)

    from streaming.views import views
    app.register_blueprint(views)

    return app
