# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Episode Model
class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', backref='episode', lazy=True)

# Guest Model
class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100), nullable=False)
    appearances = db.relationship('Appearance', backref='guest', lazy=True)

# Appearance Model (for many-to-many relationship between Episode and Guest)
class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    # Constraints and validation
    db.UniqueConstraint('episode_id', 'guest_id')  # Prevent duplicate appearances
    db.CheckConstraint('rating BETWEEN 1 AND 5')  # Rating validation (1 to 5)
