from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Function to read credentials from a file
def get_credentials_from_file():
    credentials = {}
    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                if line.strip():  # Make sure it's not an empty line
                    username, password = line.strip().split(" ")
                    credentials[username] = password
    except Exception as e:
        print(f"Error reading credentials file: {e}")
    return credentials

# Route to serve the HTML page (client)
@app.route('/')
def index():
    return render_template('index.html')

# Route to run a command
@app.route('/run_command', methods=['POST', 'OPTIONS'])
def run_command():
    # Get the password and command from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')
    command = data.get('command')
    
    # Get credentials from the file
    credentials = get_credentials_from_file()

    # Check if the username and password are correct
    if username != credentials.get('username') or password != credentials.get('password'):
        return jsonify({"error": "Invalid username or password"}), 403

    # Check if command is provided
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        # Run the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({"output": result.stdout}), 200
        else:
            return jsonify({"error": result.stderr}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

