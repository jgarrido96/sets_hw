
# 1. Python Sets Adventure

# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
all_routes = our_routes.union(competitor_routes)
print(f"Destinations that we both fly to: {all_routes}")

our_exclusive_destinations = our_routes - competitor_routes
print(f"Our exclusive destinations: {our_exclusive_destinations}")

neither = our_routes.symmetric_difference(competitor_routes)
print(f"Places where we don't layover: {neither}")

print('\n')
# 2. Set Operations in Data Analysis

# Task:1 Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
print(f"List of customer ID's:\n{customer_ids}")
set = set(customer_ids)
list_ids = list(sorted(set))
print(f"Here's a list of unique customer ID's:\n{list_ids}")