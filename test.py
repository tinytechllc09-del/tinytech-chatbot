import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "stream": False,
        "messages": [
            {"role": "system", "content": "You are a friendly assistant for New Beginnings Worship Center (NBWC) in Marianna FL. Service times: Sunday 10:00 AM, Wednesday 6:00 PM. Location: Marianna FL. For anything you are not sure about say: Please contact the church office directly for more details."},
            {"role": "user", "content": "How much does it cost to join the church?"}
        ]
    }
)

data = response.json()
print(data["message"]["content"])
