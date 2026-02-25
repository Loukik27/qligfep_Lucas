import os
# Root directory of the setup FEP modules
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

# The directories to the input FF and run related input files are given here
FF_DIR = os.path.join(ROOT_DIR, "FF")
INPUT_DIR = os.path.join(ROOT_DIR, "INPUTS")
# Dicionary of locations of Q executables
Q_DIR = {'LOCAL': '/home/lucasmat002/software/Q/src/q6/bin/q6/',
         'CESGA': '/mnt/netapp1/Store_CSIC/home/csic/edc/lmp/Q/src/q6/bin/q6/'
        }
BIN = os.path.join(ROOT_DIR, "bin")
SCHROD_DIR = '/home/lucasmat002/Q/src/q6/bin/q6/'

DEFAULT = 'LOCAL'

# CLUSTER INPUTS. To add your own cluster, use the same input as below


LOCAL = {'NODES'        : '1',
       'NTASKS'       : '16',
       'TIME'         : '0-06:00:00',  # d-hh:mm:ss
       'PARTITION'    : '',
       'EXCLUDE'      : '',
       'MODULES'      : 'module load cesga/2020\nmodule load gcc/system\nmodule load openmpi/4.0.5_ft3',
       'QDYN'         : 'qdyn=' + Q_DIR['LOCAL'] + 'qdynp',
       'QPREP'        : Q_DIR['LOCAL'] + 'qprep',
       'QFEP'         : Q_DIR['LOCAL'] + 'qfep',
       'QCALC'        : Q_DIR['LOCAL'] + 'qcalc'
      }
CESGA = {'NODES'        : '1',
       'NTASKS'       : '16',
       'TIME'         : '0-06:00:00',  # d-hh:mm:ss
       'PARTITION'    : '',
       'EXCLUDE'      : '',
       'MODULES'      : 'module load cesga/2020\nmodule load gcc/system\nmodule load openmpi/4.0.5_ft3',
       'QDYN'         : 'qdyn=' + Q_DIR['CESGA'] + 'qdynp',
       'QPREP'        : Q_DIR['CESGA'] + 'qprep',
       'QFEP'         : Q_DIR['CESGA'] + 'qfep',
       'QCALC'        : Q_DIR['CESGA'] + 'qcalc'
      }
