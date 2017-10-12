from enum import Enum

class GiveMode(Enum):
    RENT = 1
    SWAP = 2
    GIVEAWAY = 3

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
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def give_mode(self):
        return self._give_mode

    @give_mode.setter
    def give_mode(self, value):
        self._give_mode = value
    
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
        labels_formated = ''.join([f"<a href='#{label}'>#{label}</a> " for label in self._labels])
        return f"<b>{self.name}</b>  \n {self._description} \n {labels_formated}"+f"\nВладелец: @{self.current_owner.username}"
