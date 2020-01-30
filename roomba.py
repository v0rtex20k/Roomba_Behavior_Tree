# Victor Arsenescu 1/30/20
import time

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
		return top # in case you wanna use it
	def tidy_up(self):
		try:
			while self.task_queue:
				task = self.pop()
				task()
		except:
			print("[ERROR]: Roomba Deactivating")

if __name__ == '__main__':
	R = Roomba()
	R.push(bs)
	R.tidy_up()
