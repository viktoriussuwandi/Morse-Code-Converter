
def get_data() :
  from morse import Morse
  morse  = Morse()
  data   = morse.df.to_dict()
  return data

def convert_result() :
  data = get_data()
  chars  = [ val for (key,val) in data['char'].items() ]
  morses = [ val for (key,val) in data['code'].items() ]

  letters = input('Insert some words : ')
  inputs  = [ i for i in letters if i != ' ' ]
  
  for i in range( len(inputs) ) :
    input_char = inputs[i].upper()
    if input_char not in chars :
      print(f'{ inputs[i] } : ')
    else :
      result = morses[ chars.index(input_char) ]
      print(f'{ inputs[i] } : { result }')

convert_result()