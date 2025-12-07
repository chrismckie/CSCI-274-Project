# CSCI-274-Project

Job Scheduling using Weighted Interval Scheduling with Dynamic Programming

**Dataset:** This project utilizes two datasets from the Google Job Scheduling Dataset or the Kaggle Job Shop Scheduling Dataset, which contain real-world data about job start times, finish times, and profit or priority values.

This project uses two real-world datasets  (e.g., the Google Job Scheduling Dataset and the Kaggle Job Shop Scheduling Dataset) both containing information on job start times, finish times, and associated profits or priority values.

**Concept:** The project applies the Weighted Interval Scheduling Algorithm using Dynamic Programming (DP) to determine the optimal set of non-overlapping jobs that maximizes the total profit. Each job has a start time, finish time, and an associated profit, and the algorithm efficiently selects the combination of jobs that yields the highest total value without time conflicts.

**Goal:** The objective is to optimize job assignments by balancing time constraints and profit values, ensuring that the system schedules jobs in a way that achieves maximum overall benefit while maintaining efficiency in resource utilization.

**Deliverable:** A concise report comparing the performance and outcomes of the Weighted Interval Scheduling with DP algorithm across the two datasets.

## Folder Structure

```
 ├── data/  
 │   ├── original-datasets/         # Unprocessed datasets from Kaggle    
 │   │   ├── cloud-workload-job-traces/
 │   │   └── medical-appointment-scheduling-system/
 │   └── processed-datasets/        # Datasets processed from process_data.ipynb
 │       ├── cloud-workload-job-traces/
 │       └── medical-appointment-scheduling-system/
 ├── jupyter-notebooks              # Main code is run here
 │   ├── process_data.ipynb
 │   └── run_algorithm.ipynb
 ├── python                         # Algorithm and data processing functions
 │   ├── algorithm_test.py
 │   ├── data_processing.py
 │   └── weighted_interval_scheduling.py
 ├── results                        # Charts and schedules produced from run_algorithm.ipynb
 │   ├── cloud-workload/
 │   │   ├── bar-chart/
 │   │   ├── gantt-chart/
 │   │   ├── schedule
 │   └── medical-appointments/
 │       ├── bar-chart/
 │       ├── gantt-chart/
 │       └── schedule/
 └── README.md
 ```