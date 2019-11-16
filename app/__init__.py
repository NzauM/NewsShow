from flask import Flask

#Initialise app
app = Flask(__name__)

from app import views
