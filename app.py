from flask import Flask

app = Flask(__name__)    

@app.route('/')
def index():
    return "Welcome to the AI Portfolio App!"

if __name__ == '__main__':
    app.run(debug=True)


