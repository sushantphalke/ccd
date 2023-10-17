from flask import Flask, request, jsonify

app = Flask(__name__)

# Read the pre-computed π data from the text file into a dictionary
pi_data = {}
with open('master_mini.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 3:
            x, pi_x, delta_x = parts
            pi_data[float(x)] = float(pi_x) 

@app.route('/pi')
def calculate_pi():
    x = float(request.args.get('x'))
    if x in pi_data:
        result = pi_data[x]
    else:
        result = None  # Handle cases where x is not found in the data file
    
    return jsonify({'x': x, 'pi(x)': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  