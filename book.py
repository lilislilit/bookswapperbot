class Book(object):
    def __init__(self, name, owner):
        self._name = name
        self._current_owner = owner
        self._description = None #Description and labels should be set in builder
        self._labels = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.name = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    
    @property
    def current_owner(self):
        return self._current_owner

    @current_owner.setter
    def current_owner(self, value):
        self._current_owner = value

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = value
    
    def __str__(self):
        labels_formated = ''.join([f"#{label}" for label in self._labels])
        return f"<b>{self.name}</b>  \n {self._description} \n {labels_formated}"+f"\nВладелец: @{self.current_owner.username}"
