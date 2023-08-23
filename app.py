from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('table.html')

@app.route('/test', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        txtout = request.form['txtout']
        return 'Получили POST с данными: ' + txtout

    else:
        return 'Допускаем только POST, а получили GET'

if __name__ == '__main__':
    app.run()