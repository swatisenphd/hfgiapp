from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regform')
def index():
    return render_template('regform.html')

@app.route('/test')
def test():
    return 'This is a test'

if __name__ == '__main__':
    app.run()



