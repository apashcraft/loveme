from flask import Flask

#from apscheduler.schedulers.background import BackgroundScheduler
from config import Config

#from app.modules.helpers import update_apod


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    """
    nasa_key = app.config['NASA_KEY']
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_apod, trigger="cron", hour=6, args=[nasa_key])
    scheduler.start()
    """

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
