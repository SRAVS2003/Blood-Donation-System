🩸 Blood Donation System
A web-based application built using Flask that facilitates seamless blood donation and blood request management. This system allows users to register as blood donors, request blood, and provides an admin panel to manage donor and request data.

🚀 Features
🧑‍🤝‍🧑 Register as Donor: Users can submit their details to become a blood donor.

🩸 Request Blood: Patients or hospitals can raise blood requests.

📋 Admin Panel: Admins can view and manage donor and request records.

🎨 Responsive Frontend: Styled using HTML, CSS and served with Flask.

💾 Data Handling: Supports storing data in data.json (can be upgraded to use MySQL or SQLite).

🛠️ Tech Stack
Frontend: HTML, CSS

Backend: Python, Flask

Storage: JSON (can be extended to SQL databases)

📁 Folder Structure
pgsql
Copy
Edit
Blood Donation System/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── request.html
│   └── admin.html
│
├── data.json
└── app.py
📌 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/blood-donation-system.git
Navigate into the project directory:

bash
Copy
Edit
cd blood-donation-system
Install dependencies:

bash
Copy
Edit
pip install flask
Run the Flask app:

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000

