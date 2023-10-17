import requests

data = {
    'x': 32  # Example value of x
}
response = requests.post('http://localhost:8000/calculate_pi', json=data)
result = response.json()
pi_x = result['pi_x']
print(f"pi({data['x']}) = {pi_x}")