# Quantum Slot Machine

A slot machine powered by quantum randomness using Python and Q#.

This project explores how quantum mechanics can be used to generate slot machine outcomes through:

- superposition
- entanglement
- quantum measurement

Instead of using traditional random number generators, this slot machine uses quantum circuits to create unpredictable reel outcomes.

## Technology
- Python
- Q#
- VSCode


## Installation
- Clone the repoistory
- install dependencies:
- ```pip install qsharp```

## Running the project
- run the project with:
- ```python game.py```

## Example Output
- Quantum bits: 101
- Result: 💎

## How this works
The slot machine creates qubits and places them into superposition using Hadamard gates.

A qubit in superposition is represented as:

[
\frac{|0\rangle + |1\rangle}{\sqrt{2}}
]

When measured, the qubits collapse into classical bits which determine the slot machine symbols.
