from flask import Flask, render_template, request
app = Flask(__name__)

# Dictionary containing energy usage (in watts)
appliance_energy = {
    "Fridge": 500,  
    "Washing Machine": 1000,  
    "Television": 100,  
    "Air Conditioner": 3000,  
    "Microwave": 600,  
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    appliance = request.form['appliance']
    hours = float(request.form['hours'])
   

    # Calculate energy consumption in kWh
    energy_used = (appliance_energy[appliance] * hours) / 1000  # Convert to kWh

    # Month estimate at 30 days
    month=energy_used*30

    # Year estimate at 365 days
    annual=energy_used*365

    return render_template('index.html', appliance=appliance, hours=hours, energy_used=energy_used, month=month, annual=annual)

if __name__ == '__main__':
    app.run(debug=True)
