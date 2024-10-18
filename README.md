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
display C 


Expected Output:
<ERROR, Missing identifier before '='>
<ASSIGN, =>
<MATRIX, (1,2)>
<MATRIX, (3,4)>
<ERROR, Missing identifier before '='>
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




## How to Run Shell Script for our Lexer/Scanner 