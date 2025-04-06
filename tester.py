from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Basic Test</title></head>
    <body>
        <h1>Basic Test Site</h1>
        <p>This is the simplest Flask website.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()