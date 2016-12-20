from __future__ import division
import numpy as np


class Parameters_values():
    def __init__(self):
        self.weight_1 = 0.5 #percent of pop served
        self.weight_2 = 0.5
        self.weight_3 = 0.5
        self.weight_4 = 0.5
        self.weight_5 = 0.5
        self.weight_6 = 0.5
        self.weight_7 = 0.5
        self.weight_8 = 0.5
        self.weight_9 = 0.5
        self.weight_10 = 0.5

    def max_min(self, percent):
        maxmin = {
        'weight_1_min': (1-percent)*self.weight_1,
        'weight_2_min': (1-percent)*self.weight_2,
        'weight_3_min': (1-percent)*self.weight_3,
        'weight_4_min': (1-percent)*self.weight_4,
        'weight_5_min': (1-percent)*self.weight_5,
        'weight_6_min': (1-percent)*self.weight_6,
        'weight_7_min': (1-percent)*self.weight_7,
        'weight_8_min': (1-percent)*self.weight_8,
        'weight_9_min': (1-percent)*self.weight_9,
        'weight_10_min': (1-percent)*self.weight_10,
        'weight_1_max': (1+percent)*self.weight_1,
        'weight_2_max': (1+percent)*self.weight_2,
        'weight_3_max': (1+percent)*self.weight_3,
        'weight_4_max': (1+percent)*self.weight_4,
        'weight_5_max': (1+percent)*self.weight_5,
        'weight_6_max': (1+percent)*self.weight_6,
        'weight_7_max': (1+percent)*self.weight_7,
        'weight_8_max': (1+percent)*self.weight_8,
        'weight_9_max': (1+percent)*self.weight_9,
        'weight_10_max': (1+percent)*self.weight_10}
        
        return maxmin

    def uncertainty(self, percent):
        new_params = Parameters_values()
        maxmin = self.max_min(percent)
        new_params.weight_1 = np.random.uniform(maxmin['weight_1_min'],maxmin['weight_1_max'])
        new_params.weight_2 = np.random.uniform(maxmin['weight_2_min'],maxmin['weight_2_max'])
        new_params.weight_3 = np.random.uniform(maxmin['weight_3_min'],maxmin['weight_3_max'])
        new_params.weight_4 = np.random.uniform(maxmin['weight_4_min'],maxmin['weight_4_max'])
        new_params.weight_5 = np.random.uniform(maxmin['weight_5_min'],maxmin['weight_5_max'])
        new_params.weight_6 = np.random.uniform(maxmin['weight_6_min'],maxmin['weight_6_max'])
        new_params.weight_7 = np.random.uniform(maxmin['weight_7_min'],maxmin['weight_7_max'])
        new_params.weight_8 = np.random.uniform(maxmin['weight_8_min'],maxmin['weight_8_max'])
        new_params.weight_9 = np.random.uniform(maxmin['weight_9_min'],maxmin['weight_9_max'])
        new_params.weight_10 = np.random.uniform(maxmin['weight_10_min'],maxmin['weight_10_max'])
        
        return new_params

    def sensitivity(self, parameter, direction):
        new_params = Parameters_values()
        maxmin = self.max_min()
        if parameter == 'weight_1':  
            if direction == 'minus':  
                new_params.weight_1 = self.weight_1 - (maxmin['weight_1_max'] - maxmin['weight_1_min'])/10 
            if direction == 'plus':
                new_params.weight_1 = self.weight_1 + (maxmin['weight_1_max'] - maxmin['weight_1_min'])/10 
        if parameter == 'weight_2':  
            if direction == 'minus':  
                new_params.weight_2 = self.weight_2 - (maxmin['weight_2_max'] - maxmin['weight_2_min'])/10 
            if direction == 'plus':
                new_params.weight_2 = self.weight_2 + (maxmin['weight_2_max'] - maxmin['weight_2_min'])/10 
        if parameter == 'weight_3':  
            if direction == 'minus':  
                new_params.weight_3 = self.weight_3 - (maxmin['weight_3_max'] - maxmin['weight_3_min'])/10 
            if direction == 'plus':
                new_params.weight_3 = self.weight_3 + (maxmin['weight_3_max'] - maxmin['weight_3_min'])/10 
        if parameter == 'weight_4':  
            if direction == 'minus':  
                new_params.weight_4 = self.weight_4 - (maxmin['weight_4_max'] - maxmin['weight_4_min'])/10 
            if direction == 'plus':
                new_params.weight_4 = self.weight_4 + (maxmin['weight_4_max'] - maxmin['weight_4_min'])/10 
        if parameter == 'weight_5':  
            if direction == 'minus':  
                new_params.weight_5 = self.weight_5 - (maxmin['weight_5_max'] - maxmin['weight_5_min'])/10 
            if direction == 'plus':
                new_params.weight_5 = self.weight_5 + (maxmin['weight_5_max'] - maxmin['weight_5_min'])/10 
        if parameter == 'weight_6':  
            if direction == 'minus':  
                new_params.weight_6 = self.weight_6 - (maxmin['weight_6_max'] - maxmin['weight_6_min'])/10 
            if direction == 'plus':
                new_params.weight_6 = self.weight_6 + (maxmin['weight_6_max'] - maxmin['weight_6_min'])/10 
        if parameter == 'weight_7':  
            if direction == 'minus':  
                new_params.weight_7 = self.weight_7 - (maxmin['weight_7_max'] - maxmin['weight_7_min'])/10 
            if direction == 'plus':
                new_params.weight_7 = self.weight_7 + (maxmin['weight_7_max'] - maxmin['weight_7_min'])/10 
        if parameter == 'weight_8':  
            if direction == 'minus':  
                new_params.weight_8 = self.weight_8 - (maxmin['weight_8_max'] - maxmin['weight_8_min'])/10 
            if direction == 'plus':
                new_params.weight_8 = self.weight_8 + (maxmin['weight_8_max'] - maxmin['weight_8_min'])/10 
        if parameter == 'weight_9':  
            if direction == 'minus':  
                new_params.weight_9 = self.weight_9 - (maxmin['weight_9_max'] - maxmin['weight_9_min'])/10 
            if direction == 'plus':
                new_params.weight_9 = self.weight_9 + (maxmin['weight_9_max'] - maxmin['weight_9_min'])/10 
        if parameter == 'weight_10':  
            if direction == 'minus':  
                new_params.weight_10 = self.weight_10 - (maxmin['weight_10_max'] - maxmin['weight_10_min'])/10 
            if direction == 'plus':
                new_params.weight_10 = self.weight_10 + (maxmin['weight_10_max'] - maxmin['weight_10_min'])/10 
        
        return new_params


def run_simulation(layers, percent, analysis = 'Normal'):
    Parameters = Parameters_values()
    if analysis == 'Uncertainty':
            perturb_Parameters = Parameters.uncertainty(percent)
            Parameters = perturb_Parameters
    if analysis == 'Sensitivity':
            perturb_Parameters = Parameters.sensitivity(parameter, direction)
            Parameters = perturb_Parameters

    output = (layers.layer_1*Parameters.weight_1 + layers.layer_2*Parameters.weight_2 + layers.layer_3*Parameters.weight_3 + layers.layer_4*Parameters.weight_4 + layers.layer_5*Parameters.weight_5 + layers.layer_6*Parameters.weight_6 +
        layers.layer_7*Parameters.weight_7 + layers.layer_8*Parameters.weight_8 + layers.layer_9*Parameters.weight_9 + layers.layer_10*Parameters.weight_10)

    return output



