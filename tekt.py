# Root module for python extensions and utilities
__author__ = 'tekt'
import td

#import sys
#if not td.project.folder in sys.path:
#	sys.path.append(td.project.folder)

try:
	from tables import *
except ImportError:
	from shared.tektmodules.tables import *

try:
	from settings import *
except ImportError:
	from shared.tektmodules.settings import *

def dbg(*args):
	for arg in args:
		print(repr(arg))

def leapHandSelect(scriptOP):
	scriptOP.clear()
	indat = scriptOP.inputs[0]
	for r in range(1, indat.numRows):
		if indat[r, "leapraw"].val == "1" and indat[r, "leapswitch"].val == scriptOP.name + ":tracking":
			scriptOP.appendRow([indat[r, 0] + "_raw", "1"])



def getColorParams(op, prefix='color', alpha='alpha'):
	parnames = [prefix + 'r', prefix + 'g', prefix + 'b']
	if alpha is not None:
		parnames.append(alpha)
	return tuple(p.val for p in op.pars(*parnames))



