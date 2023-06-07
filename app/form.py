from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length

class ConceptForm(FlaskForm):
    concept = StringField('Concept', validators=[DataRequired()])


class EmotionCount(FlaskForm):
    happiness = IntegerField('Happiness', validators=[DataRequired()])
    sadness = IntegerField('Sadness', validators=[DataRequired()])
    anger = IntegerField('Anger', validators=[DataRequired()])
    fear = IntegerField('Fear', validators=[DataRequired()])
    surprise = IntegerField('Surprise', validators=[DataRequired()])
    disgust = IntegerField('Disgust', validators=[DataRequired()])
    neutral = IntegerField('Neutral', validators=[DataRequired()])

class EmotionDescribe(FlaskForm):
    describe = StringField('Describe', validators=[DataRequired()])
