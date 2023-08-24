from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = str(eval(expression))
    except Exception as e:
        result = 'Error'
    return render_template('calculator.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)
