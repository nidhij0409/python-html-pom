import sys
from pathlib import Path
p = Path(sys.argv[1])
data = p.read_bytes()
lines = data.splitlines()
for i,l in enumerate(lines[:200],1):
    print(f"{i}: {repr(l)}")
