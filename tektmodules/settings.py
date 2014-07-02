__author__ = 'tekt'

from abc import ABCMeta, abstractmethod

try:
	import tables
except ImportError:
	import shared.tektmodules.tables as tables

class Settings(metaclass=ABCMeta):
	@abstractmethod
	def get(self, key, defaultval=None):
		pass

	def getInt(self, key, defaultval=0):
		val = self.get(key, defaultval=defaultval)
		if val is None and defaultval is None:
			return None
		return int(val if val is not None else defaultval)

	def getFloat(self, key, defaultval=0.0):
		val = self.get(key, defaultval=defaultval)
		if val is None and defaultval is None:
			return None
		return float(val if val is not None else defaultval)

	def getBool(self, key, defaultval=False):
		val = self.get(key, defaultval=defaultval)
		if val == '1':
			return True
		if val == '0':
			return False
		if val in ['True', 'true', 't']:
			return True
		if val in ['False', 'false', 'f']:
			return False
		return defaultval

	def __getattr__(self, name):
		return self.get(name)

	def __getitem__(self, name):
		return self.get(name)

class DATSettings(Settings):
	def __init__(self, dat, usecols=False):
		self.dat = dat
		self.usecols = usecols

	def get(self, key, defaultval=None):
		return tables.getStr(self.dat, key, defaultval=defaultval, usecols=self.usecols)

class CHOPSettings(Settings):
	def __init__(self, chop):
		self.chop = chop

	def get(self, key, defaultval=None):
		if self.chop is None:
			return defaultval
		chan = self.chop[key]
		return chan.eval() if chan is not None else defaultval

class DictSettings(Settings):
	def __init__(self, settingsdict):
		self.settingsdict = settingsdict

	def get(self, key, defaultval=None):
		if self.settingsdict is None:
			return defaultval
		return self.settingsdict.get(key, defaultval)

class NullSettings(Settings):
	def get(self, key, defaultval=None):
		return defaultval