__author__ = 'tekt'

from abc import ABCMeta, abstractmethod

class Settings(metaclass=ABCMeta):
	@abstractmethod
	def get(self, key, default=None):
		pass

	def __getattr__(self, name):
		return self.get(name)

class DATSettings(Settings):
	def __init__(self, dat, usecols=False):
		self.dat = dat
		self.usecols = usecols

	def get(self, key, default=None):
		if self.dat is None or self.dat.numRows == 0:
			return default
		if self.usecols:
			cell = self.dat[1, key]
		else:
			cell = self.dat[key, 1]
		return cell.val if cell is not None else default

class CHOPSettings(Settings):
	def __init__(self, chop):
		self.chop = chop

	def get(self, key, default=None):
		if self.chop is None:
			return default
		chan = self.chop[key]
		return chan.eval() if chan is not None else default

class DictSettings(Settings):
	def __init__(self, settingsdict):
		self.settingsdict = settingsdict

	def get(self, key, default=None):
		if self.settingsdict is None:
			return default
		return self.settingsdict.get(key, default)

class NullSettings(Settings):
	def get(self, key, default=None):
		return default