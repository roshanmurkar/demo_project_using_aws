# from .app import app
from app import app
from flask_migrate import Migrate

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/test_psql"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:roshanmurkar@classroom.c6zgcadd0agd.ap-south-1.rds.amazonaws.com:5432/classroom"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)