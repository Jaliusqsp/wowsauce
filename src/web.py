from flask import Flask, render_template

app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return 'hot sauce'


if __name__ == '__main__':
    app.run()
