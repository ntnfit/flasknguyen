from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "..hello Nguyen Thanh Nguyen"

@app.route('/user', methods=['GET'])
def getNextFromCurrent():
    current_temp = 0.0
    next_temp = 1.0
    return jsonify({'current': current_temp, 'next': next_temp})

@app.route('/iot/<float:temperature>', methods=['GET'])
def getNext(temperature):
    next_temp = temperature + 1.0
    return jsonify({'next':next_temp})

if __name__=='__main__':
    app.run(threaded=True, port=5000)

