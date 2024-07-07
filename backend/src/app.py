import os
import requests
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def home_page():
    return "<p>Hello, World!</p>"

# @app.route("/get_new_photo", methods=['GET'])
# def switch_photo():
#     google_drive_url = "https://drive.google.com/drive/folders/1njJBSXpL0gikMMWmk50I6OAzJruD7JNi?usp=drive_link"
#     try:
#         file_stream = get_file(google_drive_url)
#         n = get_file_numbers(file_stream)
#         count = 0
#         if count == n:
#             count = 0
#         image = file_stream(count)
#         count += 1
#         image_url = get_url(image)
#         response = jsonify(message, image_url)
#         return response, 200
#     except Exception as e:
#         return e
    
@app.route('/photos')
def list_photos():
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile('../client_secret.json')

    try:
        gauth.LocalWebserverAuth()
    except Exception as e:
        print(f"An error occurred: {e}")

    drive = GoogleDrive(gauth)
    folder_id = "1njJBSXpL0gikMMWmk50I6OAzJruD7JNi"
    cache_dir = 'photos'

    # Ensure cache directory exists
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    photos = []
    
    for file in file_list:
        file_id = file['id']
        file_title = file['title']
        file_path = os.path.join(cache_dir, file_title)

        # Check if the file is already cached
        if not os.path.exists(file_path):
            # Download and cache the file
            file.GetContentFile(file_path)

        photos.append({'title': file_title, 'url': f'/photo/{file_title}'})
    return jsonify(photos)

    
if __name__ == "__main__":
    app.run(debug=True)