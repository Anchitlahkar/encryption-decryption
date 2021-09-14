from flask import Flask, jsonify, request
from encrypt import Encrypt
from decrypt import Decrypt

app = Flask(__name__)


@app.route('/encrypt-text', methods=['POST'])
def encryptfile():
    text = request.args.get("text")
    encryption = Encrypt(text)

    return jsonify({
        'data': encryption
    }, 200)


@app.route('/decrypt-text', methods=["POST"])
def decryptFile():
    text = request.args.get("text")
    print(type(text))
    print(text)
    decryption = Decrypt(text)

    return jsonify({
        'data': decryption
    }, 200)


if __name__ == '__main__':
    app.run()
