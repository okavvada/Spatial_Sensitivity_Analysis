values = {1:'VALUE_',
			2: 'VALUE_1',
			3: 'VALUE_12',
			4: 'VALUE_1_13',
			5: 'VALUE_1_14',
			6: 'VALUE_1_15',
			7: 'VALUE_1_16',
			8: 'VALUE_1_17',
			9: 'VALUE_1_18',
			10: 'VALUE_1_19',
			11: 'VALUE_1_20'}

class Layers_values():
	def __init__(self, dataframe):
		self.dataframe = dataframe
		self.layer_1 = self.get_value_layers(1)
		self.layer_2 = self.get_value_layers(2)
		self.layer_3 = self.get_value_layers(3)
		self.layer_4 = self.get_value_layers(4)
		self.layer_5 = self.get_value_layers(5)
		self.layer_6 = self.get_value_layers(6)
		self.layer_7 = self.get_value_layers(7)
		self.layer_8 = self.get_value_layers(8)
		self.layer_9 = self.get_value_layers(9)
		self.layer_10 = self.get_value_layers(10)
		self.layer_11 = self.get_value_layers(11)
		self.name = self.get_name_pont()

	def get_value_layers(self, layer_name):
		layer_value = self.dataframe.iloc[0][values[layer_name]]
		return layer_value

	def get_name_pont(self):
		layer_value = self.dataframe.iloc[0]['id_val']
		return layer_value






