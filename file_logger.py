from logger import logger
class file_logger(logger):
	#file_logger(3)
	logger(3)
	def __init__(self, log_level, filename='file_log.txt'):
		logger.__init__(self, log_level)
		self.output = open(filename, 'a+')

	def log(self, log_level, message):
		if log_level <= self.__log_level__:
			self.output.write(str(log_level) + ': ' + message + '\n')
