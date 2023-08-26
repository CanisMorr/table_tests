from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('table.html')

@app.route('/test', methods=['GET', 'POST'])
def testfunc():
    if request.method == 'POST':
        #Тут мы получили POST, в который передались какие-то данные. Распарсим их у сунем в консоль
        print ('Got POST.')
        #print ('id: ' + request.form['id'] )
        #print('name: ' + request.form['name'])
        #print('age: ' + request.form['age'])
        #print('col: ' + request.form['col'])
        #print('dob: ' + request.form['dob'])
        print ('PERIODKEY: ' + request.form['PERIODKEY'])

        # И дадим ответ, сейчас статический
        otvet = '{"id":777,"name":"Новое Имя","age":"777","col":"Розовый","dob":"22/05/1982"}'
        return otvet

    else:
        return 'Допускаем только POST, а получили GET'

if __name__ == '__main__':
    app.run()