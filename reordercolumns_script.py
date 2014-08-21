def cook(dat):
	dat.clear()
	colnames = dat.par.string0.val.split('|')
	indat = dat.inputs[0]
	for col in colnames:
		vals = indat.col(col)
		if vals is not None:
			dat.appendCol(vals)
