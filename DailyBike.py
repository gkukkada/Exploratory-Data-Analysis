import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DailyBike():
	"""docstring for DailyBike"""
	def __init__(self, data):
		self.data = data

	def summary(self):

		""" It Calculates the mean, median, 1st Qu, 2nd Qu, min value, max value from the given variables. FIXME's here """

		count = 0
		detail = dict()
		for i in self.data:
			detail[i]={}
			if i=='dteday':
				detail[i]["Min"]=np.min(self.data[i], axis=0)
				detail[i]["Max"]=np.max(self.data[i], axis=0)
				###### FIXME: Calculate mean, median for Dates #######
				# detail[i]["Mean"]=np.mean(np.array(detail[i]["Min"], detail[i]["Max"]))
			else:
				detail[i]["Min"]=np.min(self.data[i], axis=0)
				detail[i]["1st Qu"]=np.percentile(self.data[i], 25)
				detail[i]["Median"]= np.median(self.data[i], axis=0)
				detail[i]["Mean"]=np.mean(self.data[i], axis=0)
				detail[i]["2nd Qu"]=np.percentile(self.data[i], 50)
				detail[i]["Max"]=np.max(self.data[i])
			count += 1
		return detail

	def createBivariate(self):

		""" This Function creates the bivariate graphs for the given dataset. """

		# This plot the graph between holiday and total rental bikes i.e:997. 
		# From this observation, the amount of bike rentals increased in holidays

		self.plot2d(self.data_values('holiday'), self.data_values('cnt'), 
			'holiday(0 or 1)', 'count of total rental bikes', 'total rental bikes in holidays')

		# This plot the graph between workingday and total rental bikes i.e:997. 
		# From this observation, the amount of bike rentals increased in workingdays
		self.plot2d(self.data_values('workingday'), self.data_values('cnt'), 
			'workingday(0[False] or 1[True])', 'count of total rental bikes', 'total rental bikes on a workingday')

		# This plot the graph between weekday and total rental bikes i.e:997. 
		# From this observation, it seems that the amount of bike rentals increased on wednesdays and thursdays.
		self.plot2d(self.data_values('weekday'), self.data_values('cnt'), 
			'weekday(day of week)', 'count of total rental bikes', 'total rental bikes on a weekday')

		# This plot the graph between month and total rental bikes i.e:997. 
		# It seems that the amount of bike rentals increased in 8th, 9th, 10th months.
		self.plot2d(self.data_values('mnth'), self.data_values('cnt'), 
			'month(1-12)', 'count of total rental bikes', 'total rental bikes month wise')

		# This plots the graph between year and total rental bikes i.e:997. 
		# From this observation, it looks like the amount of bike rentals increased in the year 2012 compared to 2011 year.
		self.plot2d(self.data_values('yr'), self.data_values('cnt'), 
			'year (0: 2011, 1:2012)', 'count of total rental bikes', 'total rental bikes in the years 2011, 2012')

		# This plot the graph between temperature and total rental bikes i.e:997. 
		# Weather has a profound effect on the bike rentals. It seems that bike rentals increased on normal temperatures
		self.plot2d(self.data_values('temp'), self.data_values('cnt'), 
			'Normalized temperature in Celsius', 'count of total rental bikes', 'total rental bikes in the given temperature')

		# This plot the graph between Humidity and total rental bikes i.e:997. 
		# It has been observed that the bike rentals increased on normal humidities.
		self.plot2d(self.data_values('hum'), self.data_values('cnt'), 
			'Normalized humidity', 'count of total rental bikes', 'total rental bikes in the given humidity')

		# This plot the graph between windspeed and total rental bikes i.e:997. 
		# you can see that there are number of points at the normalized threshold amount. It means normal humidity doesnot effect bike rentals 
		self.plot2d(self.data_values('windspeed'), self.data_values('cnt'), 
			'Normalized windspeed', 'count of total rental bikes', 'total rental bikes with given windspeed')

		# This plot the graph between temperature and casual users rental bikes i.e:367. 
		# From this observation, you can see that amount of bike rentals increased at normal temperatures.
		self.plot2d(self.data_values('temp'), self.data_values('casual'), 
			'Normalized temperature in Celsius', 'count of casual rental bikes', 'casual rental bikes with given temperature')

		# This plot the graph between temperature and registered users rental bikes i.e:886. 
		# From this observation, it seems that the amount of bike rentals increased normal temperatures.
		self.plot2d(self.data_values('temp'), self.data_values('registered'), 
			'Normalized temperature in Celsius', 'count of registered rental bikes', 'registered rental bikes with given temperature')

		# This plot the graph between season and total rental bikes i.e:997. 
		# Seasons have profound effect on the amount of bike rentals. We can observe that 2(summer),3(fall) seasons have more users who take bike rentals
		self.plot2d(self.data_values('season'), self.data_values('cnt'), 
			'season (1:spring, 2:summer, 3:fall, 4:winter)', 'count of total rental bikes', 'total rental bikes in the given season')

	def data_values(self, name):

		""" It helps to create list of data """

		arr = []
		for x in self.data[name]:
			arr.append(x)
		return arr

	def plot2d(self,x,y,x_label,y_label, plot_title):

		""" Helps the createBivariate() to plot the 2D graph between x,y data """

		plt.plot(x, y,'b*')
		plt.xlabel(x_label)
		plt.ylabel(y_label)
		plt.title(plot_title)
		plt.grid(True)
		plt.show()

	def createUnivariate(self):

		""" univariate(Histograms) """

		for col in self.data:
			if col=='dteday':
				pass
			else:
				self.histograms(self.data_values(col), col,col)

	def createMultivariate(self):	

		""" Multivariate plots """

		self.plot3d(self.data_values('season'), self.data_values('cnt'),
				self.data_values('mnth'),'Season','Total Count','Month','Season, Count, Month curve')

	def plot3d(self,x,y,z,x_label,y_label,z_label, plot_title):

		""" Helps the createMultivariate() to plot the 3D graph with x,y,z data """

		fig = plt.figure()
		ax = fig.add_subplot(111,projection='3d')
		for c, m in [('r', 'o'), ('b', '^'), ('y','*')]:
			ax.scatter(x, y, z, c=c, marker=m, label = plot_title)
		ax.set_xlabel(x_label)
		ax.set_ylabel(y_label)
		ax.set_zlabel(z_label)
		ax.set_xlim(1,4)
		ax.set_ylim(1,1000)
		ax.set_zlim(1,24)
		plt.show()

	def histograms(self,x,x_label, plot_title):

		""" Helps the createUnivariate() function to plot the 1D graph(Histograms) """

		plt.hist(x)
		plt.xlabel(x_label)
		plt.title(plot_title)
		plt.show()

if __name__ == '__main__':

	dataset = pd.read_csv('./data/day.csv')

	# data dictionary with correct data types and relevant variables
	dataset_dtype = dataset.dtypes

	# data Set: summary and variable extraction
	x = DailyBike(dataset)
	hours_df = pd.DataFrame(x.summary())
	print(dataset_dtype)

	# Create plots for given data
	# x.createUnivariate()
	# x.createBivariate()
	# x.createMultivariate()

	###### ---------- TODO ----------- #######
	# date_df = pd.Series(index=dataset_hr['dteday'])
	# print(date_df.resample().min())
	# print(np.mean(dataset_hr['dteday'],axis=0))
	# print(pd.Timestamp(dataset_hr['dteday'], axis=0))