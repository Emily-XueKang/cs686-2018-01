from logger import logger
class stdout_logger(logger):
	def __init__(self, log_level):
		logger.__init__(self, log_level)
		# print("0: Starting logger (type = file) at log level {}.".format(log_level))
		# logwe(self, log_level, message)
		# print("0: Ending logger.")

	def log(self, log_level, message):
		if log_level <= self.__log_level__:
			print(str(log_level) + ": " + message)
		# if log_level <= 3:
		# 	if log_level == 1:
		# 		print("Important message.\n")
		# 	elif log_level == 2:
		# 		print("Important message.\n")
		# 		print("Less important message.\n")
		# 	elif log_level == 3:
		# 		print("Important message.\n")
		# 		print("Less important message.\n")
		# 		print("Not important message.\n")

