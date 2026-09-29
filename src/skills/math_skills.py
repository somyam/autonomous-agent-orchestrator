def compute_fibonacci(n: int) -> int:
    """Calculate the n-th Fibonacci number.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n (int): The position in the Fibonacci sequence.
        
    Returns:
        int: The n-th Fibonacci number. Returns 0 for n <= 0.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b