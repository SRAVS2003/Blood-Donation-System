import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# File path for the JSON data
DATA_FILE = 'data.json'

# Function to load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'donors': [], 'requests': []}

# Function to save data to the JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    data = load_data()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        blood_type = request.form['blood_type']

        # Add the new donor to the list
        data['donors'].append({'name': name, 'age': age, 'blood_type': blood_type})

        # Save the updated data to the JSON file
        save_data(data)

        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/request', methods=['GET', 'POST'])
def request_blood():
    data = load_data()
    if request.method == 'POST':
        requester_name = request.form['name']
        requested_blood_type = request.form['blood_type']

        # Add the new request to the list
        data['requests'].append({'requester_name': requester_name, 'blood_type': requested_blood_type})

        # Save the updated data to the JSON file
        save_data(data)

        return redirect(url_for('home'))
    return render_template('request.html')

@app.route('/admin')
def admin():
    data = load_data()
    return render_template('admin.html', donors=data['donors'], requests=data['requests'])

if __name__ == '__main__':
    app.run(debug=True)
