import tkinter as tk
from tkinter import ttk
import random

#Eccezzioni per la gestione di errori
class format_invalid(Exception):
    pass
class password_small(Exception):
    pass

#Classe per definire la logica di business
class password_generator():

    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789&$!&/(=É*§°§°_ÇÉ*)"

    def __init__(self, sequenz):
        self.__sequenz = sequenz

    @property
    def sequenz(self):
        return self.__sequenz

    @sequenz.setter
    def sequenz(self, newSequenz):
        self.sequenz = newSequenz
        

