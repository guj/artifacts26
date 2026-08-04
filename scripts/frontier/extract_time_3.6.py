#!/usr/bin/env python3
"""Extract TotalTime and IOTime from WarpX/openPMD job outputs.

Usage:
  cd <parent>                    # directory that contains job_id/ (no slash)
  python3 extract_time_3.6.py <job_id>

  # or from anywhere:
  python3 extract_time_3.6.py <job_id> [--root DIR]

Looks under <root>/<job_id>/ (default root: cwd) for dirs named:
  <encoding>_<job_id>_<type>_<numNodes>n/outs/output.<type>_<BPEngine_Agg>

Pass the bare job id (e.g. 5130062), not job_id/ with a trailing slash.

For each output file:
  TotalTime — value of "Total Time                     :" (seconds)
  IOTime    — largest 5th column ("to" time) among WriteToFile lines

Requires Python 3.6+.
"""

import argparse
import re
import sys
from pathlib import Path

DIR_RE = re.compile(r"^[^_]+_(\d+)_(.+)_(.+?)n$")
TOTAL_TIME_RE = re.compile(r"^Total Time\s*:\s*([0-9.eE+-]+)", re.M)


def parse_args():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("jobid", help="Job ID directory name under --root")
    p.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Parent directory containing <jobid>/ (default: current directory)",
    )
    return p.parse_args()


def io_time_from_text(text):
    best = None
    for line in text.splitlines():
        if "WriteToFile" not in line:
            continue
        toks = line.split()
        if len(toks) < 6:
            continue
        # trailing fields: ncalls  from  avg  to  pct%
        try:
            to_time = float(toks[-2])
        except ValueError:
            continue
        if best is None or to_time > best:
            best = to_time
    return best


def _strip_prefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix) :]
    return s


def collect(job_dir, jobid):
    rows = []
    for out in sorted(job_dir.glob("*/outs/output.*")):
        dirname = out.parts[-3]
        m = DIR_RE.match(dirname)
        if not m or m.group(1) != jobid:
            sys.stderr.write("WARN: skip unparseable dir {}\n".format(dirname))
            continue
        type_name = m.group(2)
        num_nodes = m.group(3)

        out_suffix = _strip_prefix(out.name, "output.")
        if out_suffix.startswith(type_name + "_"):
            bp_agg = out_suffix[len(type_name) + 1 :]
        else:
            bp_agg = out_suffix

        text = out.read_text(errors="replace")
        tm = TOTAL_TIME_RE.search(text)
        total_time = tm.group(1) if tm else "N/A"
        io = io_time_from_text(text)
        io_time = str(io) if io is not None else "N/A"
        rows.append((jobid, type_name, bp_agg, num_nodes, total_time, io_time))
    return rows


def main():
    args = parse_args()
    jobid = str(args.jobid)
    job_dir = args.root / jobid
    if not job_dir.is_dir():
        sys.stderr.write("error: job directory not found: {}\n".format(job_dir))
        return 1

    rows = collect(job_dir, jobid)
    if not rows:
        sys.stderr.write("error: no output.* files under {}\n".format(job_dir))
        return 1

    hdr = "{:<10} {:<12} {:<16} {:>8} {:>14} {:>10}".format(
        "jobid", "type", "BPEngine_Agg", "numNodes", "TotalTime", "IOTime"
    )
    print(hdr)
    print("-" * len(hdr))
    for jobid, type_name, bp_agg, num_nodes, total_time, io_time in rows:
        print(
            "{:<10} {:<12} {:<16} {:>8} {:>14} {:>10}".format(
                jobid, type_name, bp_agg, num_nodes, total_time, io_time
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
