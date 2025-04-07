# Late Show API

This project implements a Flask-based RESTful API for managing episodes, guests, and appearances on a late-night show. The API allows for querying episode details, guest information, and ratings for their appearances. The backend uses Flask, Flask-RESTful, Flask-SQLAlchemy, and Marshmallow for serialization.

## Features

- **Episodes**: Fetch a list of all episodes or a single episode by its ID.
- **Guests**: Retrieve a list of all guests.
- **Appearances**: Add an appearance for a guest on a specific episode with a rating (1-5).

## Technologies

- **Flask**: A lightweight WSGI web application framework.
- **Flask-RESTful**: Extension for creating REST APIs.
- **Flask-SQLAlchemy**: SQLAlchemy integration for Flask.
- **Marshmallow**: Object serialization and deserialization.
- **SQLite**: A simple, file-based relational database.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/seniorCod-72/late-show-api.git
cd late-show-api
2. Install Dependencies
Make sure you have Python 3.6+ installed, then create and activate a virtual environment:

bash
Copy
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
3. Set Up the Database
Before running the application, set up the database by running the seed.py file to create some sample data:

bash
Copy
python seed.py
This will create the database (late_show.db) and populate it with sample episodes, guests, and appearances.

4. Run the Application
To start the application, run:

bash
Copy
python app.py
The app will start on http://127.0.0.1:5000.

API Endpoints
Episodes
GET /episodes
Get a list of all episodes.

GET /episodes/{episode_id}
Get details of a single episode by ID.

Guests
GET /guests
Get a list of all guests.

Appearances
POST /appearances
Create an appearance with a rating for a specific episode and guest.

Example Request for Appearances
To create an appearance, you can send a POST request with the following JSON body:

json
Copy
{
  "rating": 4,
  "episode_id": 1,
  "guest_id": 1
}
Sample Response for Appearances
json
Copy
{
  "id": 1,
  "rating": 4,
  "guest_id": 1,
  "episode_id": 1,
  "episode": {
    "date": "1/11/99",
    "id": 1,
    "number": 1
  },
  "guest": {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  }
}
Models
Episode
id: Integer, primary key.

date: String, the date the episode aired.

number: Integer, the episode number.

Guest
id: Integer, primary key.

name: String, the guest's name.

occupation: String, the guest's occupation.

Appearance
id: Integer, primary key.

rating: Integer, a rating between 1 and 5.

episode_id: Foreign key to the Episode model.

guest_id: Foreign key to the Guest model.

Database Constraints
Unique Constraint: Prevents duplicate appearances for the same guest in the same episode.

Check Constraint: Ensures the rating is between 1 and 5.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Authors
seniorCod-72 - Initial work and API design

Enjoy using the Late Show API! 🎤📺

markdown
Copy

### Key Sections:
1. **Introduction**: A short overview of the project and its functionality.
2. **Installation Instructions**: Steps to clone the repository, install dependencies, and set up the database.
3. **API Documentation**: Details about the available endpoints and example requests/responses.
4. **Models**: Information about the database schema and constraints.
5. **Contributing**: Guidelines for contributing to the project.
6. **License**: Mentions the project license (you can adjust it as needed).

