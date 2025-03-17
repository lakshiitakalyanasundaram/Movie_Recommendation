import requests
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("backend/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# TMDb API Key (Replace with your actual key)
TMDB_API_KEY = "5cdcc7bbce44c02753df001e9901d4bd"

# Fetch movies from TMDb
def fetch_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print("Failed to fetch movies:", response.text)
        return []

# Store movies in Firestore
def store_movies_in_firestore(movies):
    movies_ref = db.collection("movies")
    for movie in movies:
        movie_id = movie["id"]
        movies_ref.document(str(movie_id)).set({
            "title": movie["title"],
            "overview": movie["overview"],
            "release_date": movie["release_date"],
            "poster_path": movie["poster_path"],
            "vote_average": movie["vote_average"],
            "genres": movie["genre_ids"]
        })
    print("Movies stored in Firestore successfully.")

# Main execution
if __name__ == "__main__":
    movies = fetch_movies()
    if movies:
        store_movies_in_firestore(movies)
