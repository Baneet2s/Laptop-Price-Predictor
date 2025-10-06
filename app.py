from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the pickled model and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main page with form inputs."""
    return render_template('index.html',
                           companies=sorted(df['Company'].unique()),
                           types=sorted(df['TypeName'].unique()),
                           rams=sorted(df['Ram'].unique()),
                           weights=df['Weight'].unique(), # Weight may not need sorting
                           touchscreens=sorted(df['Touchscreen'].unique()),
                           ips_options=sorted(df['Ips'].unique()),
                           cpu_brands=sorted(df['Cpu brand'].unique()),
                           hdds=sorted(df['HDD'].unique()),
                           ssds=sorted(df['SSD'].unique()),
                           gpu_brands=sorted(df['Gpu brand'].unique()),
                           os_options=sorted(df['os'].unique())
                           )

@app.route('/predict', methods=['POST'])
def predict():
    """Handles the prediction request from the form."""
    try:
        # Get data from form
        company = request.form.get('company')
        laptop_type = request.form.get('type')
        ram = int(request.form.get('ram'))
        weight = float(request.form.get('weight'))
        touchscreen = int(request.form.get('touchscreen'))
        ips = int(request.form.get('ips'))
        ppi = float(request.form.get('ppi'))
        cpu_brand = request.form.get('cpu_brand')
        hdd = int(request.form.get('hdd'))
        ssd = int(request.form.get('ssd'))
        gpu_brand = request.form.get('gpu_brand')
        os = request.form.get('os')

        # Create input array for prediction
        query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu_brand, hdd, ssd, gpu_brand, os], dtype=object)
        query = query.reshape(1, 12)

        # Make prediction and format the result
        prediction = pipe.predict(query)
        result = f"₹ {int(np.exp(prediction[0])):,}"

        return render_template('index.html', result=result,
                               companies=sorted(df['Company'].unique()),
                               types=sorted(df['TypeName'].unique()),
                               rams=sorted(df['Ram'].unique()),
                               weights=df['Weight'].unique(),
                               touchscreens=sorted(df['Touchscreen'].unique()),
                               ips_options=sorted(df['Ips'].unique()),
                               cpu_brands=sorted(df['Cpu brand'].unique()),
                               hdds=sorted(df['HDD'].unique()),
                               ssds=sorted(df['SSD'].unique()),
                               gpu_brands=sorted(df['Gpu brand'].unique()),
                               os_options=sorted(df['os'].unique())
                               )

    except Exception as e:
        error_message = f"Error during prediction: {str(e)}"
        return render_template('index.html', result=error_message,
                               companies=sorted(df['Company'].unique()),
                               types=sorted(df['TypeName'].unique()),
                               rams=sorted(df['Ram'].unique()),
                               weights=df['Weight'].unique(),
                               touchscreens=sorted(df['Touchscreen'].unique()),
                               ips_options=sorted(df['Ips'].unique()),
                               cpu_brands=sorted(df['Cpu brand'].unique()),
                               hdds=sorted(df['HDD'].unique()),
                               ssds=sorted(df['SSD'].unique()),
                               gpu_brands=sorted(df['Gpu brand'].unique()),
                               os_options=sorted(df['os'].unique())
                               )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)