class LogicGate(object):
	"""Represents the most general Logic Gate object."""

	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		"""This method calls code that doesn't exist yet.
		   The class's children will define the method specific
		   to themselves."""
		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	"""Represents a binary gate, which has two pins."""

	# Child class constructors need to call their parent constructors
	# before moving onto their own distinguishing data.
	# Could also use super(BinaryGate, self).__init__(n)
	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		"""If there is a connected pin, use that. Otherwise ask for one."""

		if self.pinA == None:
			return int(input("Enter Pin A input for gate %s -->" % (self.getLabel())))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		"""If there is a connected pin, use that. Otherwise ask for one."""

		if self.pinB == None:
			return int(input("Enter Pin B input for gate %s -->" % (self.getLabel())))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self, source):
		"""Set the next pin to which to connect. Default to A 
		   if available, then B. If neither, throw an error."""

		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RuntimeError('Error: No empty pins.')

class UnaryGate(LogicGate):
	"""Represents a unary gate, which has one pin."""

	def __init__(self, n):
		LogicGate.__init__(self, n)

		self.pin = None

	def getPin(self):
		return int(input("Enter Pin input for gate %s -->" % (self.getLabel())))

	def setNextPin(self, source):
		"""Set the next pin to which to connect. Throw error if no empty pins."""

		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError('Error: No empty pins.')

class AndGate(BinaryGate):
	"""Represents a logic gate that checks for the AND operator."""

	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		"""Method to check if both pins are set to 1."""

		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	"""Represents a logic gate that checks for the AND operator."""

	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		"""Method to check if either pin is set to 1."""

		a = self.getPinA()
		b = self.getPinB()
		if a == 1 or b == 1:
			return 1
		else:
			return 0

class NotGate(UnaryGate):
	"""Represents a logic gate that checks for the NOT operator."""

	def __init__(self, n):
		UnaryGate.__init__(self, n)

	def performGateLogic(self):
		"""Method to switch the input."""

		a = self.getPin()
		if a == 1:
			return 0
		if a == 0:
			return 1

class Connector(object):
	"""Represents a connection b/w two logic gates."""

	def __init__(self, fromGate, toGate):
		"""Initializes with two gates - from and to."""
		self.fromGate = fromGate
		self.toGate = toGate

		# This will have to be created in the gate classes.
		toGate.setNextPin(self)

	def getFrom(self):
		return self.fromGate

	def getTo(self):
		return self.toGate

g1 = AndGate('G1')
g2 = AndGate('G2')
g3 = OrGate('G3')
g4 = NotGate('G4')
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print g4.getOutput()