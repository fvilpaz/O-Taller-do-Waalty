from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Variable global para almacenar citas
appointments = []

@app.route('/')
def index():
    return render_template('index.html', appointments=appointments)

@app.route('/submit', methods=['POST'])
def submit():
    service = request.form.get('service')
    date = request.form.get('date')
    time = request.form.get('time')
    payment = request.form.get('payment')

    # Guardar la cita
    appointments.append({'service': service, 'date': date, 'time': time, 'payment': payment})

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
