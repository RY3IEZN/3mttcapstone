from google.cloud import firestore
import json

# Initialize Firestore client
db = firestore.Client()


def save_user_input(request):
    # Set CORS headers for the response
    headers = {
        "Access-Control-Allow-Origin": "*",  # Allow all origins or replace with your domain
        "Access-Control-Allow-Methods": "POST",
        "Access-Control-Allow-Headers": "Content-Type",
    }

    # Handle preflight OPTIONS request
    if request.method == "OPTIONS":
        return ("", 204, headers)

    try:
        # Parse the JSON input
        request_json = request.get_json()
        if not request_json:
            return {"message": "Invalid request"}, 400, headers

        # Extract user data (assuming `name` and `email` fields)
        name = request_json.get("name")
        email = request_json.get("email")

        if not name or not email:
            return {"message": "Missing fields"}, 400, headers

        # Save to Firestore
        doc_ref = db.collection("users").add({"name": name, "email": email})

        return {"message": "Data saved successfully"}, 200, headers

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500, headers
