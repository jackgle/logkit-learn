import os
import datetime
import pandas as pd
import numpy as np

class Logger(object):
# Class for tracking machine learning experiments
    
    # json_path: path to file that will store the model records
    
    # model_info: dictionary with metadata about the current model
    
        # date_created
        # model_path: path to saved model definition and weights
        # present_dir: present working directory
        # reason: reason for creating the model
        # architecture: summary of architecture type
        # input_shape
        # input_info: dictionary of extra info about the model input
        # output_info: dictionary of model output classes
        # training_info: details about training
        # history: model training history object
        # version: model version if applicable
        # source_model_index: if this is an updated version of a previous model, specify the original model's ID

    
    def __init__(self, json_path, model_info):
        self.json_path = json_path
        self.model = dict_to_df(model_info)
        if not hasattr(model_info, 'index'):
            self.model.index = [np.nan]
        self.db = 'No json file loaded'
        
        # Load the db if it exists
        if os.path.exists(self.json_path):
            print('Reading json')
            self.db = pd.read_json(self.json_path)
        
    def create_json(self):
        if not os.path.exists(self.json_path):
            print('Creating json')
            self.model.index = [0]
            self.model.to_json(self.json_path)
            self.read_json()
            return
        else:
            raise SystemExit('Error: json file already exists.')
            return
        
    def read_json(self):
        if os.path.exists(self.json_path):
            print('Reading json')
            self.db = pd.read_json(self.json_path)
            return 
        else:
            raise SystemExit('Error: no json has been created at the given json_path. Use .create_json().')
        
    def store_json(self):
        return self.db.to_json(self.json_path)
        
    def update_json(self, append=False):
        if type(self.db)==str:
            print('Creating json')
            self.create_json()
            self.db = pd.read_json(self.json_path)
        elif (not np.isnan(self.model.index)) & (not append):
            self.db.update(self.model)
            self.store_json()
        else:
            self.model.index = [max(self.db.index)+1]
            self.db = self.db.append(self.model, sort=False)
            self.store_json()
        return
    
    def load_model(self, index):
        if isinstance(index, int):
            self.model = pd.DataFrame(self.db.loc[index]).transpose()
        elif isinstance(index, dict):
            self.model = dict_to_df(index)
            if not hasattr(index, 'index'):
                self.model.index = [np.nan]
    
    def delete_model(self, index=None):
        if index is None:
            if self.model.index is not None:
                self.db.drop(self.model.index, inplace=True)
                self.store_json()
            else:
                raise SystemExit('Error: model hasn''t been written to json yet.')
        else:
            self.db.drop(index, inplace=True)
            self.store_json()
    
def dict_to_df(dct):
    return pd.DataFrame.from_dict(dct, orient='index').transpose()
        
        