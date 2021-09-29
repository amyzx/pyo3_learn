use pyo3_learn::function::*;
  
fn main() {
    println!("test functions");
    let x = 10.1;
    let y = 4.9;
    println!("{} + {} = {}", x, y, add(x, y));

    let a: usize = 5;
    let b: usize = 10;
    println!("{} + {} = {}", a, b, sum_as_string(a, b));
}