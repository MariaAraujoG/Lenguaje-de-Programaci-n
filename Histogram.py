    #Alumna Araujo González María Fernanda
         #PROGRAMMING LANGUAGE


#HISTOGRAMS | CREATION OF A SUNCTION IN SYNTAX DESCRIPTION OBJECT

import random

#Criterion: Fixed definition range for continuous quantitative variables 
def Histogram(number_interval, continuous_range):
    Histogram={}
    Continuous_Complex=[random.random() for cr in range(continuous_range)]
    Range_Limit=1/number_interval

    Continuous_Complex.sort
    for nl in range(number_interval):
        Minimum_Range=nl*Range_Limit
        Maximum_Range=Minimum_Range+Range_Limit
        Interval=(round(Minimum_Range,4), round(Maximum_Range, 4))

        Frequency=[]
        for CC in Continuous_Complex:
            if CC>Minimum_Range and CC<Maximum_Range:
                Frequency.append(CC)
                Frequency_Distribution=len(Frequency)

        Histogram[Interval]=Frequency_Distribution
        Minimum_Range=Maximum_Range

    print(f'HISTOGRAM\nStatistical Distribution Diagram | {continuous_range} Quantitative Sampling Variables')
    for interval, frequency in Histogram.items():
        Histography=(f'{interval}={frequency}')
        print(Histography)

Histogram_A=Histogram(10, 50)
Histogram_B=Histogram(100, 1000)


#Criterion: Selection of the range of definition of continuous quantitative variables
def Histogram(number_interval, continuous_range, minimum, maximum):
    Histogram={}
    Continuous_Complex=[random.uniform(minimum, maximum) for cr in range(continuous_range)]
    Range_Limit=maximum/number_interval

    Continuous_Complex.sort
    for nl in range(number_interval):
        Minimum_Range=nl*Range_Limit
        Maximum_Range=Minimum_Range+Range_Limit
        Interval=(round(Minimum_Range,4), round(Maximum_Range, 4))

        Frequency=[]
        for CC in Continuous_Complex:
            if CC>Minimum_Range and CC<Maximum_Range:
                Frequency.append(CC)
                Frequency_Distribution=len(Frequency)

        Histogram[Interval]=Frequency_Distribution
        Minimum_Range=Maximum_Range

    print(f'HISTOGRAM\nStatistical Distribution Diagram | {continuous_range} Quantitative Sampling Variables')
    for interval, frequency in Histogram.items():
        Histography=(f'{interval}={frequency}')
        print(Histography)

Histogram_C=Histogram(10, 50, 0, 1)
Histogram_D=Histogram(100, 1000, 0, 1)
