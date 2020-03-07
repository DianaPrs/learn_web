from learn_web.webapp import db, create_app

db.create_all(app=create_app())

