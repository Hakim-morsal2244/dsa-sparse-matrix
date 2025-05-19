# Sparse Matrix - DSA HW01

## 📌 Overview

This project implements a Sparse Matrix in Python as part of the Data Structures and Algorithms (DSA) coursework at ALU. Sparse matrices are matrices in which most elements are zero. To save space and improve efficiency, this project only stores and processes non-zero elements.

The assignment includes:
- Reading sparse matrix data from a file
- Displaying the matrix in a sparse format
- Adding two sparse matrices
- Handling invalid input or mismatched matrix sizes

---

## 📁 Project Structure

dsa-sparse-matrix/
│
├── README.md
├── sample_inputs/
│ ├── matrix1.txt
│ └── matrix2.txt
│
├── code/
│ └── src/
│ ├── sparse_matrix.py
│ └── test_sparse.py


---

## 🧠 Features

- Efficient representation using Python dictionaries
- File-based input for easy testing
- Matrix addition with dimension checks
- Clear and readable output format
- Graceful error handling

---

## 🧪 Sample Input (`matrix1.txt`)


4 4
0 1 5
1 2 8
2 3 -3
3 0 6


## ✅ Expected Output


---


Sparse Matrix 4x4
(0, 1): 5
(1, 2): 8
(2, 3): -3
(3, 0): 6

yaml
Copy
Edit


## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/dsa-sparse-matrix.git
cd dsa-sparse-matrix/code/src


💡 Notes
Make sure the sample_inputs folder is in the correct location (../sample_inputs) relative to the src folder.

Input files must follow the format: first line = matrix size (rows cols), followed by non-zero entries (row col value).

🧑‍💻 Author
Morsal Hakim (@Hakim-morsal2244)


📜 License
This project is for educational purposes only.
