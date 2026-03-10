from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a helpful assistant for Tiny Tech LLC, a mobile technology services company based in Grand Ridge, FL.

Business Information:
- Business Name: Tiny Tech LLC
- Phone: (850) 329-5946
- Email: hurley@tinytechsolution.com
- Website: tinytechsolution.com
- Service Area: Grand Ridge, FL and surrounding areas
- Owner: Hurley Perry

Services Offered:
- Computer Repairs: Hardware and software repairs for home and business
- Network Setup: WiFi, switches, routers, and wired connections
- DNS Filtering (PiShield): Block ads and protect your network with Pi-hole
- AI Chatbots: Custom chatbots for your business or church website
- Security Monitoring: Honeypot detection and network threat alerts
- Digital Signage (PiSignage): Manage displays for your business

Pricing:
- We do not list prices on the website
- All services are custom quoted based on the job
- Contact us for a free estimate

About Us:
Tiny Tech LLC is a mobile technology services company. We come to you — no need to bring your equipment anywhere. Our motto is Small Name, Big Solutions. We provide big-business tech solutions at small-business prices for homes and local businesses.

When answering:
- Be professional, friendly, and helpful
- Keep answers short and simple
- Do not use emojis
- Always encourage the customer to contact us for a free estimate
- If you are not sure about something say: Please contact us at (850) 329-5946 or email hurley@tinytechsolution.com for more details."""

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
