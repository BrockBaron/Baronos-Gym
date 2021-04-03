from flask import Flask, render_template

from controllers.booking_controller import booking_blueprint
from controllers.exclass_controller import exclass_blueprint
from controllers.member_controller import member_blueprint

app = Flask(__name__)

app.register_blueprint(booking_blueprint)
app.register_blueprint(exclass_blueprint)
app.register_blueprint(member_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)