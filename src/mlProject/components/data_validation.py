import os
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_file_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema
            all_schema_keys = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    col_dtype = data[col].dtype
                    required_dtype = all_schema[col]

                    if col_dtype != required_dtype:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else:
                        validation_status = True
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            return e
        