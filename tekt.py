# Root module for python extensions and utilities
__author__ = 'tekt'
import td


def colvals(dat, col, joiner=' '):
	if dat.numRows == 0:
		return [] if joiner is None else ""
	vals = [c.val for c in dat.col(col)]
	return vals if joiner is None else joiner.join(vals)


def leapHandSelect(scriptOP):
	scriptOP.clear()
	indat = scriptOP.inputs[0]
	for r in range(1, indat.numRows):
		if indat[r, "leapraw"].val == "1" and indat[r, "leapswitch"].val == scriptOP.name + ":tracking":
			scriptOP.appendRow([indat[r, 0] + "_raw", "1"])


# class FProxy:
# 	def __init__(self, fname, modpath='/_/local/modules/tekt'):
# 		self.fname = fname
# 		self.mod = td.mod(modpath)
#
# 	def __call__(self, *args, **kwargs):
# 		f = getattr(self.mod, self.fname)
# 		return f(*args, **kwargs)
#
#
# def fproxy(tmod, name):
# 	pass

class ExtBase:
	def __init__(self, comp):
		self.comp = comp
		pass

class LeapInExt:
	def __init__(self, comp):
		self.comp = comp

	def inputcol(self, col):
		return colvals(self.comp.op('activeleapinputmap'), col)


