# logkit-learn
Simple Python logger for keeping track of machine learning experiments

## Example
The following example shows some functionalities of the package (full example code in `examples/example.py`):

```python

from lklearn.Logger import Logger
import datetime
import os

json_path = './demo_log.json'
if os.path.exists(json_path):
    os.remove(json_path)
    
model_info = {'date_created': datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
              'model_path':'./ResNet50/',
              'present_dir': os.getcwd(),
              'reason':'To test ResNet50',
              'architecture': 'ResNet50',
              'input_shape': (224,224,3),
              'input_info': {'nfft': 2048, 'nmels': 128, 'nperseg': 512, 'noverlap': 384},
              'output_info': {0:'chainsaw', 1:'environment'},
              'training_info': {'lr':'0.001', 'optimizer':'adam', 'batch_size':16},
              'history': {'loss':[5,4,3,2,1],'val_loss':[5,4,3,2,1]},
              'version':1.0}
              
logger = Logger(json_path, model_info)
logger.create_json() # creates a new log file for models/experiments and stores the current model/experiment
logger.db # contains the log file info


# Define a new model/experiment
# model_info = {...}

logger = Logger(json_path, model_info)
logger.update_json() # adds the new model/experiment to the log file

```
