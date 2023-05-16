import pandas as pd

class Morse :
  def __init__(self) :
    self.path = 'morse_code.csv'
    self.df   = pd.read_csv(self.path)

  def __repr__(self):
    return f'{self.df}'