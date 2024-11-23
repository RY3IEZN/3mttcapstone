from google.cloud import firestore
import json

# Initialize Firestore client
db = firestore.Client()


def save_user_input(request):
    try:
        # Parse the JSON input
        request_json = request.get_json()
        if not request_json:
            return {"message": "Invalid request"}, 400

        # Extract user data (assuming `name` and `email` fields)
        name = request_json.get("name")
        email = request_json.get("email")

        if not name or not email:
            return {"message": "Missing fields"}, 400

        # Save to Firestore
        doc_ref = db.collection("users").add({"name": name, "email": email})

        return {"message": "Data saved successfully", "id": doc_ref[1].id}, 200

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500
