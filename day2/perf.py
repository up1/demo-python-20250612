# check member in large list performance
import time
def check_member_in_list(large_list, item):
    start_time = time.time()
    result = item in large_list
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

# Example usage
if __name__ == "__main__":
    # Create a large list
    large_list = list(range(10_000_000))  # List of integers from 0 to 999999

    # Check for an item in the list
    item_to_check = 9_999_999
    result, elapsed_time = check_member_in_list(large_list, item_to_check)

    print(f"Item {item_to_check} found: {result}")
    print(f"Time taken to check membership: {elapsed_time:.6f} seconds")