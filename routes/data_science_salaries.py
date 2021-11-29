from dataset import Dataset
from flask_restful import Resource
from flask import request
# Makes import from parent directories work
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))

parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# Makes import from parent directories work


class DataScienceSalaries(Resource):

    def __init__(self) -> None:
        super().__init__()
        self.INSUFFICIENT_PARAMS_ERR_MSG = 'Insufficient params. Necessary params: field, filter, groupby, x, y.\nFor more help go to /help'

    def get(self):
        dataset = Dataset()
        permitted_params = self._get_permitted_params(request.args)

        insufficient_params = permitted_params == self.INSUFFICIENT_PARAMS_ERR_MSG
        if insufficient_params:
            return self.INSUFFICIENT_PARAMS_ERR_MSG

        filtered_data = dataset.filter_by(
            permitted_params['field'], permitted_params['filter'])
        df_to_persist = dataset.group_by(
            df=filtered_data, by=permitted_params['groupby'], groupby_method=permitted_params['method'])
        dataset.persist_answers(df_to_persist)
        dataset.create_graph(filtered_data, permitted_params['orientation'],
                             permitted_params['x'], permitted_params['y'],
                             permitted_params['xlabel'], permitted_params['ylabel'])
        return filtered_data.to_json()

    def _get_permitted_params(self, params):
        allowed = ['field', 'filter', 'groupby', 'method',
                   'orientation', 'x', 'y', 'xlabel', 'ylabel']
        optional = ['orientation', 'xlabel', 'ylabel', 'method']
        permitted_params = {}
        for allowed_param in allowed:
            value = params.get(allowed_param)
            param_is_obrigatory_and_none = value is None and not allowed_param in optional
            if param_is_obrigatory_and_none:
                return self.INSUFFICIENT_PARAMS_ERR_MSG
            permitted_params[allowed_param] = value
        return permitted_params
