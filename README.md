# Real2QASM ![Python_3.6](https://shields.io/badge/Python-3.6-blue) ![Qiskit_0.19.0](https://shields.io/badge/Qiskit-0.19.0-blueviolet)

Real2QASM is a script to convert quantum circuits from `Real` to `QASM`, which supports MCT-library only. The folder `source` contains the benchmark circuits considered in our paper. For more MCT circuits, please refer to [RevLib](http://www.informatik.uni-bremen.de/rev_lib/realizations.php?lib=1).

## Usage

```
usage: main.py [-h] [-o QASM] [--basis-gates BASIS_GATES]
               [--show-input-circuit] [--show-output-circuit]
               REAL

Real2QASM is a script to convert quantum circuits from `Real` to `QASM`, which
supports MCT-library only.

positional arguments:
  REAL                  Input file (.real format)

optional arguments:
  -h, --help            show this help message and exit
  -o QASM, --output QASM
                        Output file (.qasm format)
  --basis-gates BASIS_GATES
                        List of basis gate names pass to Qiskit transpiler for
                        unrolling (e.g., cx,u3). If empty, do not unroll.
  --show-input-circuit  Display the input quantum circuit.
  --show-output-circuit
                        Display the output quantum circuit.
```

The `REAL` field is required.

## Example

```
$ python main.py --basis-gates cx,u3 --show-input-circuit --show-output-circuit source/toffoli_2.real
Arguments:
  - Input file:  source/toffoli_2.real
  - Output file: toffoli_2.qasm
  - Basis gates: ['cx', 'u3']

Information of toffoli_2
  - version:	1.0
  - numvars:	3
  - variables:	a b c
  - inputs:	a b c
  - outputs:	a b c
  - constants:	---
  - garbage:	---
  - numgates:	1

Converting... done.

Input circuit:
     ┌───┐
q_0: ┤ X ├
     └─┬─┘
q_1: ──■──
       │  
q_2: ──■──
          

Unrolling... done.

Output circuit:
     ┌───────────────┐┌───┐┌───────────────┐┌───┐┌──────────────┐┌───┐┌───────────────┐┌───┐┌──────────────┐┌───────────────┐     
q_0: ┤ U3(pi/2,0,pi) ├┤ X ├┤ U3(0,0,-pi/4) ├┤ X ├┤ U3(0,0,pi/4) ├┤ X ├┤ U3(0,0,-pi/4) ├┤ X ├┤ U3(0,0,pi/4) ├┤ U3(pi/2,0,pi) ├─────
     └───────────────┘└─┬─┘└───────────────┘└─┬─┘└──────────────┘└─┬─┘└┬──────────────┤└─┬─┘└────┬───┬─────┘├───────────────┤┌───┐
q_1: ───────────────────■─────────────────────┼────────────────────■───┤ U3(0,0,pi/4) ├──┼───────┤ X ├──────┤ U3(0,0,-pi/4) ├┤ X ├
                                              │                        └──────────────┘  │       └─┬─┘      └┬──────────────┤└─┬─┘
q_2: ─────────────────────────────────────────■──────────────────────────────────────────■─────────■─────────┤ U3(0,0,pi/4) ├──■──
                                                                                                             └──────────────┘     

Saving... done.
```
