from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-9.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-27.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-13.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-28.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-21.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-27.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-4.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-16.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-20.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-30.gif"
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-22.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-5.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-26.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-1.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-19.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-7.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-17.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-11.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-2.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-3.gif"
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-9.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-8.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-10.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-12.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-14.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-18.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-23.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-24.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-25.gif",
    "https://acegif.com/wp-content/uploads/gifs/happy-cat-29.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
