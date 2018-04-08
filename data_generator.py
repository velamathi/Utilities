
import pandas as pd
import numpy as np

"""Sample Test Data Creation
"""
x = pd.DataFrame(np.random.random((10,6)),
                 columns=['a','b',
                          'gradeDetail',
                          'gradeRecordId',
                          'lossGivenDefault',
                          'factorDetails',
                         ])

a = ['USA', 'GBP'] * 5
b = ['Under 50', 'Under 15', 'Over 60', 'Under 25' , 'Under 35'] * 2
x['a'] = a
x['b'] = b


def data_generator(data_frame, column_list_to_change, run_loops=10):
    """Function generates dummy data set using a given dataframe and
    running it run_loop times and adding a very negligible value to
    columns in column_list_to_change
    :param: data_frame : data frame that has to be used for data creation
    column_list_to_change: list of columns that has to be modified
    run_loops: number of times the columns has to be changed
    """
    new_data_frame_list = []
    while run_loops:
        df = data_frame
        for column in column_list_to_change:
            df[column] = df[column] + np.random.randn()/10000
        new_data_frame_list.append(df)
        run_loops -= 1
    return_data_frame = (pd.concat(new_data_frame_list, axis=0))
    return_data_frame = return_data_frame.reset_index()
    return return_data_frame


if __name__ == "__main__":
    data_generator(data_frame=x,
                  column_list_to_change=['gradeDetail',
                                         'gradeRecordId',
                                         'lossGivenDefault',
                                         'factorDetails']
                   )