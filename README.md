# Real2QASM ![Ubuntu](https://shields.io/badge/Ubuntu-16.04-orange) ![Python_3.6](https://shields.io/badge/Python-3.6-blue) ![Qiskit_0.19.0](https://shields.io/badge/Qiskit-0.19.0-blueviolet)

Real2QASM is a script to convert quantum circuits from `Real` to `QASM`, which supports MCT-library only. The folder `source` contains the benchmark circuits considered in our paper. For more MCT circuits, please refer to [RevLib](http://www.informatik.uni-bremen.de/rev_lib/realizations.php?lib=1).

## Quick Start

```bash
$ REAL2QASM=/path/to/real2qasm
$ pip install -r ${REAL2QASM}/requirement.txt
$ mkdir unrolled_cx_u3; cd unrolled_cx_u3
$ for real in ${REAL2QASM}/source/*.real; do python ${REAL2QASM}/main.py --basis-gates cx,u3 ${real}; done
```

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

## References

If you use of Real2QASM contributes to a published paper, please cite the following BibTeX entries.

```
@article{chang2021mapping,
  author={Chang, Kaun-Yu and Lee, Chun-Yi},
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems}, 
  title={Mapping Nearest Neighbor Compliant Quantum Circuits onto a 2-D Hexagonal Architecture}, 
  year={2021},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TCAD.2021.3127868}
}

@article{aleksandrowicz2019qiskit,
  author={Aleksandrowicz, Gadi and Alexander, Thomas and Barkoutsos, Panagiotis and others},
  title={{Qiskit: An Open-source Framework for Quantum Computing}},
  month={Jan.},
  year={2019},
  publisher={Zenodo},
  doi={10.5281/zenodo.2562111},
  url={https://doi.org/10.5281/zenodo.2562111}
}

@article{cross2017open,
  title={Open quantum assembly language},
  author={Cross, Andrew W and Bishop, Lev S and Smolin, John A and Gambetta, Jay M},
  journal={arXiv preprint arXiv:1707.03429},
  year={2017}
}

@inproceedings{wille2008revlib,
  title={RevLib: An online resource for reversible functions and reversible circuits},
  author={Wille, Robert and Gro{\ss}e, Daniel and Teuber, Lisa and Dueck, Gerhard W and Drechsler, Rolf},
  booktitle={38th International Symposium on Multiple Valued Logic (ismvl 2008)},
  pages={220--225},
  year={2008},
  organization={IEEE}
}
```
