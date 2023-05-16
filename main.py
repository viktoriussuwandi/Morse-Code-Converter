from morse import Morse

morse = Morse()
data = morse.df

inputs = input('Insert some words : ')

for a in inputs :
  if a.upper() in data.char : 
    print(f'{a}')