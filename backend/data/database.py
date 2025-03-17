import firebase_admin
from firebase_admin import credentials, firestore
from backend.config.firebase_config import db

# Check if Firebase is already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("backend/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

# Firestore database reference
def get_user_watch_history(user_id):
    """Retrieve a user's watch history from Firestore."""
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get()
    if user_data.exists:
        return user_data.to_dict().get("watch_history", [])
    return []

def update_user_watch_history(user_id, movie_id):
    """Update the user's watch history with a new movie."""
    user_ref = db.collection("users").document(user_id) 
    user_ref.update({"watch_history": firestore.ArrayUnion([movie_id])})
