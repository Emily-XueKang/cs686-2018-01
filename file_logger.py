from logger import logger
class file_logger(logger):
	def __init__(self, log_level):
		logger.__init__(self, log_level)
		self.output = open('file_log.txt', 'a+')
		# message = "0: Starting logger (type = stdout) at log level {}.".format(log_level)
		# log(self, log_level, message)
		# message += '\n' + "Enging logger"
		# f = open('file_log.txt','w')
		# f.write(message)
		# f.close()

	def log(self, log_level, message):
		if log_level <= self.__log_level__:
			self.output.write(str(log_level) + ': ' + message + '\n')
		# if log_level <= 3:
		# 	if log_level == 1:
		# 		message+= "\nImportant message."
		# 	elif log_level == 2:
		# 		message+= "\nImportant message."
		# 		message+="\nLess important message."
		# 	elif log_level == 3:
		# 		message+= "\nImportant message."
		# 		message+="\nLess important message."
		# 		message+="\nNot important message."
