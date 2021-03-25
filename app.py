from flask import Flask, render_template
import json
import argparse


app = Flask(__name__)

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--limit", type=int, default=4,
	help="Please enter the maximum number of people")
args = vars(ap.parse_args())

# 定員
limit = args["limit"]

@app.route('/')
def get():
    try:
        # with open('tmp/persons.json') as f:
        with open('tmp/persons.json') as f:
            load = json.load(f)

            count = load['count']
            if count >= limit:
                return render_template('danger.html', count=count ,limit=limit)
            elif count >= (limit/2):
                return render_template('caution.html', count=count ,limit=limit)
            else:
                return render_template('safety.html', count=count ,limit=limit)

    except FileNotFoundError:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)