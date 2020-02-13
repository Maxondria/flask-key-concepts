from app import app


@app.route('/')
def index():
    return 'Hello, Young man'

