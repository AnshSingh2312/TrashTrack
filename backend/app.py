from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import random
from werkzeug.utils import secure_filename
from ultralytics import YOLO

app = Flask(__name__, static_folder="../static", template_folder="../templates")

MODEL_PATH = os.path.join(os.getcwd(), 'runs', 'detect', 'train', 'weights', 'best.pt')
model = YOLO(MODEL_PATH)

# Simulated database
valid_credentials = [
    {"username": "user1", "password": "p1"},
    {"username": "user2", "password": "p2"},
    {"username": "user3", "password": "p3"},
    {"username": "user4", "password": "p4"},
]

challans = []  # Store challans for users
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'Uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
incident_reports = []  # In-memory store

# ---------------------- Helper Function ------------------------ #
def detect_litter_in_image(filepath, confidence_threshold=0.5):
    results = model(filepath)

    # Get detection results with confidence filter
    detections = results[0].boxes

    filtered_boxes = [

        box for box in detections if box.conf and box.conf.item() > confidence_threshold
    ]

    detected = len(filtered_boxes) > 0
    user = random.choice(['user1', 'user2', 'user3', 'user4']) if detected else None

    return {
        "detected": detected,
        "user": user
    }


# ------------------------- Routes ------------------------------ #
@app.route('/get-challans')
def get_challans():
    # Fetch the user's challans (for demonstration, we will return all challans)
    # In a real app, you'd filter by the logged-in user
    return jsonify({"challans": challans})

@app.route('/payment/<int:challan_id>')
def payment(challan_id):
    # This is a placeholder route for payment, which could lead to a real payment page
    return f"Proceeding to payment for Challan ID: {challan_id}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/incident-report')
def incident_report():
    return render_template('incident-report.html')

@app.route('/my-challans')
def my_challans():
    return render_template('my-challans.html')

@app.route('/report-status')
def report_status():
    return render_template('report-status.html', reports=incident_reports)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/grievance')
def grievance():
    return render_template('grievance.html')

@app.route('/profile')
def profile():
    return render_template('user-profile.html')

@app.route('/rewards')
def rewards():
    return render_template('my-rewards.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    for user in valid_credentials:
        if user["username"] == username and user["password"] == password:
            return jsonify({"success": True})

    return jsonify({"success": False})

@app.route('/detect-litter', methods=['POST'])
def detect_litter():
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'No image uploaded.'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected.'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Get the description and date from the form data
    location = request.form.get('location')
    description = request.form.get('description')
    incident_date = request.form.get('date')

    result = detect_litter_in_image(filepath)
    image_url = url_for('static', filename=f"uploads/{filename}")

    if result["detected"]:
        message = f"Littering detected. Fine issued to {result['user']}."
        challans.append({
            "user": result["user"],
            "date": "2025-04-22",  # Example date, you should get the actual incident date
            "location": location,  # Example location, replace with actual location
            "complain": "Littering of plastic waste",
            "fine_amount": 1000,  # Example fine amount, you can change based on your logic
            "paid": False  # Track if the fine is paid
        })
    else:
        message = "No littering detected in the image."

    incident_reports.append({
        "image_url": image_url,
        "description": description,
        "date": incident_date,
        "status": "approved" if result["detected"] else "Declined",
        "user": result["user"],
        "message": message
    })

    return jsonify({
        "success": True,
        "detected": result["detected"],
        "user": result["user"],
        "message": message
    })


# ---------------------- Run App ---------------------------- #
if __name__ == '__main__':
    app.run(debug=True)