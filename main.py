import re
from flask import Flask, request, jsonify

# Define a regex pattern to match common password patterns (e.g. "password1")
pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])")

# Create a Flask app
app = Flask(__name__)

@app.route('/check-password-strength', methods=['POST'])
def check_password_strength():
  # Get the password from the request body
  password = request.json['password']
  
  # Check the length of the password and assign a score
  if len(password) < 8:
    score = 1
  elif len(password) >= 8 and len(password) <= 12:
    score = 2
  elif len(password) > 12:
    score = 3
  
  # Check the complexity and uniqueness of the password, and adjust the score accordingly
  if not pattern.match(password):
    score -= 1
  if password in common_passwords:
    score -= 1
  
  # Return the password strength score in the response body
  return jsonify({'score': score})

# Run the app
if __name__ == '__main__':
  app.run()
