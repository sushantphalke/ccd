import math
# import merge_chunks
with open('master_mini.txt', 'r') as file:
    lines = file.readlines()[3:]
    print(len(lines))

chunk_lines = int(len(lines)/32)

# for i in range (len(lines)):
#     text_to_write=lines[i]
#     x=i//chunk_lines
#     with open(f"output_32_{x+1}.txt", "a") as file:
#         file.write(text_to_write)
k=0
for i in range(1,33):
    for j in range(chunk_lines):
        text_to_write = lines[k]
        k+=1
        with open(f"32_instances/output_32_{i}.txt", "a") as file:
            file.write(text_to_write)
    

# merge_chunks.merge_chunks(2)
# merge_chunks.merge_chunks(4)
# merge_chunks.merge_chunks(8)