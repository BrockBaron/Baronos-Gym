from flask import Flask, render_template

import repositories.exclass_repository as exclass_repository

from controllers.booking_controller import bookings_blueprint
from controllers.exclass_controller import exclasses_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(exclasses_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    classes = exclass_repository.select_all()
    return render_template('index.html', exclasses = classes)

if __name__ == '__main__':
    app.run(debug=True)