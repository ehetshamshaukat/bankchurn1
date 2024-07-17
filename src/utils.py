import os
import pickle

def save_file_as_pickle(obj_path,obj_name,name):
    os.makedirs(os.path.dirname(obj_path),exist_ok=True)
    with open(obj_path,"wb") as path:
        pickle.dump(obj_name,path)
        print(name,"save in pickle format")