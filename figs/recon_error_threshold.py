from __future__ import division
import matplotlib as mpl
mpl.use('Agg') #instead of Xserver for png
import matplotlib.pyplot as plt
import sys
import numpy


def plotDataList( datasetList, filename, label="default", secondDatasetList=None, thirdDatasetList=None  ):
  
  fig = plt.figure()
  ax = fig.add_subplot(111)

  x_values = [x for x in range(len(datasetList))]
  y_values = datasetList 

  
  ax.plot(x_values,y_values, 'co',markersize=1)
  
  if secondDatasetList != None:

    x_values = [x for x in range(len(secondDatasetList))]
    y_values = secondDatasetList
    dashes = [10, 5, 10, 5]  # 10 points on, 5 off, 100 on, 5 off 
    #ax.plot(x_values, y_values, 'ro', label = 'Thresold Error')
    ax.plot(x_values, y_values, 'r-',dashes=dashes, label = 'Threshold')
    #ax.plot(x_values, y_values, 'r-',dashes=dashes)

  if thirdDatasetList != None:

    x_values = [x for x in range(len(thirdDatasetList))]
    y_values = thirdDatasetList

  
    ax.plot(x_values, y_values, 'g^', label = 'third')

 
  ax.legend(loc='upper left') 
  ax.set_ylabel("RE")
  ax.set_xlabel("Training sample")
  
  plt.tight_layout()
  fig.savefig(filename)







mpl.rcParams.update({'font.size': 18})


infile = sys.argv[1]

numbers = []
with open(infile) as fs:
  for line in fs.readlines():
    line = line.strip()
    numbers.append(float(line))

numbers = numbers[:400000]

nsamples = len(numbers)

mean_val = numpy.mean(numbers)

mean_val += (2 * numpy.std(numbers))

#mean_val = 0.28
mean_numbers = [mean_val]*nsamples



#plotDataList( numbers, "Train.pdf",  "Reconstruction Error", mean_numbers)
plotDataList( numbers, "recon_threshold_dedup.png",  "Reconstruction Error", mean_numbers)
#plotDataList( numbers, "recon_threshold_mysql.png",  "Reconstruction Error", mean_numbers)

#testfile = sys.argv[2]
#
#test_numbers = []
#with open(testfile) as fs:
#  for line in fs.readlines():
#    line = line.strip()
#    test_numbers.append(float(line))
#
#test_numbers = test_numbers[:400000]
#

#plotDataList( test_numbers, "Test.pdf",  "Reconstruction Error", mean_numbers)

