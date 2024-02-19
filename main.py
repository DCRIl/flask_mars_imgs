from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def gallery():
    images = [
        'mars1.jpg',
        'mars2.jpg',
        'mars3.jpg'
    ]
    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
