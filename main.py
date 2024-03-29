"""
This script calculates the median price value of houses located in California
with linear regression and random forest model.

This script was created based on the work of the YouTube channel NeuralNine.
Video sources: https://www.youtube.com/watch?v=Wqmtf9SA_kk&t=1900s
"""

from functions import (
    loader, feature_engineering, plots, preprocess_data, model)

# %%
def main():
    
    dict_input = loader.load_data()
    
    dict_input = feature_engineering.separate_data(dict_input)
    
    plots.generate_plots(dict_input)
    
    plots.generate_scatterplot(dict_input)
    
    dict_input = preprocess_data.scale_data(dict_input)
    
    model.calc_lin_regres(dict_input)
    
    model.calc_lin_regress_scaler(dict_input)
    
    model.calc_random_forest_model(dict_input)
    
    # Warning, this function will take 5-10 minutes to be executed
    model.calc_best_random_forest_model(dict_input, flag_run=False)
    
    # Warning, this function will take 30 minutes to be executed
    # It has a bad score, like 0.05. The number of feature is too high.
    model.calc_support_vector_machine_model(dict_input, flag_run=False)
    
if __name__ == "__main__":
    main()
