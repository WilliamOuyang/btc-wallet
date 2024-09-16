from bitcoin import random_key, privtopub, pubtoaddr




from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])

def generate_keys():
    private_key = random_key()
    public_key= privtopub(private_key)
    address = pubtoaddr(public_key)

    return jsonify({
            'private_key': private_key,
            # 'public_key': public_key,
            'address': address
    })

if __name__ == '__main__':
    app.run(debug=True)