from mongoengine import connect

def init_db():
    connect(
        db="healthcare",
        host="mongodb://localhost:27017/healthcare"
    )