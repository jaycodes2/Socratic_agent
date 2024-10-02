import os

class Config:
    MONGO_URI = os.environ.get('MONGO_URI') or "mongodb://localhost:27017/socraticDB"
    CORS_HEADERS = "Content-Type"


