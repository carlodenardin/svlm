import json
from typing import Any, Dict, List, Optional, Union

# Flowcharts (ASCII diagrams) for documentation in code

FLOW_MAIN_BODY = r"""
+-----------------------------------+
|             Main Body             |
+-----------------------------------+
| Start                             |
|   |                               |
|   v                               |
| Parse Input Data ---------------->|
|   |                               |
|   v                               |
| Compute Metrics                   |
|   |                               |
|   v                               |
| Store Results                     |
|   |                               |
|   v                               |
| End                               |
+-----------------------------------+
"""

FLOW_PARSE_INPUT = r"""
+-----------------------------------+
|         Sub-Algorithm: Parse Input  |
+-----------------------------------+
| Start                             |
|   |                               |
|   v                               |
| Validate Raw Data                   |
|   |                               |
|  No -> Raise Error                 |
|   |                               |
|  Yes -> Convert to List of Ints    |
|   |                               |
|   v                               |
| Return nums                       |
+-----------------------------------+
"""

FLOW_COMPUTE_METRICS = r"""
+-----------------------------------+
|        Sub-Algorithm: Compute Metrics |
+-----------------------------------+
| Start                              |
|   |                                |
|   v                                |
| Compute Sum, Product, Count        |
|   |                                |
|   v                                |
| Compute Average (sum/count)        |
|   |                                |
|   v                                |
| Return metrics dict                |
+-----------------------------------+
"""

FLOW_STORE_RESULTS = r"""
+-----------------------------------+
|        Sub-Algorithm: Store Results  |
+-----------------------------------+
| Start                              |
|   |                                |
|   v                                |
| Prepare JSON payload               |
|   |                                |
|   v                                |
| Write to storage_path (JSON)       |
|   |                                |
|   v                                |
| Confirm and Return                 |
+-----------------------------------+
"""

FLOW_INPUT_DATA = r"""
+-----------------------------------+
|          Data Input Flow          |
+-----------------------------------+
| Raw input provided by caller       |
|   |                                 |
|   v                                 |
| Parsed into a list of integers     |
|   |                                 |
|   v                                 |
| Output: nums (list[int])            |
+-----------------------------------+
"""

FLOW_OUTPUT_DATA = r"""
+-----------------------------------+
|          Data Output Flow          |
+-----------------------------------+
| Metrics dict produced by compute     |
|   |                                    |
|   v                                    |
| data = { input: nums, metrics: dict } |
|   |                                    |
|   v                                    |
| Output: data to caller (return)       |
+-----------------------------------+
"""

FLOW_FINAL_RESULT = r"""
+-----------------------------------+
|          Final Result Flow          |
+-----------------------------------+
| data = { input, metrics }            |
|   |                                    |
|   v                                    |
| Return to caller / display to user    |
+-----------------------------------+
"""

FLOW_UI = r"""
+-----------------------------------+
|          User Interface Flow        |
+-----------------------------------+
| Start UI prompts (CLI)               |
|   |                                    |
|   v                                    |
| Collect raw input                         |
|   |                                    |
|   v                                    |
| Pass input to solver                    |
+-----------------------------------+
"""

FLOW_STORAGE = r"""
+-----------------------------------+
|          Storage Flow               |
+-----------------------------------+
| Prepare data payload                    |
|   |                                       |
|   v                                       |
| Write to storage.json                    |
|   |                                       |
|   v                                       |
| Confirm storage completion               |
+-----------------------------------+
"""

FLOW_ERROR_CLEANUP = r"""
+-----------------------------------+
| Error Handling & Cleanup                |
+-----------------------------------+
| Catch exception                          |
|   |                                        |
|   v                                        |
| Log error message                          |
|   |                                        |
|   v                                        |
| Cleanup resources                          |
|   |                                        |
|   v                                        |
| Exit / Rethrow                             |
+-----------------------------------+
"""


# Core implementation

def parse_input(data: Union[List[int], str, None]) -> List[int]:
    """
    Sub-algorithm: Parse Input
    Converts raw data into a list of integers.
    """
    # Display flowchart for parse_input (documentation)
    # (In actual execution, we just perform parsing.)
    if data is None:
        raise ValueError("No input data provided")

    if isinstance(data, list):
        nums = []
        for x in data:
            if isinstance(x, int):
                nums.append(x)
            else:
                raise ValueError("All elements in the input list must be integers.")
        return nums

    if isinstance(data, str):
        # Split by whitespace or commas
        tokens = [tok for tok in data.replace(',', ' ').split() if tok]
        nums = []
        for tok in tokens:
            try:
                nums.append(int(tok))
            except ValueError:
                raise ValueError(f"Invalid integer value in input: {tok}")
        return nums

    raise ValueError("Unsupported input type for parsing.")


def compute_metrics(nums: List[int]) -> Dict[str, Any]:
    """
    Sub-algorithm: Compute Metrics
    Returns a dictionary with sum, product, count, and average.
    """
    # Display flowchart for compute_metrics (documentation)
    s = sum(nums)
    p = 1
    for n in nums:
        p *= n
    count = len(nums)
    avg = (s / count) if count > 0 else None
    return {"sum": s, "product": p, "count": count, "average": avg}


def store_results(data: Dict[str, Any], storage_path: str) -> None:
    """
    Sub-algorithm: Store Results
    Serializes data to a JSON file at storage_path.
    """
    # Display flowchart for store_results (documentation)
    import os

    dirpath = os.path.dirname(storage_path)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)

    with open(storage_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def cleanup_resources() -> None:
    """
    Cleanup resources if any were opened.
    For this simple implementation, there may be nothing to clean,
    but we provide the hook for conformity with the requested flowchart.
    """
    # Could close files, network connections, etc.
    pass


def solve_problem_with_flowcharts(
    input_data: Union[List[int], str, None],
    storage_path: str = "results.json",
    show_diagrams: bool = True
) -> Dict[str, Any]:
    """
    Top-level function that ties together parsing, computation, and storage.
    It also prints ASCII flowcharts describing the process if requested.
    Returns a dictionary containing input and computed metrics.
    """
    if show_diagrams:
        print(FLOW_MAIN_BODY)
        print(FLOW_PARSE_INPUT)
        print(FLOW_COMPUTE_METRICS)
        print(FLOW_STORE_RESULTS)
        print(FLOW_INPUT_DATA)
        print(FLOW_OUTPUT_DATA)
        print(FLOW_FINAL_RESULT)
        print(FLOW_UI)
        print(FLOW_STORAGE)
        print(FLOW_ERROR_CLEANUP)

    try:
        # Data Input Flow
        nums = parse_input(input_data)

        # Computation Flow
        metrics = compute_metrics(nums)

        # Final data structure
        data = {
            "input": nums,
            "metrics": metrics
        }

        # Data Output Flow
        store_results(data, storage_path)

        # UI/Final Result Flow
        if show_diagrams:
            print("Final Result:")
            print(json.dumps(data, indent=2))

        return data

    except Exception as e:
        if show_diagrams:
            print("Error encountered during processing:")
            print(f"{type(e).__name__}: {e}")
            print(FLOW_ERROR_CLEANUP)
        # Cleanup and propagate
        try:
            cleanup_resources()
        finally:
            raise


# Optional: a tiny example to demonstrate usage (not executed on import)
if __name__ == "__main__":
    # Example input: a string of numbers
    sample_input = "1, 2, 3, 4"
    try:
        result = solve_problem_with_flowcharts(sample_input, storage_path="outputs/results.json", show_diagrams=True)
        print("Computation successful. Result stored.")
        print(result)
    except Exception as exc:
        print("An error occurred during execution:", exc)