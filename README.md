# Programming Assignment 1 - Lexer for Matrix Language
# Partners: Amanda Jenkins (alj2155) & Mike Yang (ty2467) 

## Overview

This project implements a lexer (scanner) for a matrix-based programming language. The lexer tokenizes input source code and outputs a list of tokens in the format `<Token Type, Token Value>`. The lexer also performs error checking for unknown characters and syntactical issues like missing identifiers before the assignment operator (`=`).

## Lexical Grammar

The following token types are defined in the language:

The following token types and their respective regular expressions are defined in the language:

- **ID**: Matches matrix identifiers, which are single capital letters (e.g., A, B, C).  
  **Regex**: `[A-Z]`
  
- **ASSIGN**: Assignment operator (`=`).  
  **Regex**: `=`
  
- **MATRIX**: Matches matrix elements in the format `(n,m)` where `n` and `m` are digits.  
  **Regex**: `\(\[0-9]+,[0-9]+\)`
  
- **OP_MUL**: Matrix multiplication operator (`x`).  
  **Regex**: `x`
  
- **OP_ADD**: Matrix addition operator (`+`).  
  **Regex**: `\+`
  
- **DISPLAY**: The `display` keyword used to output matrix results.  
  **Regex**: `display`
  
- **WHITESPACE**: Matches spaces and newlines (ignored for now).  
  **Regex**: `\s+`


## Sample Input Programs and Expected Outputs

### Sample Program 1: Valid Matrix Declaration and Operations

```
Input Program:
A = (1,2)
    (3,4)
B = (5,6)
    (7,8)
C = A x B
display C

Expected Output:
<ID, A>
<ASSIGN, =>
<MATRIX, (1,2)>
<MATRIX, (3,4)>
<ID, B>
<ASSIGN, =>
<MATRIX, (5,6)>
<MATRIX, (7,8)>
<ID, C>
<ASSIGN, =>
<ID, A>
<OP_MUL, x>
<ID, B>
<DISPLAY, display>
<ID, C>
```

### Sample Program 2: Missing Identifier(s) Before Assignment Operator

```
Input:

 = (1,2) 
   (3,4) 
 = (5,6) 
   (7,8) 
C = A x B 
display C&


Expected Output:
<ID, A>
<ASSIGN, =>
<MATRIX, (1,2)>
<MATRIX, (3,4)>
<ID, B>
<ASSIGN, =>
<MATRIX, (5,6)>
<MATRIX, (7,8)>
<ID, C>
<ASSIGN, =>
<ID, A>
<OP_MUL, x>
<ID, B>
<DISPLAY, display>
<ID, C>
<ERROR, Unknown character '&'>

```

### Sample Program 3: 
```
**Input:**


**Expected Output:**

```
### Sample Program 4: 
```
**Input:**


**Expected Output:**
```
### Sample Program 5: 
```

**Input:**


**Expected Output:**



```
<<<<<<< HEAD
## How to Run Shell Script for our Lexer/Scanner 
=======
## How to Run Shell Script for our Lexer/Scanner
>>>>>>> 55f0c562b8921bbdf4995b22f429334596f39607

# How to Run the Lexer/Scanner 

To run the lexer, follow these steps:

1. **Ensure you have the following files:**
   - `run_scanner.sh`: The shell script that runs the lexer.
   - `scanner2.py`: Our Python lexer script.
   - The source code file you want to analyze (e.g., `example.txt`).

2. **Make the shell script executable**:
   Open a terminal and run the following command to make the shell script executable:
   ```bash
   chmod +x run_scanner.sh


# Run the script
    ./run_scanner.sh <source_code_file> 
    For example, if your source code file is named source_code.txt, run: ./run_scanner.sh source_code.txt
