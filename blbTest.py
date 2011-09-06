import unittest
from blb import *
from blb_implementations import *

class blbTest(unittest.TestCase):
   
    """
    this method tests the correctness of the "correct" algorithm by testing to see if it properly
    computes the statistic it is intended to by comparing that computed stat with the same computed
    stat on the complete set of data. it sets all combining functions after the original to simply
    the mean so as to ensure an easy check...(assumes that the last two combining functions are 
    implemented correctly)
    """
    def test_correct_blb(self):       
        reduce_bootstraps = correct_blb.reduce_bootstraps       
        correct_blb.reduce_bootstraps = mean 
        
        actual_result = correct_blb.compute_estimate(data)                
        test_results = []
        for i in range(num_results_compared):
            test_results.append(correct_blb.run(data))
        derived_result = mean(test_results)  
        
        relative_error = abs(actual_result - derived_result)/actual_result    
        print("TESTING CORRECT_BLB ----------------")
        print("For testing correct_blb, the actual result from the data is", actual_result)             
        print("For testing correct_blb, the derived result is", derived_result)
        print("This is a relative error of", relative_error)
        print("DONE TESTING CORRECT_BLB -------------")
        
        correct_blb.reduce_bootstraps = reduce_bootstraps
      
    def test_compute_estimate(self):
        test_result = test_blb.compute_estimate(data)
        correct_result = correct_blb.compute_estimate(data)
        self.assertEqual(test_result, correct_result)
    
    def test_reduce_bootstraps(self):
        test_result = test_blb.reduce_bootstraps(data)
        correct_result = correct_blb.reduce_bootstraps(data)
        self.assertEqual(test_result, correct_result)
                
    def test_average(self):
        test_result = test_blb.average(data)
        correct_result = correct_blb.average(data)
        self.assertEqual(test_result, correct_result)
    
    """
    informal varying of parameters, just basically to test if not using the defaults results in an error
    """  
    def test_vary_params(self): 
        for i in range(10):  ##numbers here are informally estimated...can be varied for more/less accuracy
            subsample_len_exp = random.uniform(.5, .99) 
            num_bootstraps = int(random.randint(10,50))
            num_subsamples = int(random.randint(40, 150))           
            vtest_blb = test_class(num_subsamples, num_bootstraps, subsample_len_exp)
            vcorrect_blb = correct_class(num_subsamples, num_bootstraps, subsample_len_exp)  
            
            test_result = vtest_blb.run(data)
            correct_result = vcorrect_blb.run(data)
            rel_error = abs(test_result - correct_result) / correct_result
            
            self.assertLessEqual(rel_error, max_error)
        
    def test_final_answer(self):        
        self.assertLessEqual(average_relative_result_error(), max_error)
        
def average_relative_result_error():
    test_results = []
    correct_results = []  
    for i in range(num_results_compared):
        test_results.append(test_blb.run(data))
        correct_results.append(correct_blb.run(data))
    test_average = sum(test_results) / num_results_compared
    correct_average = sum(correct_results)  / num_results_compared
    relative_error = abs(test_average - correct_average)/correct_average
    print('The test average result is', test_average)
    print('The correct average result is', correct_average)
    print('The relative error is', relative_error)
    
    return relative_error

def gauss_distribution(length, mean, stddev):
    distribution = []
    for i in range(length):
        distribution.append(random.gauss(mean, stddev))  
    return distribution
    
if __name__ == '__main__':
        data = gauss_distribution(500, 100, 10)  #(length, mean, stddev)
               
        test_class = MeanSD_BLB ##IMPLEMENTATION TO BE TESTED
        correct_class = MeanSD_BLB ##CORRECT IMPLEMENTATION
        
        input_params = [100, 25,.5]   #[num_subsamples=100, num_bootstraps=25, subsample_len_exp=.5]
       
        if not input_params:
            test_blb = test_class()
            correct_blb = correct_class()
        else:
            test_blb = test_class(input_params[0], input_params[1], input_params[2])
            correct_blb = correct_class(input_params[0], input_params[1], input_params[2])
        
        num_results_compared = 15 ## number of times they will be run and compared against each other
        max_error = .05 ## max difference the average of the results can be for the test implementation to be considered correct       
        
        unittest.main()

