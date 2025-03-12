from flask import Flask, Response
import subprocess

app = Flask(__name__)

def stream_batch():
    process = subprocess.Popen(["script.bat"], stdout=subprocess.PIPE, text=True)
    for line in iter(process.stdout.readline, ''):
        yield line

@app.route('/')
def run_batch():
    return Response(stream_batch(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
