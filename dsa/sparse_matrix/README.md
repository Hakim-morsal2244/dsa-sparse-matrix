# Sparse Matrix - DSA HW01

## 📌 Overview
This project implements a **Sparse Matrix** in Python for the **Data Structures and Algorithms (DSA)** course at ALU. A sparse matrix is one where most of the elements are zero. This implementation stores only **non-zero elements** to improve space and performance.

---

## 📁 Project Structure

dsa-sparse-matrix/
├── README.md
├── sample_inputs/
│ ├── matrix1.txt
│ └── matrix2.txt
└── code/
└── src/
├── sparse_matrix.py
└── test_sparse.py

yaml
Copy
Edit

---

## 🧠 Features

- Efficient storage using Python dictionaries
- File input with clear parsing
- Matrix addition with dimension checks
- Formatted output for sparse data
- Error handling for bad input or mismatched sizes

---

## 🧪 Input Format Example (`matrix1.txt`)

4 4
0 1 5
1 2 8
2 3 -3
3 0 6

shell
Copy
Edit

## ✅ Expected Output

Sparse Matrix 4x4
(0, 1): 5
(1, 2): 8
(2, 3): -3
(3, 0): 6

yaml
Copy
Edit

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/dsa-sparse-matrix.git
cd dsa-sparse-matrix/code/src
Make sure the file paths to matrix1.txt and matrix2.txt are correct.

Run the test script:

bash
Copy
Edit
python3 test_sparse.py
🧪 Sample Test Script (test_sparse.py)
python
Copy
Edit
from sparse_matrix import SparseMatrix

# Adjust path if needed based on where you're running this from
file1 = "../../sample_inputs/matrix1.txt"
file2 = "../../sample_inputs/matrix2.txt"

matrix1 = SparseMatrix(file1)
matrix2 = SparseMatrix(file2)

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

result = matrix1.add(matrix2)

print("\nResult of Addition:")
result.display()
👩‍💻 Author
Morsal Hakim
GitHub: @Hakim-morsal2244

📜 License
For educational use only – ALU DSA Coursework

yaml
Copy
Edit

---
