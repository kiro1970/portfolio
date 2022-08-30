from flask import Flask
app = Flask(__name__)
print( f'APPNAME={__name__}')
import routes