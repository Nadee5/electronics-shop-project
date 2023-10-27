class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = '_Файл item.csv поврежден_'

