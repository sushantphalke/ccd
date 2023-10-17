def calculate_pi_x(x, data_file):
    c_x = None
    c_pi_x = None
    with open(data_file, 'r') as file:
        file = file.readlines()[3:]
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                data_x, pi_x, _ = map(float, parts)
                if data_x <= x:
                    c_x = data_x
                    c_pi_x = pi_x

    if c_x is not None:
        return c_x, c_pi_x
    else:
        return None, None

data_file = 'master_mini.txt'

x = 20

c_x, c_pi_x = calculate_pi_x(x, data_file)

if c_x is not None:
    print(f"π({c_x}) = {int(c_pi_x):,} (primes less than or equal to {c_x})")
else:
    print(f"No data found for x = {x}")
