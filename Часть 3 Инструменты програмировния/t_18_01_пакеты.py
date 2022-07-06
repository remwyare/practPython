#pip3.exe install Flask==0.11.1


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Привет, мир!"

app.run(port='8000')

#print(__name__)
