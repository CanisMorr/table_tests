from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('table.html')

@app.route('/test', methods=['GET', 'POST'])
def testfunc():
    if request.method == 'POST':
        #Тут мы получили POST, в который передались какие-то данные. Ответ дадим статический
        return '{"id":777,"name":"Новое Имя","age":"777","col":"Розовый","dob":"22/05/1982"}'

    else:
        return 'Допускаем только POST, а получили GET'

if __name__ == '__main__':
    app.run()