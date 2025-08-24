# Python implementation following the (implied) reasoning:
# - Main flow: data input -> validation -> sum -> mean -> storage -> output -> final
# - Sub-algorithms: validate_input, compute_sum, compute_mean, store_result, output_result
# - Data-input/output flowcharts and final result flowcharts are represented as ASCII art strings
# - Flowcharts are printed at each stage, including a separate flowchart for each function call
# - Results are stored in an in-memory storage (a dict)

# ASCII flowcharts (main and sub-algorithms, inputs/outputs, final result, storage, and function calls)

FLOW_MAIN_FLOW = r"""
+--------------------------------------------------+
| MAIN BODY OF THE ALGORITHM                         |
| 1) Start                                           |
| 2) Data Input                                      |
| 3) Validation -> Sum -> Mean -> Storage -> Output  |
| 4) Final result                                    |
| 5) End                                             |
+--------------------------------------------------+
"""

FLOW_INPUT_FLOW = r"""
+------------------------+
| Data Input             |
| - Receive input data   |
| - Prepare as list(nums)|
+------------------------+
"""

FLOW_VALIDATE_FLOW = r"""
+---------------------------+
| Validate Input            |
| - Check all items are nums  |
| - Check list is non-empty     |
+---------------------------+
"""

FLOW_SUM_FLOW = r"""
+---------------------+
| Compute Sum         |
| - total = sum(nums) |
+---------------------+
"""

FLOW_MEAN_FLOW = r"""
+---------------------+
| Compute Mean        |
| - mean = total / n   |
+---------------------+
"""

FLOW_STORE_FLOW = r"""
+----------------------+
| Store Result         |
| - Persist to storage  |
+----------------------+
"""

FLOW_OUTPUT_FLOW = r"""
+----------------------+
| Output Result        |
| - Show final values  |
+----------------------+
"""

FLOW_FINAL_FLOW = r"""
+----------------------+
| Final Result         |
| - Return result dict |
+----------------------+
"""

FLOW_STORAGE_FLOW = r"""
+----------------------+
| Storage Layer        |
| - In-memory dict     |
+----------------------+
"""

# Flowcharts for function calls
FLOW_CALL_MAIN = r"""
[CALL] Enter function: solve_problem (main flow)
"""

FLOW_CALL_VALIDATE = r"""
[CALL] Enter function: validate_input
"""

FLOW_CALL_SUM = r"""
[CALL] Enter function: compute_sum
"""

FLOW_CALL_MEAN = r"""
[CALL] Enter function: compute_mean
"""

FLOW_CALL_STORE = r"""
[CALL] Enter function: store_result
"""

FLOW_CALL_OUTPUT = r"""
[CALL] Enter function: output_result
"""

FLOW_CALL_STORAGE = r"""
[CALL] Enter function: storage module (store)
"""

# Data/input/output and final result flowcharts labels
FLOW_LABELS = {
    "main_flow": FLOW_MAIN_FLOW,
    "input_flow": FLOW_INPUT_FLOW,
    "validate_flow": FLOW_VALIDATE_FLOW,
    "sum_flow": FLOW_SUM_FLOW,
    "mean_flow": FLOW_MEAN_FLOW,
    "store_flow": FLOW_STORE_FLOW,
    "output_flow": FLOW_OUTPUT_FLOW,
    "final_flow": FLOW_FINAL_FLOW,
    "storage_flow": FLOW_STORAGE_FLOW,
    "call_main": FLOW_CALL_MAIN,
    "call_validate": FLOW_CALL_VALIDATE,
    "call_sum": FLOW_CALL_SUM,
    "call_mean": FLOW_CALL_MEAN,
    "call_store": FLOW_CALL_STORE,
    "call_output": FLOW_CALL_OUTPUT,
    "data_input": FLOW_INPUT_FLOW,
    "data_output": FLOW_OUTPUT_FLOW
}

# In-memory storage for results
STORAGE = {}

def print_flowchart(label: str) -> None:
    # Print the ASCII flowchart for the given label if available
    art = FLOW_LABELS.get(label)
    if art is None:
        print(f"[No flowchart defined for label: {label}]")
    else:
        print(art)

def solve_problem(input_numbers):
    """
    Main entry point implementing the described reasoning:
    - Validate input
    - Compute sum
    - Compute mean
    - Store and output result
    - Return final result dictionary
    """
    # 1. Main flow start
    print_flowchart("call_main")
    print_flowchart("main_flow")

    # 2. Data Input flow
    print_flowchart("call_main")  # represent a call to main as a whole
    print_flowchart("input_flow")
    nums = input_numbers

    # 3. Validate Input (sub-algorithm)
    print_flowchart("call_validate")
    print_flowchart("validate_flow")
    if not isinstance(nums, list) or len(nums) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("All elements in input must be numbers.")

    # 4. Compute Sum (sub-algorithm)
    print_flowchart("call_sum")
    print_flowchart("sum_flow")
    total = sum(nums)

    # 5. Compute Mean (sub-algorithm)
    print_flowchart("call_mean")
    print_flowchart("mean_flow")
    n = len(nums)
    mean = total / n if n > 0 else 0

    # 6. Store Result (sub-algorithm)
    print_flowchart("call_store")
    print_flowchart("store_flow")
    result = {
        "sum": total,
        "mean": mean,
        "count": n
    }
    STORAGE["result"] = result  # store in-memory
    print_flowchart("storage_flow")
    # Explicit storage call (even though we already stored above)
    # (We keep this for completeness with the required flowchart)
    # No real action beyond the dictionary assignment above

    # 7. Output Result (sub-algorithm)
    print_flowchart("call_output")
    print_flowchart("output_flow")
    print("Final Result:", result)

    # 8. Final result flow
    print_flowchart("final_flow")
    return result

# Example usage (can be removed if used as a module)
if __name__ == "__main__":
    sample_input = [1, 2, 3, 4, 5]
    solve_problem(sample_input)