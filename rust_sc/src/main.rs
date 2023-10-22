use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::time::Instant;
use std::mem::size_of;

use csv::ReaderBuilder;
use rayon::prelude::*;
use itertools::Itertools;

fn load_data(file: &str) -> Vec<Vec<String>> {
    let file = File::open(file).unwrap();
    let mut reader = BufReader::new(file);
    let mut contents = String::new();
    reader.read_to_string(&mut contents).unwrap();
    let mut rdr = ReaderBuilder::new().has_headers(true).from_reader(contents.as_bytes());
    let records = rdr.records().map(|r| r.unwrap().iter().map(|s| s.to_string()).collect_vec()).collect_vec();
    records
}

fn sort_data(mut data: Vec<Vec<String>>, by: usize) -> Vec<Vec<String>> {
    data.par_sort_by(|a, b| b[by].cmp(&a[by]));
    data
}

fn main() {
    let start_time = Instant::now();

    // function to run data analysis
    let data = load_data("../data/IMDB-Movie-Data.csv");
    let data = sort_data(data, 13);

    let end_time = Instant::now();
    
    println!("Size of Movie df: {:?}", data.len());
    println!("Execution Time: {:.8} seconds", end_time.duration_since(start_time).as_secs_f64());
    println!("Function Memory Usage: {:.4} MB", (data.len() * size_of::<Vec<String>>()) as f64 / (1024.0 * 1024.0));
}