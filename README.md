# Maverick
Marverrick Programming Language

## Environment
* System: Windows/MacOs/Linux
* Language: Python 3.8

## IDE
* Pycharm 

## Python Requirements
* antlr4-python3-runtime
* llvmlite

## Installation
1. Install llvm in PC，you can compile llvm from source: https://llvm.org/docs/GettingStarted.html. 
If you use Macos, you can install llvm by homebrew.
```shell
brew install llvm
```
Remember add llvm/bin folder to $PATH.

2. Install python requirements
```shell
pip install antlr4-python3-runtime
pip install llvmlite
```
or (If you use anaconda)
```shell
conda install antlr4-python3-runtime
conda install llvmlite
```

## Folder Structure
* doc --> documents for maverick programming language
* example --> Marverick Example Code(Marverick code files are ending with .m)
* src/generator --> IR Generator
* src/parser --> Antlr4 Generated Code


## How to run

1. generate llvm code
```shell
python main.py example/xxx.m   # generate llvm code file ending with .ll in folder example
```

2. run llvm code
```shell
lli example/xxx.ll    # run files that generated in step 1.
```