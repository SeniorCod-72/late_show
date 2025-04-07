# seed.py

from app import app, db
from models import Episode, Guest, Appearance

# Create some sample episodes and guests
def create_sample_data():
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="comedian")

    db.session.add(episode1)
    db.session.add(episode2)
    db.session.add(guest1)
    db.session.add(guest2)
    db.session.commit()

    # Create sample appearances
    appearance1 = Appearance(rating=4, episode_id=episode1.id, guest_id=guest1.id)
    appearance2 = Appearance(rating=5, episode_id=episode2.id, guest_id=guest2.id)

    db.session.add(appearance1)
    db.session.add(appearance2)
    db.session.commit()

    print("Sample data created successfully.")

if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()

        # Seed data
        create_sample_data()
