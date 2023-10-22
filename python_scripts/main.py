import pandas as pd
# import resource - not available on Windows
import time
import psutil
import tracemalloc
 
def load_data(file = "IMDB-Movie-Data.csv"):
    # load the data
    df = pd.read_csv("../data/" + file)
    return df


# get memory resources
def get_system_resources():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/')
    return cpu_percent, memory_percent, disk_usage

# main function to run function and calculate execution time + memory usage
def main():
    start_time = time.time()
    tracemalloc.start()

    # function to run data analysis
    df = load_data()
    print(f"Size of Movie df: {df.shape}")

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()

    print("Execution Time: {:.8f} seconds".format(end_time - start_time))
    print("Function Memory Usage: {:.4f} MB".format(peak_memory / (1024 ** 2)))

if __name__ == "__main__":
    main()

    cpu_percent, memory_percent, disk_usage = get_system_resources()

    print("Tot CPU Usage: {:.2f}%".format(cpu_percent))
    print("Tot Memory Usage: {:.2f}%".format(memory_percent))
    print("Disk Usage: Total {:.2f} GB, Used {:.2f} GB, Free {:.2f} GB".format(
        disk_usage.total / (1024 ** 3),
        disk_usage.used / (1024 ** 3),
        disk_usage.free / (1024 ** 3)
    ))