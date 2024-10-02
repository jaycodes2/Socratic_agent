from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import google.generativeai as genai
from config import Config
from bson import ObjectId

# Configure the API key
api_key = "AIzaSyC0Lwyqsoci7wytEeiqtZ5UgXEG8tZNeE4"
genai.configure(api_key=api_key)

# Set up generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="tunedModels/dsasocraticexamples-lu4fbkyf4xks",
    generation_config=generation_config,
)

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)  # Ensure you have your MongoDB URI in the Config class
mongo = PyMongo(app)
CORS(app)
try:
    mongo.init_app(app)
    print("MongoDB connected successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
# Store active chat session
def create_chat_session():
    return model.start_chat(history=[])

# Start the first chat session
chat_session = create_chat_session()

# API to handle chat messages
current_conversation_id = None

@app.route('/api/chat', methods=['POST'])
def chat():
    global chat_session, current_conversation_id
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        # AI response generation
        response = chat_session.send_message(user_message)

        # Use the existing conversation ID or generate a new one if required
        if not current_conversation_id:
            existing_chat = mongo.db.conversations.find_one({"_id": "current_session"})
            if existing_chat:
                current_conversation_id = existing_chat["_id"]
            else:
                # Create a new conversation ID
                current_conversation_id = str(ObjectId())

        # Append the chat to the current conversation
        mongo.db.conversations.update_one(
            {"_id": current_conversation_id},
            {
                "$push": {"conversation": {"user": user_message, "ai": response.text}}
            },
            upsert=True  # Create if it doesn't exist
        )

        return jsonify({'response': response.text}), 200

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while processing the chat.'}), 500

@app.route('/api/conversations', methods=['GET'])
def get_conversations():
    try:
        conversations = mongo.db.conversations.find({}, {'conversation': 1})
        chat_list = []
        for chat in conversations:
            chat_list.append({
                "_id": str(chat["_id"]),
                "conversation": chat.get("conversation", [])
            })
        return jsonify(chat_list), 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'An error occurred while retrieving chats.'}), 500

@app.route('/api/conversation/<chatId>', methods=['GET'])
def get_conversation_by_id(chatId):
    try:
          # Ensure the ObjectId is stripped of whitespace
        conversations = mongo.db.conversations.find({"_id": str(chatId)})  # This returns a cursor

        # Convert cursor to a list and check if there are any results
        conversation_list = list(conversations)
        print(f"Chat ID: {chatId}, Conversation List: {conversation_list}")
        if conversation_list:  # If there's at least one document
            return jsonify({
                "conversation": conversation_list[0].get("conversation", [])
            }), 200
        else:
            return jsonify({"error": "Conversation not found"}), 404
    except Exception as e:
        print(f"Error occurred while fetching chat: {e}")  # Log any errors
        return jsonify({"error": "An error occurred while fetching the conversation."}), 500


@app.route('/api/start_new_conversation', methods=['POST'])
def start_new_conversation():
    global chat_session, current_conversation_id
    chat_session = create_chat_session()

    # Generate a new conversation ID for the upcoming conversation
    current_conversation_id = str(ObjectId())  # Don't store until the first message
    return jsonify({"_id": current_conversation_id, "message": "New conversation started"}), 200

@app.route('/api/conversation/<chatId>', methods=['DELETE'])
def delete_conversation(chatId):
    try:
        result = mongo.db.conversations.delete_one({"_id": str(chatId)})
        if result.deleted_count > 0:
            return jsonify({"message": "Conversation deleted successfully"}), 200
        else:
            return jsonify({"error": "Conversation not found"}), 404
    except Exception as e:
        print(f"Error occurred while deleting chat: {e}")
        return jsonify({"error": "An error occurred while deleting the conversation."}), 500

if __name__ == '__main__':
    app.run(debug=True)
