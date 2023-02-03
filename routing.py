from flask import Flask
app = Flask(__name__)

@app.route('/data/appInfo/<name>', methods=['GET'])
def queryDataMessageByName(name):
    print("type(name) : ", type(name))
    return 'String => {}'.format(name)

@app.route('/')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

if __name__ == ("__main__"):
    app.run()