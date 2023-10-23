use std::process::Command;
use std::time::{Instant, Duration};

fn get_system_resources() -> (f32, f32, Duration) {
    let start_time = Instant::now(); // Capture the start time

    let cpu_output = Command::new("ps")
        .args(&["aux", "--no-headers"])
        .output()
        .expect("Failed to execute ps command");

    let cpu_percent = String::from_utf8_lossy(&cpu_output.stdout)
        .lines()
        .map(|line| {
            let fields: Vec<&str> = line.split_whitespace().collect();
            fields[2].parse::<f32>().unwrap_or(0.0)
        })
        .sum();

    let mem_output = Command::new("ps")
        .args(&["aux", "--no-headers"])
        .output()
        .expect("Failed to execute ps command");

    let mem_percent = String::from_utf8_lossy(&mem_output.stdout)
        .lines()
        .map(|line| {
            let fields: Vec<&str> = line.split_whitespace().collect();
            fields[3].parse::<f32>().unwrap_or(0.0)
        })
        .sum();

    let elapsed_time = start_time.elapsed(); // Calculate elapsed time

    (cpu_percent, mem_percent, elapsed_time)
}

fn main() {
    // Get system resource usage
    let (cpu_percent, mem_percent, elapsed_time) = get_system_resources();

    println!("Tot CPU Usage: {:.2}%", cpu_percent);
    println!("Tot Memory Usage: {:.2}%", mem_percent);

    // Print elapsed time in milliseconds
    println!("Elapsed Time: {} ms", elapsed_time.as_millis());
}
