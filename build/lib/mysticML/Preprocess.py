import pandas
from mysticML.utils import Duplicate, Outlier, \
    Imputation, Transformation, Encoding, \
    FeatureSelection, FeatureExtraction, Sampling

class Preprocess(object):
    def __init__(self, df:pandas.DataFrame) ->None:
        '''
            df: accepts pandas.DataFrame
        '''
        self.report_ = []
        self.df = df

    def fit(self, target:str=None, combo:str='advanced',
            duplicate:bool=None, outlier:bool=None, impute:bool=None,
            transform:bool=None, encode:bool=None,
            feature_sel:bool=None, feature_ext:bool=None, sampling:bool=None) ->pandas.DataFrame:
        '''
            target : specify the target column.

            combo : choose from basic | intermediate | advanced

            duplicate : False to force skip, True to include (default)

            outlier : False to force skip, True to include (default)

            impute :  False to force skip, True to include (default)

            transform : False to force skip, True to include (default)

            encode : False to force skip, True to include (default)

            feature_sel : False to force skip, True to include (default)

            feature_ext : False to force skip, True to include (default)

            sampling : False to force skip, True to include (default)
        '''
        df = self.df
        Duplicate.report_.clear()
        operations = [Duplicate, Outlier, Imputation,
        Transformation, Encoding, FeatureSelection, FeatureExtraction, Sampling]

        for operation in operations:
            op = operation(df,target=target,combo=combo,duplicate=duplicate,
                           outlier=outlier,impute=impute,transform=transform,encode=encode,
                           feature_sel=feature_sel,feature_ext=feature_ext,sampling=sampling)
            df = op.apply()
            self.report_ = op.report_

        return df
