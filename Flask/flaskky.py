from flask import Flask


app = Flask(__name__)


def make_bold(funtion):
    def indent():
        return f"<b>{funtion()}</b>"
    return indent

def make_underline(funtion):
    def indent():
        return f"<u>{funtion()}</u>"
    return indent


@app.route('/')
def home():
    return "<h1>Hello, Aryan!</h1>\
        <p>Welcome to your Flask app.</p>"

@app.route('/bye')
@make_bold
@make_underline
def say_bye():
    return "Goodbye! Don't forget to hydrate."

if __name__ == "__main__":

    app.run()