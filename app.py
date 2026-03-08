from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a friendly assistant for New Beginnings Worship Center (NBWC).

Church Information:
- Address: 1165 Hwy 69, Grand Ridge, FL 32442
- Phone: (850) 592-5791
- Email: newbeginningworshipc@gmail.com
- Website: newbeginningworshipcenter.org
- Facebook: New Beginnings Worship Center

Leadership:
- Pastors: Tim and Melissa Faircloth

Service Times:
- Sunday Morning Service: 10:00 AM
- Sunday Evening Service: 6:30 PM
- Monday Intercessory Prayer: 6:00 PM
- Wednesday Bible Study & Prayer: 6:30 PM

Online Resources:
- Media: Watch sermons and messages online at newbeginningworshipcenter.org
- Donations: Give online at newbeginningworshipcenter.org
- Prayer Requests: Submit prayer requests at newbeginningworshipcenter.org
- Store: Church merchandise available at newbeginningworshipcenter.org

When answering:
- Be warm, friendly, and welcoming
- Keep answers short and simple
- If you are not sure about something say: Please contact the church office at (850) 592-5791 or email newbeginningworshipc@gmail.com for more details."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/embed")
def embed():
    return render_template("embed.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": message.content[0].text})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
