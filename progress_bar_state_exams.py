import csv
import os
import datetime
import matplotlib.pyplot as plt
from tqdm import tqdm

PROGRESS_FILE = "progress_state_exams.csv"

# Function to load progress from CSV
def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return []
    with open(PROGRESS_FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)

# Function to save progress to CSV
def save_progress(timestamp, previous, new, previous_total, new_total):
    with open(PROGRESS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, previous, new, previous_total, new_total])

# Function to update progress
def update_progress(new_progress, new_total):
    data = load_progress()
    previous_progress = int(data[-1][2]) if data else 0
    previous_total = int(data[-1][4]) if data else 0
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_progress(timestamp, previous_progress, new_progress, previous_total, new_total)
    show_progress_bar(new_progress, new_total)

# Function to display a progress bar
def show_progress_bar(progress, total):
    print(f"\nThesis Progress: {progress}/{total}")
    bar = tqdm(total=total, initial=progress, bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")
    bar.close()

# Function to plot progress over time
def plot_progress():
    data = load_progress()
    if not data:
        print("No progress data available.")
        return
    
    timestamps = [datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in data]
    progress = [int(row[2]) for row in data]
    total_work = [int(row[4]) for row in data]
    
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, total_work, marker="", linestyle="-", color="b", alpha = 0.3,label="Total Work")
    plt.fill_between(timestamps, total_work, color="b", alpha=0.3)

    plt.plot(timestamps, progress, marker="", linestyle="-", color="r", label="Progress")
    plt.fill_between(timestamps, progress, color="r", alpha=0.3)
    
    
    
    plt.xlabel("Date")
    plt.ylabel("Progress")
    plt.title("First Look at State Exam Sub-Topic (Progress Over Time)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.savefig("state_exam_progress_plot.png", dpi=200)

# Example Usage
if __name__ == "__main__":
    update = input("Do you want to update? (Y/N): ")
    if update == "Y":
        total_work = 52  # Allow user to re-enter total work each time
        new_progress = int(input("Enter the amount of topics covered so far: "))
        update_progress(new_progress, total_work)
    plot_progress()
