
from datetime import datetime
import matplotlib.pyplot as plt
total_serial_time_start = datetime.now()
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
    
time_diff_instances= []   
insta_ary=[2,4,8,16,32] 
x = 26846287
for insta in insta_ary:
    no_of_instances = insta
    start_time = datetime.now()
    for i in range(no_of_instances,0,-1):
        with open(f'{no_of_instances}_instances/output_{no_of_instances}_{i}.txt',"r") as f:
            lines=f.readline()
            s = lines.split()
        if(x>float(s[0])):
            print("output found from : "+str(i)+" th chunk")
            data_file = f'{no_of_instances}_instances/output_{no_of_instances}_{i}.txt'
            break

    closest_x, closest_pi_x = calculate_pi_x(x, data_file)
    end_time = datetime.now()
    time_difference = (end_time - start_time).total_seconds()
    time_diff_instances.append(time_difference)

if closest_x is not None:
    # with open("submission1.txt",'a'):
    print(f"π({closest_x}) = {int(closest_pi_x):,} (primes less than or equal to {closest_x})")
else:
    print(f"No data found for x = {x}")

    

total_serial_time_end = datetime.now()
total_time = (total_serial_time_end-total_serial_time_start).total_seconds()
total_serial_time = total_time
for each in time_diff_instances:
    total_serial_time = total_serial_time-each
total_serial_time+=time_diff_instances[0]*2

print(total_serial_time)


amdahl_speedup = []
amdahl_efficiency = []
gustafson_speedup=[]
gustafson_efficiency=[]

for each in insta_ary:
    P = total_serial_time
    N = each
    am_sp = 1 /((1-P)+(P/N))
    amdahl_speedup.append(am_sp)
    gus_sp = N+(1-N)*(total_serial_time+P)
    gustafson_speedup.append(gus_sp)
    am_eff = am_sp/N
    amdahl_efficiency.append(am_eff)
    gus_eff = gus_sp/N
    gustafson_efficiency.append(gus_eff)


print("| amdahl_speedup | gustafson_speedup | amdahl_efficiency[i] | gustafson_efficiency |")
for i in range(0,5):
    print("|",amdahl_speedup[i],"|",gustafson_speedup[i],"|",amdahl_efficiency[i],"|",gustafson_efficiency[i],"|")




# from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/calculate_pi', methods=['POST'])
# def calculate_pi_route():
#     data = request.get_json()
#     x = data['x']
#     pi_x = int(closest_x)
#     response = {
#         'pi_x': pi_x
#     }
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
plt_data = gustafson_speedup
plt.plot(plt_data)
plt.xlabel('instances ')
plt.ylabel('time scale')
plt.title('gustafsons speedup')
plt.show()

plt_data = gustafson_speedup
labels =[2,4,8,16,32]
plt.bar(labels, plt_data)
plt.xlabel('instances ')
plt.ylabel('time scale')
plt.title('gustafsons speedup')
plt.show()

plt_data = gustafson_efficiency
labels =[2,4,8,16,32]
plt.bar(labels, plt_data)
plt.xlabel('instances ')
plt.ylabel('time scale(inversly proportional)')
plt.title('gustafsons efficiency')
plt.show()