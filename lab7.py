from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/<username>')
def about(username):
    return render_template('about.html', username=username)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('result.html', name=name, email=email, message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

