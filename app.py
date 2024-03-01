from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='Templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.root_path, filename)

if __name__ == '__main__':
   app.run()
