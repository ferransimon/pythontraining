# inheritance
# Dependancy injection

import unittest

class Robot(object):
	"Class to move a real robot"
	def fetch(self, tool):
		print("Real movement! Fetching")
	def move_forward(self, tool):
		print("Real movement! move forward")
	def move_backward(self, tool):
		print("Real movement! move backward")
	def replace(self, tool):
		print("Real movement! replacing")

class CleaningRobot(Robot):
	"Custom robot"
	def clean(self, tool, times=10):
		super(CleaningRobot, self).fetch(tool)
		for i in range(times):
			super(CleaningRobot, self).move_forward(tool)
			super(CleaningRobot, self).move_backward(tool)
		super(CleaningRobot, self).replace(tool)

c = CleaningRobot()
c.clean("map")

class MockRobot(Robot):
	"Simulate a real robot"
	def __init__(self):
		self.tasks = []
	def fetch(self, tool):
		self.tasks.append('fetching %s' % tool)
	def move_forward(self, tool):
		self.tasks.append('forward %s' % tool)
	def move_backward(self, tool):
		self.tasks.append('backward %s' % tool)
	def replace(self, tool):
		self.tasks.append('replace %s' % tool)

class MockedCleaningRobot(CleaningRobot, MockRobot):
	'Inject a mock robot into the CleaningRobot'

class TestCleaningRobot(unittest.TestCase):
	
	def test_clean(self):
		t = MockedCleaningRobot()
		t.clean('map')
		expected = (['fetching map'] + 
					['forward map', 'backward map'] * 10 +
					['replace map'])
		self.assertEqual(t.tasks, expected)


unittest.main()

