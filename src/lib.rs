use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
pub mod function;

#[pyfunction]
fn add_f64(x: f64, y: f64) -> f64 {
    return function::add(x, y);
}

#[pyfunction]
fn sum_usize(a: usize, b: usize) -> PyResult<String> {
    return Ok(function::sum_as_string(a, b));
}

// the name should be the same with rust project name, which is pyo3_learn in this project
#[pymodule]
fn pyo3_learn(_py: Python<'_>, m: &PyModule) -> PyResult<()> { 
    m.add_function(wrap_pyfunction!(add_f64, m)?)?;
    m.add_function(wrap_pyfunction!(sum_usize, m)?)?; 
    Ok(())
}