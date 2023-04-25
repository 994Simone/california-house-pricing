import matplotlib.pyplot as pltimport seaborn as sns# %%def generate_plots(dict_input: dict) -> None:        plt.figure(figsize=(15, 8))        sns.heatmap(        dict_input['train_data'].corr(),        annot=True,        cmap="YlGnBu")        plt.show()    plt.close()        # %%def generate_scatterplot(dict_input: dict) -> None:    plt.figure(figsize=(15, 8))        sns.scatterplot(        x="latitude",        y="longitude",        data=dict_input['train_data'],        hue="median_house_value",        palette='coolwarm')        plt.show()    plt.close()