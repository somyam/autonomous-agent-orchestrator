
## 🧮 Math Skills

### `compute_fibonacci`
Calculates the n-th number in the Fibonacci sequence using an optimized, iterative approach.

*   **Description**: Use this tool whenever a user explicitly asks to calculate a specific position in the Fibonacci sequence or needs to generate sequence values for mathematical modeling.
*   **Module Path**: `src.skills.math_skills.compute_fibonacci`
*   **Interface**:
    *   **Inputs**:
        *   `n` (integer): The 1-based index position of the sequence to retrieve.
    *   **Outputs**:
        *   (integer): The computed Fibonacci value. Returns `0` for any invalid or non-positive indices.
*   **Constraints**: 
    *   Optimized for O(n) time and O(1) space. 
    *   Do not use for non-integer inputs.