# Root module for python extensions and utilities
__author__ = 'tekt'
import td

def dbg(*args):
	for arg in args:
		print(repr(arg))

def colvals(dat, col, joiner=' '):
	if dat.numRows == 0:
		return [] if joiner is None else ""
	vals = [c.val for c in dat.col(col)]
	return vals if joiner is None else joiner.join(vals)

def rowvals(dat, row, joiner=' '):
	if dat.numRows == 0:
		return [] if joiner is None else ""
	vals = [c.val for c in dat.row(row)]
	return vals if joiner is None else joiner.join(vals)


def leapHandSelect(scriptOP):
	scriptOP.clear()
	indat = scriptOP.inputs[0]
	for r in range(1, indat.numRows):
		if indat[r, "leapraw"].val == "1" and indat[r, "leapswitch"].val == scriptOP.name + ":tracking":
			scriptOP.appendRow([indat[r, 0] + "_raw", "1"])


class UISetter:
	pass

def rowsToDicts(dat):
	if dat.numRows < 2:
		return []
	names = dat.row(0)
	return (_tableLineToDict(names, dat.row(i)) for i in range(1, dat.numRows))

def colsToDicts(dat):
	if dat.numCols < 2:
		return []
	names = dat.col(0)
	return (_tableLineToDict(names, dat.col(i)) for i in range(1, dat.numCols))

def _tableLineToDict(names, vals):
	return {names[i].val: vals[i].val for i in range(len(names))}

def rowToDict(row):
	if row is None or len(row) is 0:
		return {}
	dat = row[0].owner
	return _tableLineToDict(dat.row(0), row)

def colToDict(col):
	if col is None or len(col) is 0:
		return {}
	dat = col[0].owner
	return _tableLineToDict(dat.col(0), col)

def tableToDict(dat, vertical=True):
	if vertical:
		return colToDict(dat.col(1))
	else:
		return colToDict(dat.row(1))

def toggle_set(uiop, val, param=None):
	uiop.op("button").click(1 if val is not 0 else 0)

def slider_set(uiop, val, param=None):
	uiop.op("set").run(val)

def tuik_auto_set(uiop, val, param=None):
	uidefine = uiop.op("local/define")
	uitype = uidefine['type', 1].val if uidefine is not None else None
	if not uitype:
		raise Exception('UI operator ' + uiop.path + ' does not support type tuik_auto')
	callUISetter(uiop, uitype, val, param=param)

uiSetters = {
	'toggle': toggle_set,
	'slider': slider_set,
	'sliderhorz': slider_set,
	'slidervert': slider_set,
	'xfade': slider_set,
	'tuik_auto': tuik_auto_set
}

def callUISetter(uiop, uitype, val, param=None):
	setter = uiSetters[uitype]
	if setter is None:
		raise Exception('Unsupported UI operator type: ' + uitype)
	setter(uiop, val, param=param)




