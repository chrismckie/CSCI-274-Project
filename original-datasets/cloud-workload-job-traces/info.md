# Cloud Workload Job Traces for Resource Forecasting

Dataset from [zoya77](https://www.kaggle.com/zoya77)

[Link to Kaggle Dataset](https://www.kaggle.com/datasets/zoya77/cloud-workload-job-traces-for-resource-forecasting)

## About Dataset

This dataset captures real-world cloud workload job traces consisting of detailed information about resource requests, usage patterns, job scheduling times, and user behavior. It includes 3,562 unique records representing submitted jobs in a distributed cloud environment. Each entry logs metadata such as submission time, start/end timestamps, CPU and memory usage, and job priority. The dataset reflects realistic usage diversity, incorporating various job types like batch, interactive, and GPU-intensive tasks. It helps analyze queue wait times, resource allocation gaps, and user-level patterns. The data is essential for improving workload forecasting, resource planning, and SLA compliance in cloud systems.

### About this file

Dataset Description
This dataset was generated to support cloud workload analysis and resource usage forecasting. It contains high-resolution job traces with time-based attributes and performance-related indicators. The dataset is tailored to mimic operational cloud systems with varying CPU/memory demands and job characteristics. It is useful for benchmarking workload prediction methods and evaluating system-level efficiency.

#### Column Descriptions

**Job_ID:** Unique identifier for each job submitted to the system.

**Submit_Time:** The timestamp when the job was submitted by the user.

**Start_Time:** Time when the job began executing after waiting in queue.

**End_Time:** Time at which the job execution completed.

**Requested_CPUs:** Number of CPU cores initially requested for the job.

**Used_CPUs:** Number of CPU cores actually utilized during execution.

**Requested_Memory(MB):** Memory requested in megabytes.

**Used_Memory(MB):** Actual memory used in megabytes.

**Execution_Time(Seconds):** Total time taken by the job from start to end.

**Queue_Wait_Time(Seconds):** Time difference between job submission and start.

**User_ID:** Encoded identifier of the user who submitted the job.

**Job_Type:** Type of the job (e.g., batch, interactive, GPU, MPI).

**Priority_Level:** Scheduling priority assigned to the job.

**Node_Count:** Number of compute nodes used for the job.

**Interarrival_Time:** Time interval between job submissions.
