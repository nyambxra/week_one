def minOperations(n):
    # Base case: if n is less than or equal to 1, return 0
    if n <= 1:
        return 0
    
    # Initialize a list to store the minimum operations required
    dp = [float('inf')] * (n+1)

    # Set the base case: 0 operations required to convert 1 to 1
    dp[1] = 0
    
    # Iterate from 2 to n to compute the minimum operations required
    for i in range(2, n+1):
        # Check if i is a factor of n
        if n % i == 0:
            # If i is a factor, calculate operations needed to reach i and update dp[i]
            for j in range(1, i // 2 + 1):
                dp[i] = min(dp[i], dp[j] + dp[i // j] + 2)

    # Check if it's possible to reach n characters
    if dp[n] != float('inf'):
        return dp[n]
    else:
        return 0
    

# example usage:
n = 10
result = minOperations(n)
print(f"Number of operations for {n} characters: {result}")
                
            
            

