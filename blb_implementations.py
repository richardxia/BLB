
import math

from blb import *

def mean(sample):
    return sum(sample)*1.0/len(sample)

def stddev(sample):
    mn = mean(sample)
    return math.sqrt(sum([(x-mn)*(x-mn) for x in sample])*1.0/(len(sample)-1))

class MeanMean_BLB(BLB):
    def compute_estimate(self, sample):
        return mean(sample)

    def reduce_bootstraps(self, sample):
        return mean(sample)

    def average(self, sample):
        return mean(sample)

class SDMean_BLB(BLB):
    def compute_estimate(self, sample):
        return mean(sample)

    def reduce_bootstraps(self, sample):
        return stddev(sample)

    def average(self, sample):
        return mean(sample)

class MeanSD_BLB(BLB):
    def compute_estimate(self, sample):
        return stddev(sample)

    def reduce_bootstraps(self, sample):
        return mean(sample)

    def average(self, sample):
        return mean(sample)

class SDSD_BLB(BLB):
    def compute_estimate(self, sample):
        return stddev(sample)

    def reduce_bootstraps(self, sample):
        return stddev(sample)

    def average(self, sample):
        return mean(sample)

