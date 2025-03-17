from backend.config.firebase_config import auth, db

def signup_user(email, password):
    """Signup a new user in Firebase Authentication."""
    try:
        user = auth.create_user(email=email, password=password)
        print(f"User {email} created successfully!")
        return user.uid
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_user_by_email(email):
    """Retrieve user UID by email."""
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except Exception as e:
        print(f"Error: {e}")
        return None

def store_user_preferences(user_id, watch_history, preferences):
    """Store user watch history and preferences in Firestore."""
    user_ref = db.collection("users").document(user_id)
    user_ref.set({
        "watch_history": watch_history,
        "preferences": preferences
    })
    print("User data stored successfully!")

def get_user_preferences(user_id):
    """Retrieve user preferences from Firestore."""
    user_ref = db.collection("users").document(user_id)
    user_data = user_ref.get()

    if user_data.exists:
        return user_data.to_dict()
    else:
        print("User not found!")
        return None
