#!/bin/bash

# Enable nullglob so unmatched patterns expand to nothing
shopt -s nullglob

# Customize Bash 'time' output format: %3R prints real (elapsed) time in seconds with 3 decimals
export TIMEFORMAT="%3R"

num_nodes_list=(8 16 32)
base_path="PerformanceRun/BTD"
summary_log="timing_summary.txt"

# Clear old log file
> "$summary_log"

echo "=================================================="
echo " Starting Benchmark Runs (Using Bash 'time')"
echo "=================================================="

for numNodes in "${num_nodes_list[@]}"; do
    bp_dir="${base_path}/N${numNodes}/bp_flatten"

    [[ -d "$bp_dir" ]] || continue

    for job_path in "${bp_dir}"/*/; do
        jobID=$(basename "$job_path")

        # Verify jobID is an integer
        if [[ "$jobID" =~ ^[0-9]+$ ]]; then
            target_dir="${bp_dir}/${jobID}/f_${jobID}_flatten_${numNodes}n/diags/diag1_f"

            if [[ -d "$target_dir" ]]; then
                for bp_item in "${target_dir}"/openpmd_00000[0-3].bp/; do
                    bp_name=$(basename "$bp_item")
                    
                    echo "--------------------------------------------------"
                    echo "Target: N${numNodes} | Job ${jobID} | ${bp_name}"
                    echo "--------------------------------------------------"

		    ./bpls -V ${bp_item}
                    times=()
                    for run in 1 2 3; do
                        # Capture stderr output of 'time' into variable
                        elapsed=$( { time ./bpls -l "$bp_item" > /dev/null ; } 2>&1 )
                        
                        times+=("$elapsed")
                        echo "  Run ${run}: ${elapsed}s"
                    done

                    # Log all 3 runs to the summary file
                    printf "Nodes: %-2s | JobID: %-8s | File: %-20s | Run 1: %6ss | Run 2: %6ss | Run 3: %6ss\n" \
                        "$numNodes" "$jobID" "$bp_name" "${times[0]}" "${times[1]}" "${times[2]}" >> "$summary_log"

                    echo ""
                done
            fi
        fi
    done
done

echo "=================================================="
echo " Timing Summary Report"
echo "=================================================="
cat "$summary_log"
