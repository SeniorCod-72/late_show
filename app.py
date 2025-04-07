# app.py

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import db, Episode, Guest, Appearance

# Initialize Flask app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and Marshmallow
db.init_app(app)
ma = Marshmallow(app)

# Initialize Flask-RESTful API
api = Api(app)

# Marshmallow Schemas
class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
        include_fk = True

class GuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Guest
        include_fk = True

class AppearanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Appearance
        include_fk = True

# Resource for Episodes
class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        episode_schema = EpisodeSchema(many=True)
        return episode_schema.dump(episodes), 200

# Resource for a Single Episode
class EpisodeById(Resource):
    def get(self, episode_id):
        episode = Episode.query.get(episode_id)
        if episode:
            episode_schema = EpisodeSchema()
            return episode_schema.dump(episode), 200
        return {'error': 'Episode not found'}, 404

# Resource for Guests
class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        guest_schema = GuestSchema(many=True)
        return guest_schema.dump(guests), 200

# Resource for Appearances
class Appearances(Resource):
    def post(self):
        data = request.get_json()
        rating = data.get('rating')
        episode_id = data.get('episode_id')
        guest_id = data.get('guest_id')

        if not (1 <= rating <= 5):
            return {"errors": ["Rating must be between 1 and 5"]}, 400

        # Create a new Appearance record
        appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
        db.session.add(appearance)
        db.session.commit()

        # Return response with serialized data
        episode = Episode.query.get(episode_id)
        guest = Guest.query.get(guest_id)

        return {
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': guest.id,
            'episode_id': episode.id,
            'episode': {'date': episode.date, 'id': episode.id, 'number': episode.number},
            'guest': {'id': guest.id, 'name': guest.name, 'occupation': guest.occupation}
        }, 201

# Add Resources to API
api.add_resource(Episodes, '/episodes')
api.add_resource(EpisodeById, '/episodes/<int:episode_id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

if __name__ == '__main__':
    app.run(debug=True)
