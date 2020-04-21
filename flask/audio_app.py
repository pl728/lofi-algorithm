from flask import Flask, render_template

app = Flask(__name__, static_folder='lofai',
            static_url_path='/lofai')


@app.route("/")
def hello():
    return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)
