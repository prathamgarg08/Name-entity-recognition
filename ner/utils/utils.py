import os
import sys
from typing import Dict
import dill
from ner.constants import *
from ner.logger import logging
from ner.exception import NerException
import numpy as np
import yaml
from zipfile import Path
import pickle


class Mainutils:
    
    def read_yaml_file(self,filename:str)-> Dict:
        
        logging.info("Entered the read_yaml_file method of MainUtils class")
        
        try:
            with open(filename,'rb') as yaml_file:
                return yaml.safe_load(yaml_file)
            
        except Exception as e:
            raise NerException(e,sys) from e
        
    @staticmethod

    def load_pickle_file(filepath:str)->object:
        
        try:
            with open(filepath,'rb') as pickle_obj:
                obj=pickle.load(pickle_obj)
            return obj
        
        except Exception as e:
            raise NerException(e,sys) from e



    @staticmethod
    
    def dump_pickle_file(output_filepath:str,data)->None:
        
        try:
            with open(output_filepath,'wb') as encoded_file:
                pickle.dump(data,encoded_file)
        
        except Exception as e:
            raise NerException(e,sys) from e




    def load_numpy_array_data(self,filepath:str)->np.array:
        
        logging.info("Entered the load_numpy_array_data method of MainUtils class")
        
        try:
            with open(filepath,'rb') as numpy_array:
                return np.load(numpy_array)
        
        except Exception as e:
            raise NerException(e,sys) from e
    

    
    def save_numpy_array_data(self,filepath:str,array:np.array)-> str:

        logging.info("Entered the save_numpy_array_data method of MainUtils class")
        
        try:
            with open(filepath, 'wb') as file_obj:
                np.save(array,file_obj)
            logging.info("Exited the save_numpy_array_data method of MainUtils class")
            return filepath
        
        except Exception as e:
            raise NerException(e,sys) from e
        
   
    @staticmethod
    def load_object(file_path:str)->object:
        logging.info('Entered the load object method of MainUtils class')

        try:
            with open(file_path,'rb') as file_obj:
                obj=dill.load(file_obj)
            logging.info('Exited the load object method')
            return obj
        except Exception as e:
            raise NerException(e,sys) from e
    

    @staticmethod
    def save_object(file_path:str,obj:object)->None:
        logging.info('Entered the save object method of MainUtils class')

        try:
            with open(file_path,'wb') as file_obj:
                dill.dump(obj,file_obj)

                logging.info('Exited the save object method')
            return file_path
        except Exception as e:
            raise  NerException(e,sys) from e
        
    
    @staticmethod
    def read_txt_file(file_path:str)->str:
        logging.info('Entered the read text file method')
        try:
            file1=open(file_path,'r',encoding='utf8')
            text=file1.readlines()
            file1.close()

            logging.info('Exited the read text file method')
            return text
        except Exception as e:
            raise NerException(e,sys) from e
    

    
    
    @staticmethod
    def save_descriptions(descriptions,filename)->None:
        try:
            lines=list()
            for key,desc_list in descriptions.items():
                for desc in desc_list:
                    lines.append(key + " " + desc)
            data='\n'.join(lines)
            file1=open(filename,'w')
            file1.write(data)
            file1.close()
            return filename
        except Exception as e:
            raise NerException(e,sys) from e
    
    
    
    @staticmethod
    def save_txt_file(output_file_path:str,data:list)->Path:
        try:
            with open(output_file_path,'w') as file:
                file.writelines("% s\n" % line for line in data)
            return output_file_path
        except Exception as e:
            raise NerException(e,sys) from e
        
    
    @staticmethod
    def max_length_desc(descriptions:dict)->int:
        try:
            all_desc=list()
            for key in descriptions.keys():
                [all_desc.append(d) for d in descriptions[key]]
            return max(len(d.split()) for d in all_desc)
        except Exception as e:
            raise NerException(e,sys) from e

    

        
    

