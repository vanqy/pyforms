#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__      = "Ricardo Ribeiro"
__credits__     = ["Ricardo Ribeiro"]
__license__     = "MIT"
__version__     = "0.0"
__maintainer__  = "Ricardo Ribeiro"
__email__       = "ricardojvr@gmail.com"
__status__      = "Development"


import os
import pickle
import pyforms.Utils.tools as tools
from PyQt4 import uic, QtGui
from pyforms.Controls.ControlBase import ControlBase

class ControlNumber(ControlBase):

	def __init__(self, label = "", defaultValue = 0, min = 0, max = 100):
		self._min = min
		self._max = max
		ControlBase.__init__(self, label, defaultValue)
		
		
		self._label = label
		self._value = defaultValue
	 

	def initForm(self):
		control_path = tools.getFileInSameDirectory(__file__,"number.ui")
		self._form = uic.loadUi( control_path )
		self.label = self._label
		self.value = self._value 
		self.form.spinBox.valueChanged.connect( self.valueChanged )
		self.min = self._min
		self.max = self._max

	def valueChanged(self, value):
		self._updateSlider = False
		self.value = value
		self._updateSlider = True

	############################################################################
	############ Properties ####################################################
	############################################################################

	@property
	def label(self): return self.form.label.text()

	@label.setter
	def label(self, value):
		self.form.label.setText(value)

	@property
	def value(self): 
		self._value = self.form.spinBox.value()
		return self._value

	@value.setter
	def value(self, value):
		ControlBase.value.fset(self,value)
		self.form.spinBox.setValue(int(value))


	@property
	def min(self):
		return self.form.spinBox.minimum()
	
	@min.setter
	def min(self, value): self.form.spinBox.setMinimum(value)

	@property
	def max(self):
		return self.form.spinBox.maximum()
	
	@max.setter
	def max(self, value): self.form.spinBox.setMaximum(value)