from flask import Flask, jsonify
import pyotp

app = Flask(__name__)

# Generate an OTP secret
secret_key = pyotp.random_base32()

# Initialize the TOTP object
totp = pyotp.TOTP(secret_key)

@app.route('/generate', methods=['GET'])
def generate_otp():
    otp = totp.now()
    return jsonify({'otp': otp})

if __name__ == '__main__':
    app.run(port=5000)