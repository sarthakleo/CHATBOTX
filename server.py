from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from bot import chat, new_conversation
from config import APP_TITLE, QUICK_QUESTIONS
import os

app = Flask(__name__)
CORS(app)

conversations = {}

@app.route('/', methods=['GET'])
def index():
    try:
        return send_file('index.html')
    except:
        return jsonify({
            "app": APP_TITLE,
            "status": "running",
            "message": "API Server Running",
            "endpoints": {
                "GET /": "Serve HTML UI or API info",
                "POST /chat": "Send a message",
                "GET /new": "Start new conversation",
                "GET /questions": "Get quick questions"
            }
        })

@app.route('/api/home', methods=['GET'])
def api_home():
    return jsonify({
        "app": APP_TITLE,
        "status": "running",
        "endpoints": {
            "GET /": "Serve HTML UI",
            "POST /chat": "Send a message",
            "GET /new": "Start new conversation",
            "GET /questions": "Get quick questions"
        }
    })

@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({"questions": QUICK_QUESTIONS})

@app.route('/new', methods=['GET'])
def new_conv():
    session_id = request.args.get('session_id', 'default')
    conversations[session_id] = new_conversation()
    return jsonify({
        "message": "New conversation started",
        "session_id": session_id
    })

@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        if session_id not in conversations:
            conversations[session_id] = new_conversation()
        
        history = conversations[session_id]
        
        reply = chat(history, user_message)
        
        return jsonify({
            "user_message": user_message,
            "bot_reply": reply,
            "session_id": session_id
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
