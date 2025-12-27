"""Flask example."""
import os
from http import HTTPStatus

from flask import Flask, request
from flask import jsonify

from werkzeug.utils import secure_filename
"""
Author: James Campbell
Date: Mon May 23 16:26:36 2016
Date Updated: 2 July 2019
What is this code: An example Flask connection
Why?: For me to remember later
"""

app = Flask(__name__)
ALLOWED_EXTENSIONS = ["zip", "gz", "bz2"]


def allowed_filename(filename: str) -> bool:
    """Define allowed file extensions."""
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def hello_world():
    """Hello world example."""
    return """\
        <!DOCTYPE html><head><title>Flask test</title></head>\
            <body style="font-family:monospace;">Hello, simply run\
            <pre style="color:blue;">curl -X POST localhost:6969/upload\
            -F file=@"assets/archive_name.tar.gz" -i</pre> to test from\
                 same folder you executed <pre style="color:blue;">python3\
                    flask-example.py</pre></body>
                    """


@app.route("/upload", methods=["POST"])
def upload_csv() -> str:
    """Upload CSV example."""
    if "file" not in request.files:
        return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "No file provided"}), 400
    
    submitted_file = request.files["file"]
    
    if not submitted_file or not submitted_file.filename:
        return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "No file selected"}), 400
    
    if not allowed_filename(submitted_file.filename):
        return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "File type not allowed"}), 400
    
    filename = secure_filename(submitted_file.filename)
    
    # Additional security check: ensure filename is not empty after sanitization
    if not filename:
        return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "Invalid filename"}), 400
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    upload_folder = os.path.abspath(os.path.join(basedir, app.config["UPLOAD_FOLDER"]))
    
    # Create directory with secure permissions if it doesn't exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder, mode=0o755, exist_ok=True)
    
    # Construct full path and verify it's within the upload directory (prevent path traversal)
    file_path = os.path.abspath(os.path.join(upload_folder, filename))
    
    if not file_path.startswith(upload_folder):
        return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "Invalid file path"}), 400
    
    # Limit file size (optional but recommended)
    # submitted_file.seek(0, os.SEEK_END)
    # file_size = submitted_file.tell()
    # submitted_file.seek(0)
    # if file_size > MAX_FILE_SIZE:
    #     return jsonify({"status": HTTPStatus.BAD_REQUEST, "message": "File too large"}), 400
    
    submitted_file.save(file_path)
    
    out = {
        "status": HTTPStatus.OK,
        "filename": filename,
        "message": f"{filename} saved successfully.",
    }
    return jsonify(out)


if __name__ == "__main__":
    app.config["UPLOAD_FOLDER"] = "flaskme/"
    # Debug mode disabled for security - use environment variable to enable in development
    debug_mode = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    app.run(port=6969, debug=debug_mode)

# curl -X POST localhost:6969/upload -F file=@"assets/archive_name.tar.gz" -i
