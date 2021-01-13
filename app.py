from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def get():
    try:
        with open('/tmp/mouses.json') as f:
            load = json.load(f)

            count = load['count']
            return render_template('get.html', count=count)
    except FileNotFoundError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)