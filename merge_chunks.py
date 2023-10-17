import math
def merge_chunks(chunks):
    m=int(32/chunks)
    ini=int(0)
    for i in range (0,chunks):
        for j in range(ini,m):
            with open(f"{chunks}_instances/output_{chunks}_{i+1}.txt", "a") as f:
                with open(f"32_instances/output_32_{j+1}.txt", "r") as file:
                    lines = file.readlines()
                    for each in lines:
                        f.write(each)
        ini=m
        m+=int(32/chunks)
        
merge_chunks(2)
merge_chunks(4)
merge_chunks(8)
merge_chunks(16)