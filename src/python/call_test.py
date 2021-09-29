from itertools import islice
import os
import shutil
import platform

# before run this file, run 'cargo build --release' to build release rust library

# compare two files, if the same return true, else return false
def cmp_file(f1, f2):
    st1 = os.stat(f1)
    st2 = os.stat(f2)
    # compare size
    if st1.st_size != st2.st_size:
        return False
    bufsize = 8 * 1024
    with open(f1, 'rb') as fp1, open(f2, 'rb') as fp2:
        while True:
            b1 = fp1.read(bufsize)  # read block and compare
            b2 = fp2.read(bufsize)
            if b1 != b2:
                return False
            if not b1:
                return True


# move rust library to this directory
def load_rust_dll():
    oriPath = os.path.abspath(os.path.join(os.path.dirname(
        __file__), '..\\..\\target\\release\\pyo3_learn.dll'))
    desPath = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '.\\pyo3_learn.pyd'))

    if platform.system().lower() == 'linux':
        oriPath = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '../target/release/libpyo3_learn.so'))
        desPath = os.path.abspath(os.path.join(
            os.path.dirname(__file__), './pyo3_learn.so'))

    if os.path.exists(desPath) and cmp_file(oriPath, desPath):
        return
    else:
        try:
            print("\nmove rust library to python library")
            shutil.copy(oriPath, desPath)
        except shutil.SameFileError:
            print("same library file")
            pass


# test 2 rust functions
def function_test(): 
    
    load_rust_dll()
    from pyo3_learn import add_f64, sum_usize

    print("1.5 + 14.5 = ")
    print(add_f64(1.5, 14.5))

    print("3 + 19 = ")
    print(sum_usize(3, 19))


if __name__ == '__main__':
    function_test()
