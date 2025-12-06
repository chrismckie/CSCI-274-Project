import weighed_interval_scheduling as wis

# Example from lecture slides to test the algorithm code
interval = ['A', 'B', 'C', 'D', 'E', 'F','G','H']
intervalNum = [i for i in range(len(interval))]
start = [1, 3, 0, 4, 3, 5, 6, 8]
finish = [4, 5, 6, 7, 8, 9, 10, 11]
weight = [5, 6, 5, 4, 11, 2, 8, 7]

# Run algorithm 
max_profit, selected_intervals = wis.create_interval_schedule(intervalNum, start, finish, weight)
selected = [interval[i] for i in selected_intervals]
print(f"Maximum Profit: {max_profit}")  # Expected: 18
print(f"Selected Jobs: {selected}")     # Expected: [E, H]