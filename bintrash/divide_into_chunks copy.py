def calculate_pi_x(x, data_file):
    closest_x = None
    closest_pi_x = None
    with open(data_file, 'r') as file:
        file = file.readlines()[3:]
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                data_x, pi_x, _ = map(float, parts)
                if data_x <= x:
                    closest_x = data_x
                    closest_pi_x = pi_x

    if closest_x is not None:
        return closest_x, closest_pi_x
    else:
        return None, None
    
x = 32

data_file = 'master_mini.txt'
closest_x, closest_pi_x = calculate_pi_x(x, data_file)

if closest_x is not None:
    print(f"π({closest_x}) = {int(closest_pi_x):,} (primes less than or equal to {closest_x})")
else:
    print(f"No data found for x = {x}")
