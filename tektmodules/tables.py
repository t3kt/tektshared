__author__ = 'tekt'

def _prepDATArg(dat):
	return op(dat) if isinstance(dat, str) else dat

def colvals(dat, col, joiner=' '):
	dat = _prepDATArg(dat)
	if dat.numRows == 0:
		return [] if joiner is None else ""
	vals = [c.val for c in dat.col(col)]
	return vals if joiner is None else joiner.join(vals)

def rowvals(dat, row, joiner=' '):
	dat = _prepDATArg(dat)
	if dat.numRows == 0:
		return [] if joiner is None else ""
	vals = [c.val for c in dat.row(row)]
	return vals if joiner is None else joiner.join(vals)

def rowsToDicts(dat):
	dat = _prepDATArg(dat)
	if dat.numRows < 2:
		return []
	names = dat.row(0)
	return (_tableLineToDict(names, dat.row(i)) for i in range(1, dat.numRows))

def colsToDicts(dat):
	dat = _prepDATArg(dat)
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
	dat = _prepDATArg(dat)
	if vertical:
		return colToDict(dat.col(1))
	else:
		return colToDict(dat.row(1))

def appendDictRow(dat, rowdict):
	dat = _prepDATArg(dat)
	dat.appendRow([rowdict.get(name.val, '') for name in dat.row(0)])

def getStr(dat, key, usecols=False):
	dat = _prepDATArg(dat)
	cell = dat[1, key] if usecols else dat[key, 1]
	return None if cell is None or cell.val == '' else cell.val

def getFloat(dat, key, defaultval=0.0, usecols=False):
	val = getStr(dat, key, usecols)
	return float(defaultval if val is None else val)

def getInt(dat, key, defaultval=0, usecols=False):
	val = getStr(dat, key, usecols)
	return int(defaultval if val is None else val)

def getBool(dat, key, defaultval=False, usecols=False):
	val = getInt(dat, key, defaultval=1 if defaultval else 0, usecols=usecols)
	return val != 0
