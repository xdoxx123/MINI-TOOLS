import requests

def switchstatusto(usetoken,status):
    

# Replace with your user token (NOT a bot token)
    user_token = "YOUR_USER_TOKEN"

    # URL to change your user settings (status)
    url = "https://discord.com/api/v9/users/@me/settings"

    # Headers for authentication
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Content-Type": "application/json"
    }

    # Data to change the status
    data = {
        "status": "online",  # Change to "idle", "dnd", or "invisible" if desired
        "custom_status": {
            "text": "Coding a bot!"  # Optional: Add a custom status message
        }
    }

    # Send the request to change status
    response = requests.patch(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Status updated successfully.")
    else:
        print(f"Failed to update status: {response.status_code}")
