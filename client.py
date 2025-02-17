import requests

# The server URL (assuming server is running on localhost and port 5000)
SERVER_URL = "http://127.0.0.1:5000/run_command"

# The username, password, and command you want to run
username = "acosta"  # Change to your actual username
password = "acosta"  # Change to your actual password
command = "ls -l"  # You can change this to any command you want to run

# Prepare the data to send
data = {
    "username": username,
    "password": password,
    "command": command
}

# Send the request
response = requests.post(SERVER_URL, json=data)

# Handle the response
if response.status_code == 200:
    print("Command output:", response.json().get("output"))
else:
    print("Error:", response.json().get("error"))

