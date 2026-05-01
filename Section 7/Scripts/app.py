from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def Index():
    print("Hello request")
    time.sleep(10)
    print("Done")
    return "Hello From the service..."





@app.route('/rec', methods=['POST'])
def Rec():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON received"}), 400
    
    print(data)
    return jsonify({
        "message": "Data received successfully",
        "received": data
    }), 200

if __name__ == '__main__':
    app.run(debug=True)