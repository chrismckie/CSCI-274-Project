import pandas as pd
from datetime import timedelta

# Converts HH:MM:SS to minutes since midnight
def time_to_minutes(time):
    if isinstance(time, pd.Timestamp):
        return time.hour * 60 + time.minute
    else:
        hours, minutes, seconds = map(int, time.split(':'))
        return hours * 60 + minutes

# Creates a dictionary for a week of dates
def get_week_by_start_date(df, week_start):

    # Determine column names based on dataframe input
    if df.columns[0] == "appointment_id":
        is_medical_data = True

        # Process medical data
        id = "appointment_id"
        job_date = "appointment_date"      
    else:
        is_medical_data = False

        # Process cloud data
        id = "job_interval"
        job_date = "job_date"
  
    # These values are the same across both datasets
    start_time = 'start_time'
    end_time = 'end_time'
    start = "start_minutes"
    end = "end_minutes"
    priority = "priority"

    num_weeks = 2 if is_medical_data else 1     # Medical data combines appointments over multiple weeks
    week_start = pd.to_datetime(week_start)
    week_end = week_start + pd.Timedelta(days=7 * num_weeks)

    df = df.copy()
    df[job_date] = pd.to_datetime(df[job_date])

    # Filter to the week
    mask = (df[job_date] >= week_start) & (df[job_date] < week_end)
    week_df = df.loc[mask].copy()

    # Group dataframes by day of the week
    day_frames = {}

    if is_medical_data:
        # Medical data groups 3 weeks of data by weekday
        week_df["weekday"] = week_df[job_date].dt.day_name()

        for day_name, group in week_df.groupby("weekday"):
            day_frames[day_name] = (
                group[[id, start_time, end_time, start, end, priority]]
                .sort_values(start)
                .reset_index(drop=True)
            )
    else:
        # Cloud data groups 1 week of data by weekday
        for date, group in week_df.groupby(week_df[job_date].dt.date):
            day_name = pd.to_datetime(date).strftime('%A')

            # Sort by start time
            day_frames[day_name] = (
                group[[id, start_time, end_time, start, end, priority]]
                .sort_values(start)
                .reset_index(drop=True)
            )
    return day_frames

# Returns data frame w columns: appointment_id, start_time, end_time, priority
def load_medical_data(filepath):
    df = pd.read_csv(filepath)

    df['appointment_date'] = pd.to_datetime(df['appointment_date'])
    df = df.dropna(subset=['appointment_id', 'start_time', 'end_time', 'age', 'appointment_duration'])
    df = df[df['appointment_duration'] <= 1440].copy()

    df['start_minutes'] = df['start_time'].apply(time_to_minutes)
    df['end_minutes'] = df['end_time'].apply(time_to_minutes)

    # Prioritizes appointments by the age of patient
    df['priority'] = df['age']

    result = df[['appointment_id', 
                 'appointment_date', 
                 'start_time', 
                 'end_time', 
                 'start_minutes', 
                 'end_minutes', 
                 'priority']]

    return result

def load_cloud_data(filepath):
    df = pd.read_csv(filepath)

    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['End_Time'] = pd.to_datetime(df['End_Time'])

    # Clean data
    df = df.dropna(subset=['Job_ID', 'Start_Time', 'End_Time', 'Priority_Level'])
    df['duration_hours'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds() / 3600

    df['job_date'] = df['Start_Time'].dt.date
    df['start_minutes'] = df['Start_Time'].apply(time_to_minutes)
    df['end_minutes'] = df['End_Time'].apply(time_to_minutes)

    # Filter out jobs that are longer than 24 hours or extend into the next day
    df = df[df['duration_hours'] <= 24].copy()
    df = df[df['end_minutes'] > df['start_minutes']].copy()

    priority_map = {'low': 1, 'medium': 2, 'high': 3}
    df['priority'] = df['Priority_Level'].str.lower().map(priority_map)

    result = df[['Job_ID', 
                 'job_date', 
                 'Start_Time', 
                 'End_Time', 
                 'start_minutes', 
                 'end_minutes', 
                 'priority']]
    result = result.rename(columns={'Job_ID': 'job_interval', 'Start_Time': 'start_time', 'End_Time': 'end_time'})

    return result

def min_to_hhmm(x, pos):
    hours = int(x) // 60
    minutes = int(x) % 60
    return f"{hours:02d}:{minutes:02d}"