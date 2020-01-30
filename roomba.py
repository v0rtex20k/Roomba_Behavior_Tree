# Victor Arsenescu 1/30/20
import random
import sys
class Roomba(object):
	def __init__(self, battery_level=0, spot=0, general=0 , dusty_spot=0, home_path=0):
		'''Roomba will have a blackboard w/ info and a task queue that it cycles through.'''
		self.blackboard = {
		                    "battery"    : battery_level,
		                    "spot"       : spot,
		                    "general"    : general,
		                    "dusty_spot" : dusty_spot,
		                    "home_path"  : home_path
		                  }
		self.task_queue = []

	def push(self, func):
		self.task_queue.append(func)

	def pop(self):
		top = self.task_queue.pop(0)
		return top

	def tidy_up(self):
		while self.task_queue:
			task = self.pop()
			task(self)
	def find_home(self):
		try:
			x = random.randint(0, 1000)
			y = random.randint(0, 1000)
			self.blackboard["home_path"] = (x,y)
			print("Home located:", self.blackboard["home_path"])
		except:
			# print( sys.exc_info()[0] )
			print("FAILED")

	def go_home(self):
		try:
			print("Following path:", self.blackboard["home_path"])
		except:
			print("FAILED")

	def dock(self):
		print("Docked")

	def clean_spot(self, timer):
		for rep in range(timer):
			print("RUNNING")

	def done_spot(self):
		print("DONE SPOT")
		try:
			self.blackboard["spot"] = False
		except:
			print("FAILED")

	def clean(self):
		print("Cleaning")

	def done_general(self):
		print("DONE GENERAL")
		try:
			self.blackboard["general"] = False
		except:
			print("FAILED")

def task1(R):
	if R.blackboard["battery"] < 30:
		R.find_home()
		R.go_home()
		R.dock()
		print("SUCCEEDED")
	else:
		print("FAILED")

def task2(R):
	def subtask1(R):
		print("SUBTASK1")
		if R.blackboard["spot"] is True:
			R.clean_spot(20)
			R.done_spot()
			print("SUCCEEDED")
	def subtask2(R):
		print("SUBTASK2")
		if R.blackboard["general"] is True:
			successful = False
			while not successful:
				if not R.blackboard["battery"] < 30:
					if R.blackboard["dusty_spot"] is True:
						R.clean_spot(35)
						print("SUCCEEDED") # if this part succeeds, subtask MUST succeed (not all fail)
						successful = True  # IFF succeeded
			R.done_general()

def task3(R):
	print("Doing Nothing...")

if __name__ == '__main__':
	R = Roomba()
	R.push(task1)
	R.push(task2)
	R.push(task3)
	R.tidy_up()
