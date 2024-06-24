from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>File Transfer App</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f7f7f7;
      }
      .container {
        width: 50%;
        margin: 50px auto;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        padding: 20px;
        border-radius: 8px;
      }
      h1 {
        text-align: center;
        color: #333;
      }
      form {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
      }
      input[type="file"],
      input[type="text"] {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
        width: 100%;
        max-width: 300px;
      }
      input[type="submit"] {
        padding: 10px 20px;
        background-color: #007bff;
        border: none;
        color: white;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
      }
      input[type="submit"]:hover {
        background-color: #0056b3;
      }
      ul {
        list-style: none;
        padding: 0;
      }
      li {
        margin: 10px 0;
      }
      li a {
        text-decoration: none;
        color: #007bff;
      }
      li a:hover {
        text-decoration: underline;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Upload File</h1>
      <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
      </form>

      <h1>Uploaded Files</h1>
      <ul>
        {% for file in files %}
        <li><a href="{{ url_for('uploaded_file', filename=file) }}">{{ file }}</a></li>
        {% endfor %}
      </ul>

      <h1>Download File</h1>
      <form method="GET" action="/download">
        <input type="text" name="filename" placeholder="Enter filename to download">
        <input type="submit" value="Download">
      </form>
    </div>
  </body>
</html>
'''

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template_string(HTML_TEMPLATE, files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    if filename:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
