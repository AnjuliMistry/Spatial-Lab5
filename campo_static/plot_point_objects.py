import lue.data_model as ldm
import campo

dataset = ldm.open_dataset('food_environment.lue')

dataframe = campo.dataframe.select(dataset.foodstores, property_names=['x_value','healthy'])
print(dataframe)
print(type(dataframe))
campo.to_csv(dataframe,'foodstores.csv')
#campo.to_gpkg(dataframe,'foodstores.gpkg','ESPG:28992')