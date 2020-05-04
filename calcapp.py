'''
This app will display a form with two fields to allow the user to enter two numbers and get the sum 
of those numbers. This application is unit tested!
'''

from flask import Flask, render_template, request
import calculator

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def calc():
    '''
    Controller code for the main webesite application
    '''
    if request.method == 'POST':
        calc_obj = calculator.Calculator(request.form['first_number'],
                                           request.form['second_number'])
        calc_json = calc_obj.return_json()

        return render_template('calculator.html', results=calc_json)
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
