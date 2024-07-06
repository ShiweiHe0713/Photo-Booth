from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p>Hello, World!</p>"

@app.route("/get_new_photo")
def switch_photo():
    google_drive_url = "https://drive.google.com/drive/folders/1njJBSXpL0gikMMWmk50I6OAzJruD7JNi?usp=drive_link"
    try:
        file_stream = get_file(google_drive_url)
        n = get_file_numbers(file_stream)
        count = 0
        if count == n:
            count = 0
        image = file_stream(count)
        count += 1
        image_url = get_url(image)
        response = jsonify(message, image_url)
        return response, 200
    except Exception as e:
        return e, 500

