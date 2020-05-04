'''
This app will display a form with two fields to allow the user to enter two numbers and get the sum 
of those numbers. 
'''

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def calc():
    '''
    Controller code for the main webesite application
    '''
    if request.method == 'POST':
        pass
    else:
        return render_template('calculator.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
