"""Main class representing the BLB algorithm.

"""

import random

class BLB:
    def __init__(self, num_subsamples=100, num_bootstraps=25, 
                 subsample_len_exp=0.5):
        self.num_subsamples = num_subsamples
        self.num_bootstraps = num_bootstraps
        self.subsample_len_exp = subsample_len_exp

    def run(self, data):
        subsample_estimates = []
        for i in range(self.num_subsamples):
            subsample = self.__subsample(data, self.subsample_len_exp)
            bootstrap_estimates = [] 
            for j in range(self.num_bootstraps):
                bootstrap = self.__bootstrap(subsample)
                estimate = self.compute_estimate(bootstrap)
                bootstrap_estimates.append(estimate)
            subsample_estimates.append(self.reduce_bootstraps(bootstrap_estimates))
        return self.average(subsample_estimates)
    
    def __subsample(self, data, subsample_len_exp):
        subsample_len = int(len(data) ** subsample_len_exp)
        subsample = random.sample(data, subsample_len)
        return subsample

    def __bootstrap(self, data):
        bootstrap = [random.choice(data) for i in range(len(data))]
        return bootstrap

    # These three methods are to be implemented by subclasses
    def compute_estimate(self, sample):
        '''The actual statistic being computed. E.g. mean, standard deviation,
        etc. This is run on just the bootstrapped samples in the inner loops.
        '''
        TypeError('compute_estimate not defined')

    def reduce_bootstraps(self, sample):
        TypeError('reduce_bootstraps not defined')

    def average(self, sample):
        TypeError('average not defined')

