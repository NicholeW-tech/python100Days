from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"



random_num = random.randint(0,9)
print(random_num)


@app.route('/URL/<int:num>')
def check_num(num):
    if random_num == num:
        return "<h1 style='color: green; text-align: center'>You found me!!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif random_num > num:
        return "<h1 style='color: blue; text-align: center'>You're too low!!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif random_num < num:
        return "<h1 style='color: red; text-align: center'>You're too high!!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"




if __name__ == "__main__":
    app.run(debug=True)

