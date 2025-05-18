from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(min_lth, use_number=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if use_number:
        characters += digits
    if use_special:
        characters += special

    pwd = []

    if use_number:
        pwd.append(random.choice(digits))
    if use_special:
        pwd.append(random.choice(special))

    while len(pwd) < min_lth:
        pwd.append(random.choice(characters))

    random.shuffle(pwd)
    return ''.join(pwd)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password', methods=['POST'])
def generate():
    data = request.get_json()
    min_length = int(data.get('length', 8))
    use_number = data.get('number', True)
    use_special = data.get('special', True)
    password = generate_password(min_length, use_number, use_special)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
