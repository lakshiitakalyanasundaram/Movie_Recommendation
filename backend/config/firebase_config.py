import firebase_admin
from firebase_admin import credentials, firestore, auth


# Load Firebase credentials (Update with your actual file path)
if not firebase_admin._apps:
    cred = credentials.Certificate("/Users/lakshiitakalyanasundaram/Desktop/Machine Learning/Movie_Recommendation/backend/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

# Firestore database
db = firestore.client()
