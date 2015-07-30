import os
from flask import Flask

app = Flask(__name__)

from ToppTrack import views
from views import *