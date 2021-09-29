## Introduction

This is an example about how to use [pyo3](https://github.com/PyO3/pyo3) library. We can call rust functions in python scripts.

In **src/function.rs**, we define two function add and sum_as_string.

In **src/bin/function_test.rs**, we test two functions.

In **src/lib.rs**, we define the interface for python and rust.

In **src/python/call_test.py**, we show how to use python to call rust functions.



## How to run

1. build the rust project and generate library

```shell
cargo build --release
```

2. go to **src/python** directory

```shell
python call_test.py
```

