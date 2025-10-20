# entropy_unicity.py
import math
import json
import os
from datetime import timedelta

def entropy(keyspace_size):
    return math.log2(keyspace_size)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

def brute_force_time_days(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

def human_time_days(days):
    years = int(days // 365)
    days_r = days - years*365
    if years > 0:
        return f"{years} years, {days_r:.2f} days"
    else:
        return f"{days:.2f} days"

results = {}

# Keyspaces to evaluate
keyspaces = {
    'Caesar (26)': 26,
    'AES-128 (2^128)': 2**128,
    'AES-256 (2^256)': 2**256,
    'Custom 40-bit': 2**40
}

attempts = [1e6, 1e9, 1e12]  # attempts per second - example machines

for name, ks in keyspaces.items():
    HK = entropy(ks)
    U = unicity_distance(HK)
    times = {int(a): {'days': brute_force_time_days(ks, a), 'human': human_time_days(brute_force_time_days(ks, a))} for a in attempts}
    results[name] = {
        'keyspace': ks,
        'entropy_bits': HK,
        'unicity_distance_chars': U,
        'brute_force_estimates': times
    }

# Euler theorem / modular inverse example
# phi(26) = 12, inverse of 7 mod 26 is 15 since 7*15 % 26 == 1
mod_example = {
    'modulus': 26,
    'phi(26)': 12,
    'a': 7,
    'inverse_of_a_mod_26': pow(7, -1, 26),
    'check': (7 * pow(7, -1, 26)) % 26
}

# Save outputs
outdir = os.path.dirname(__file__)
outfile = os.path.join(outdir, '..', 'screenshots', 'hasil_output.txt')
os.makedirs(os.path.join(outdir, '..', 'screenshots'), exist_ok=True)

with open(outfile, 'w') as f:
    f.write('=== Entropy, Unicity Distance & Brute Force Estimates\n')
    f.write(json.dumps(results, indent=2, default=str))
    f.write('\n\n=== Modular inverse example\n')
    f.write(json.dumps(mod_example, indent=2))

# Print to stdout for user
print('=== Entropy, Unicity Distance & Brute Force Estimates')
print(json.dumps(results, indent=2, default=str))
print('\n=== Modular inverse example')
print(json.dumps(mod_example, indent=2))

# Additionally create a simple CSV summary
import csv
csvfile = os.path.join(outdir, '..', 'screenshots', 'summary.csv')
with open(csvfile, 'w', newline='') as csvf:
    writer = csv.writer(csvf)
    writer.writerow(['cipher','keyspace','entropy_bits','unicity_distance_chars'])
    for k,v in results.items():
        writer.writerow([k, v['keyspace'], f"{v['entropy_bits']:.4f}", f"{v['unicity_distance_chars']:.4f}"])
