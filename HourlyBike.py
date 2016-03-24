import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from DailyBike import *

class HourlyBike(object):
	"""docstring for HourlyBike"""
	def __init__(self, data, hourlyObject):
		self.data = data
		self.obj = hourlyObject

	def summary(self):

		""" It Calculates the mean, median, 1st Qu, 2nd Qu, min value, max value from the given variables. 
		Referred from DailyBike class, Look into DailyBike.summary(). """

		return self.obj.summary()

	def createUnivariate(self):

		""" This Function creates the Uni graphs for the given dataset. 
			Look into DailyBike.createUnivariate() """

		self.obj.createUnivariate()

	def createBivariate(self):

		""" This Function creates the bivariate graphs for the given dataset. 
			Look into DailyBike.createBivariate() """

		self.obj.createBivariate()
		self.obj.plot2d(self.obj.data_values('hr'), self.obj.data_values('cnt'), 
				'hours', 'count of total rental bikes', 'hours vs count')

	def createMultivariate(self):

		""" This Function creates the multivariate graphs for the given dataset. """

		self.obj.plot3d(self.obj.data_values('season'), self.obj.data_values('cnt'),
				self.obj.data_values('hr'),'Season','Total Count','Hour','Season, Count, Hour curve')


if __name__ == '__main__':

	data = pd.read_csv('./data/hour.csv')
	dailyObject = DailyBike(data)
	hourlyObject = HourlyBike(data, dailyObject)

	# data Set: summary and variable extraction
	dataset_dtype = data.dtypes

	# data dictionary with correct data types and relevant variables
	day_df = pd.DataFrame(hourlyObject.summary())
	print(day_df)

	# Plots the graphs for various versions.
	# hourlyObject.createUnivariate()
	# hourlyObject.createBivariate()
	# hourlyObject.createMultivariate()
