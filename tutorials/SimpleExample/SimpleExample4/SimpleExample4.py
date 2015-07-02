from __init__ import *



class SimpleExample4(AutoForm):
	
	def __init__(self):
		super(SimpleExample4,self).__init__('Simple example 4')

		#Definition of the forms fields
		self._firstname 	= ControlText('First name', 'Default value')
		self._middlename 	= ControlText('Middle name')
		self._lastname 		= ControlText('Lastname name')
		self._fullname 		= ControlText('Full name')
		self._button 		= ControlButton('Press this button')

		#Define the organization of the forms
		self._formset = [ {'Tab1':['_firstname','||','_middlename'], 'Tab2':['_lastname']},'=','_button' ]
		#Use dictionaries for tabs
		#Use the sign '=' for a vertical splitter
		#Use the signs '||' for a horizontal splitter

		#Definition of the button action
		self._button.value = self.__buttonAction


	def __buttonAction(self):
		"""Button action event"""
		self._fullname.value = self._firstname.value +" "+ self._middlename.value +" "+ self._lastname.value




##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 app.startApp( SimpleExample4 )
	