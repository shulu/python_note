import hashlib
import struct

NODE_COUNT = 100
DATA_ID_COUNT = 10000000

node_counts = [0] * NODE_COUNT
for data_id in range(DATA_ID_COUNT):
    data_id = str(data_id)
    # This just pulls part of the hash out as an integer
    hsh = struct.unpack_from('>I', hashlib.md5(data_id).digest())[0]
    node_id = hsh % NODE_COUNT
    node_counts[node_id] += 1
desired_count = DATA_ID_COUNT / NODE_COUNT
print('%d: Desired data ids per node' % desired_count)
max_count = max(node_counts)
over = 100.0 * (max_count - desired_count) / desired_count
print('%d: Most data ids on one node, %.02f%% over' % \
    (max_count, over))
min_count = min(node_counts)
under = 100.0 * (desired_count - min_count) / desired_count
print('%d: Least data ids on one node, %.02f%% under' % \
    (min_count, under))

#100000: Desired data ids per node
#100695: Most data ids on one node, 0.69% over
#99073: Least data ids on one node, 0.93% under