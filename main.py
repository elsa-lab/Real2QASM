'''
Real2QASM
                                                                        
Copyright (c) 2021 ELSA Lab, National Tsing Hua University
                                                                        
Real2QASM has been developed by Kuan-Yu Chang at ELSA Lab, National
Tsing Hua University, Hsinchu, Taiwan. If you use of this software
contributes to a published paper, we request that you cite our paper:
K.-Y. Chang and C.-Y. Lee, "Mapping Nearest Neighbor Compliant Quantum
Circuits onto a 2-D Hexagonal Architecture," IEEE Transactions on
Computer-Aided Design of Integrated Circuits and Systems, DOI:
10.1109/TCAD.2021.3127868.

Permission to use, copy, and modify this software and its documentation
is granted only under the following terms and conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

This software may be distributed (but not offered for sale or
transferred for compensation) to third parties, provided such third
parties agree to abide by the terms and conditions of this notice.

This software is distributed in the hope that it will be useful to the
community, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
'''

import os, argparse
import qiskit as qk

parser = argparse.ArgumentParser(description='Real2QASM is a script to convert quantum circuits from `Real` to `QASM`, which supports MCT-library only.')
parser.add_argument('REAL', type=str, 
                    help='Input file (.real format)')
parser.add_argument('-o', '--output', metavar='QASM', type=str, default=None,
                    help='Output file (.qasm format)')
parser.add_argument('--basis-gates', metavar='BASIS_GATES', type=str, default=None,
                    help='List of basis gate names pass to Qiskit transpiler for unrolling (e.g., cx,u3). If empty, do not unroll.')
parser.add_argument('--show-input-circuit', action='store_true',
                    help='Display the input quantum circuit.')
parser.add_argument('--show-output-circuit', action='store_true',
                    help='Display the output quantum circuit.')
args = parser.parse_args()

real_file = args.REAL
circ_name = os.path.basename(real_file).split('.real')[0]
qasm_file = circ_name + '.qasm' if args.output is None else args.output
basis_gates = args.basis_gates.split(',') if args.basis_gates is not None else None

print('Arguments:')
print('  - Input file:  {}'.format(real_file))
print('  - Output file: {}'.format(qasm_file))
if not basis_gates is None:
  print('  - Basis gates: {}'.format(basis_gates))

with open(real_file, 'r') as f:
  content = f.readlines()
  content = [line.replace('\n', '') for line in content]
  content = [line for line in content if not line == '']
  content = [line for line in content if line[0] != '#']

  print('\nInformation of {}'.format(circ_name))
  for info in [line for line in content if line[0] == '.'][:-2]:
    infos = [i for i in info.split(' ') if len(i) > 0]
    label = infos[0][1:]
    rest = ' '.join(infos[1:])
    print('  - {}:\t{}'.format(label, rest))

    if label == 'numvars':
      numbits = int(rest)
    elif label == 'variables':
      bit_dict = {}
      for idx, bit_name in enumerate(rest.split(' ')):
        bit_dict[bit_name] = idx

  gates = [line.rstrip() for line in content if line[0] != '.']
  print('  - numgates:\t{}'.format(len(gates)))

circ = qk.QuantumCircuit(numbits)

print('\nConverting...', end=' ')
for idx, g in enumerate(gates):
  g_split = g.split(' ')
  numctrl = int(g_split[0][1:]) - 1
  ctr_labels = g_split[1:-1]
  tar_label = g_split[-1]
  ctr_bits = [bit_dict[c] for c in ctr_labels]
  tar_bit = bit_dict[tar_label]

  if numctrl == 0:
    circ.x(tar_bit)
  elif numctrl == 1:
    circ.cx(ctr_bits[0], tar_bit)
  elif numctrl == 2:
    circ.ccx(ctr_bits[0], ctr_bits[1], tar_bit)
  else:
    circ.mcx(ctr_bits, tar_bit)
print('done.')

if args.show_input_circuit:
  print('\nInput circuit:')
  print(circ.draw())
  print()

if basis_gates is not None:
  print('Unrolling...', end=' ')
  circ = qk.transpile(circ, basis_gates=basis_gates, optimization_level=0)
  print('done.')

if args.show_output_circuit:
  if basis_gates is not None:
    print('\nOutput circuit:')
    print(circ.draw())
    print()
  else:
    print('Output circuit is same as input circuit.')

print('Saving...', end=' ')
circ.qasm(False, qasm_file)
print('done.')

