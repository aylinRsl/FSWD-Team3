import os
from flask import Flask, render_template
import database 

app = Flask(__name__)

app.secret_key = "studynet-secret-key"

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'studynet.sqlite')
)
app.cli.add_command(database.init_db)
app.teardown_appcontext(database.close_db)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')




