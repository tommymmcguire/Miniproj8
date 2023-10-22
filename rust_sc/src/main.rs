extern crate csv;
extern crate sys_info;

use csv::ReaderBuilder;
use sys_info::{cpu, mem};
use std::time::{SystemTime, UNIX_EPOCH};

fn load_data(file: &str) -> Result<Vec<Vec<String>>, csv::Error> {
    let mut reader = ReaderBuilder::new().from_path(file)?;
    let records = reader.records().collect();
    records
}

fn get_system_resources() -> (f32, f32, f32) {
    let cpu_percent = cpu::cpu_usage().unwrap_or(0.0);
    let memory_info = mem::mem_info().unwrap_or(mem::MemInfo {
        total: 0,
        free: 0,
        avail: 0,
        buffers: 0,
        cached: 0,
        swap_total: 0,
        swap_free: 0,
    });
    let memory_percent = (1.0 - memory_info.free as f32 / memory_info.total as f32) * 100.0;

    (cpu_percent, memory_percent, memory_info.total as f32 / 1024.0 / 1024.0)
}

fn main() -> Result<(), csv::Error> {
    let file = "../data/IMDB-Movie-Data.csv";

    // Start measuring execution time
    let start_time = SystemTime::now();
    let start_time_ms = start_time.duration_since(UNIX_EPOCH).unwrap().as_secs_f64();

    // Load data
    let data = load_data(file)?;

    // Calculate execution time
    let end_time = SystemTime::now();
    let end_time_ms = end_time.duration_since(UNIX_EPOCH).unwrap().as_secs_f64();

    println!("Size of Movie df: {:?}", data.len());
    println!("Execution Time: {:.8} seconds", end_time_ms - start_time_ms);

    // Get system resource usage
    let (cpu_percent, memory_percent, total_memory) = get_system_resources();

    println!("Tot CPU Usage: {:.2}%", cpu_percent);
    println!("Tot Memory Usage: {:.2}%", memory_percent);
    println!("Total Memory: {:.2} GB", total_memory);

    Ok(())
}
