from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def proff(prof):
    return render_template('lol.html', prof=prof, img1=url_for('static', filename='img/r.png'),
                           img2=url_for('static', filename='img/riana.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
