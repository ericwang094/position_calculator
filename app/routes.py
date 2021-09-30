from flask import render_template

from app import app
from app.position_form import PositionCalculatorForm


@app.route("/")
@app.route("/index")
def index():
    symbol_form = PositionCalculatorForm()
    return render_template("symbol_form.html", form=symbol_form)
