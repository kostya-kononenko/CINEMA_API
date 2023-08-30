# CINEMA_API

The RESTful API for a movie. 


## User Registration and Authentication (using Djoser library):

- Users can register with their username and password to create an account with email confirmation.
- Users can log in with their credentials and receive a token for authentication (JWT or simple Token).
- Users can log out and invalidate their token.

## User Profile:
- Users can create, update, and delete their profile.

## Movie/Actors/Genres Retrieval:
- Users can retrieve movies, genres, actors, and directors.

## Comments:
- Users can add comments to the movie and comments for another comment.

## Add star ratings:
- Users can add star ratings for all movies.

## API Documentation:
- The API is well-documented with clear instructions on how to use each endpoint.
- The documentation includes sample API requests and responses for different endpoints.

## How to install using GitHub

- Clone this repository
- Create venv: python -m venv venv
- Activate venv: source venv/bin/activate
- Install requirements: pip install -r requirements.txt
- Run: python manage.py runserver
- Create user via: auth/register
- Get access token via: auth/tokin
