from flask import Flask

# Create a Flask web app
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'LOVE, BITCHES'

# Run the app on IP 0.0.0.0 (exposed) and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

