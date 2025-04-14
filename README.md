# SYSC5807X Final Project: Software Testing Techniques

## Overview
This project demonstrates the application of two software testing techniques — Combinatorial Testing and Metamorphic Testing — on two case studies:

1. Quadratic Equation Solver  
2. Date Conversion Program  

The objective was to generate test cases, improve code coverage, perform mutation testing, and compare the effectiveness of both testing techniques in terms of coverage and fault detection.

---

## Repository Structure

The repository is organized as follows:

SYSC5807X_Final_Project/ │ 
├── date-conversion-combinatorial-testing/ │ 
└── date_conv_comb.py │ 
├── date-conversion-metamorphic-testing/ │ 
└── date_conv_meta.py │ 
├── quadratic-equation-solver-combinatorial-testing/ │ 
└── quad_comb.py │ 
├── quadratic-equation-solver-metamorphic-testing/ │ 
└── quad_meta.py │ 
├── htmlcov/ # Auto-generated coverage report 
├── .coverage # Coverage data file 
├── report.tex # Final project report (IEEE format) 
└── README.md # Project overview, instructions,
---

> Note:
> - The `venv/` folder is excluded from the repository since it contains environment-specific files that can be recreated locally using `python -m venv venv`.
>
> - The `.coverage` file and the `htmlcov/` folder are included in the repository for demonstration and grading purposes.
>   - `.coverage`: Raw coverage data.
>   - `htmlcov/`: Detailed HTML coverage report generated using Coverage.py.
>
> To regenerate the coverage report locally, use the commands provided in the "Run Coverage Analysis" section below.


---

## Testing Techniques Used

### 1. Combinatorial Testing
- Generated exhaustive test cases for input combinations.
- Covered boundary cases and edge scenarios.
- Achieved high code coverage for both case studies.

### 2. Metamorphic Testing
- Identified metamorphic relations (MRs) to generate follow-up tests.
- Verified input-output consistency across transformed inputs.
- Improved branch coverage through property-based testing.

---

## Tools Used

- Python 3.x  
- Mutatest (for Mutation Testing)  
- Coverage.py (for Code Coverage Measurement)  
- Git & GitHub (Version Control)  

---

## Results Summary

| Case Study        | Technique        | Coverage | Mutation Score | Execution Time |
|------------------|-----------------|----------|----------------|----------------|
| Quadratic Solver | Combinatorial   | 100%     | 0% (26 survived) | ~0.0041 sec   |
| Quadratic Solver | Metamorphic     | 99%      | 0% (26 survived) | ~0.0023 sec   |
| Date Conversion  | Combinatorial   | 91%      | 0% (2 survived)  | ~0.0223 sec   |
| Date Conversion  | Metamorphic     | 92%      | 0% (10 survived) | ~0.0043 sec   |

---

## How to Run

Ensure your virtual environment is activated:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Run Combinatorial Testing Programs:

# Quadratic Equation Solver - Combinatorial Testing
py quadratic-equation-solver-combinatorial-testing/quadratic_combinatorial_testing.py

# Date Conversion Program - Combinatorial Testing
py date-conversion-combinatorial-testing/date_conversion_combinatorial_testing.py


# Run Metamorphic Testing Porgrams:
# Quadratic Equation Solver - Metamorphic Testing
py quadratic-equation-solver-metamorphic-testing/quadratic_metamorphic_testing.py

# Date Conversion Program - Metamorphic Testing
py date-conversion-metamorphic-testing/date_conversion_metamorphic_testing.py

# Run Coverage Analysis:

coverage run --branch <path_to_python_file>
coverage report -m
coverage html

#Example
coverage run --branch quadratic-equation-solver-combinatorial-testing/quadratic_combinatorial_testing.py
coverage report -m
coverage html

## Project Report

The final project report is available in IEEE format in the `report.tex` file.

Author
Diana Addae
SYSC5807X - Advanced Software Testing
Carleton University
Winter 2025

References
Klara: Automatic test case generation for Python and static analysis library
https://github.com/usagitoneko97/klara

Programming Z3 (The Stanford Z3 Solver Resource)
https://theory.stanford.edu/~nikolaj/programmingz3.html

Chen, Tsong Yueh, D. H. Huang, T. H. Tse, and Zhi Quan Zhou.
Case studies on the selection of useful relations in metamorphic testing.

Category-Partition Testing (SFU Course Resource)
https://coursys.sfu.ca/2016fa-cmpt-473-d1/pages/CategoryPartition

Jia, Yue, and Mark Harman.
An analysis and survey of the development of mutation testing. IEEE Transactions on Software Engineering, 2011.
https://ieeexplore.ieee.org/document/5398526

Python Coverage.py Documentation — Measuring Code Coverage in Python
https://coverage.readthedocs.io/en/6.5.0/

Segura, Santiago, et al.
Metamorphic testing: A systematic literature review. IEEE Transactions on Software Engineering, 2016.
https://ieeexplore.ieee.org/document/7372052

