from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms.validators import DataRequired


class PositionCalculatorForm(FlaskForm):
    symbol: str = StringField("Symbol", validators=[DataRequired()])
    ATR: float = FloatField("ATR", validators=[DataRequired()])
    AStarting: float = FloatField("AStrating", validators=[DataRequired()])
    BStarting: float = FloatField("BStrating", validators=[DataRequired()])
    opening: float = FloatField("Opening", validators=[DataRequired()])
    closing: float = FloatField("Closing", validators=[DataRequired()])
    open_date: str = StringField("Open Date", validators=[DataRequired()])
    open_hour: int = IntegerField("Open Hour", validators=[DataRequired()])
    close_date: str = StringField("Close Date", validators=[DataRequired()])
    close_hour: int = IntegerField("Close Hour", validators=[DataRequired()])
