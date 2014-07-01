__author__ = 'tekt'


class UISetter:
	pass

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
