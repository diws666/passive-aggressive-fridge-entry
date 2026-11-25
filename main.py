import os

# Verified count: 110 characters (110 UTF-8 bytes).
LINE = "Note from your fridge: I kept the leftovers safe. I also ate the last slice of cake. It was for your own good."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output/entry.txt')

# The default names the output file itself; a set MAKEFUN_OUTPUT_DIR is a
# directory to write entry.txt into.
if output_dir == '/output/entry.txt' or os.path.splitext(output_dir)[1]:
    output_path = output_dir
else:
    output_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE))
