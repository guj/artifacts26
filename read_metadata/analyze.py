#!/usr/bin/env python3
"""
Compute mean +/- stdev of bpls -l metadata inspection times
from out_default and out_flatten, reproducing Table II of the paper.
"""
import re
import statistics

def parse_file(path):
    data = {}  # node_count -> list of elapsed times (seconds)
    with open(path) as f:
        for line in f:
            m = re.match(
                r'Nodes:\s*(\d+).*Run 1:\s*([\d.]+)s.*Run 2:\s*([\d.]+)s.*Run 3:\s*([\d.]+)s',
                line)
            if m:
                n = int(m.group(1))
                times = [float(m.group(i)) for i in range(2, 5)]
                data.setdefault(n, []).extend(times)
    return data

default   = parse_file("out_default")
flattened = parse_file("out_flatten")

print(f"{'N':>4}  {'Snapshot':>10}  {'Default mean':>14}  {'Default stdev':>14}  "
      f"{'Flatten mean':>14}  {'Flatten stdev':>14}  {'n trials':>8}")
print("-" * 90)

sizes = {8: "2.0 GB", 16: "7.6 GB", 32: "15.3 GB"}

for n in sorted(default):
    d = default[n]
    f = flattened[n]
    print(f"{n:>4}  {sizes.get(n,''):>10}  "
          f"{statistics.mean(d):>14.4f}  {statistics.stdev(d):>14.4f}  "
          f"{statistics.mean(f):>14.4f}  {statistics.stdev(f):>14.4f}  "
          f"{len(d):>8}")
