import time
import random
import string
import matplotlib.pyplot as plt

def generate_random_sequence(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = lcs[::-1]

    return lcs

if __name__ == "__main__":

    test_lengths = list(range(0, 10000, 100))  # Increasing sequence with a step size of 10
    ellapsed_times = []
    theoretical_times = []

    num_tests = 1
    total_time_ns = 0
    normalization_factor = 1041.635945715738

    for length in test_lengths:
        for _ in range(num_tests):
            X = generate_random_sequence(length)
            Y = generate_random_sequence(length)
        
            start_time = time.perf_counter()
            lcs = longest_common_subsequence(X, Y)
            end_time = time.perf_counter()

            elapsed_time_ns = (end_time - start_time) * 1e9
            total_time_ns += elapsed_time_ns

        average_time_ns = total_time_ns / num_tests
        ellapsed_times.append(average_time_ns)
        theoretical_times.append(length * length * normalization_factor)

        print("Average time per call for length ", length," in nanoseconds:", average_time_ns)


    sum = 0
    for time in ellapsed_times:
        sum += time
    
    sum_theoretical = 0
    for time in theoretical_times:
        sum_theoretical += time

    normalization_factor = sum / sum_theoretical
    print("Normalization factor:", normalization_factor)

   # Plot the data
    plt.plot(test_lengths, ellapsed_times, marker='o')
    plt.plot(test_lengths, theoretical_times, marker='x', label='n^2')
    plt.title('Test Length vs. Elapsed Time')
    plt.xlabel('Test Length')
    plt.ylabel('Elapsed Time (ns)')
    plt.grid(True)
    plt.show()

