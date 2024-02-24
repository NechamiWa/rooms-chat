import json
import os.path
from flask import Flask, url_for, redirect, request, jsonify
from datetime import datetime

app = Flask(__name__)

CHAT_DATA_FILE = 'chat-data/chat-data.json'


def load_chat_data():
    if os.path.exists(CHAT_DATA_FILE):
        with open(CHAT_DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        with open(CHAT_DATA_FILE, 'w') as file:
            json.dump([], file)
        return []


def get_room_messages(room_id: int):
    try:
        room_id = int(room_id)
    except ValueError:
        return -1, []
    data = load_chat_data()
    is_exist = False
    if data != []:
        for index, room in enumerate(data):
            if room["id"] == room_id:
                is_exist = True
                return index, room["messages"]
    if not is_exist:
        return -1, "room is not exist"
    return -2, "no rooms data"


def add_room_message(room: int, message: dict):
    data = load_chat_data()
    index, messages = get_room_messages(int(room))
    if index >= 0:
        data[index]["messages"].append(message)
    else:
        data.append({'id': int(room), 'messages': [message]})
    with open(CHAT_DATA_FILE, 'w') as file:
        json.dump(data, file)


@app.route('/', methods=['GET'])
def index():
    with open('index.html', 'r') as file:
        return file.read()


@app.route('/<room>', methods=['GET'])
def room_index(room):
    # return app.redirect(url_for(index))
    with open('index.html', 'r') as file:
        return file.read()


@app.route('/api/chat/<room>', methods=['GET'])
def get_room_chat(room: int):
    index, room_messages = get_room_messages(room)
    if index >= 0:
        formatted_messages = ""
        for message in room_messages:
            formatted_messages += f"{message['date']} {message['name']}:{message['message']} \n"
        return formatted_messages
    else:
        return "Room not found", 404


@app.route('/api/chat/<room>', methods=['POST'])
def add_chat_message(room: str):
    username = request.form.get('username')
    msg = request.form.get('msg')
    if not (username and msg):
        return jsonify({'error': 'Username and message are required'}), 400

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("[%Y-%m-%d %H:%M:%S]")
    date = formatted_datetime
    message = {
        "date": date,
        "name": username,
        "message": msg
    }
    if add_room_message(room, message):
        get_room_messages(room)
        return "message added", 200
    else:
        get_room_messages(room)
        return 'Room created and message added', 201


if __name__ == "__main__":
    app.run(host="0.0.0.0")
