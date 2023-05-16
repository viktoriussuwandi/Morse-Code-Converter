
def get_data() :
  from morse import Morse
  morse  = Morse()
  data   = morse.df.to_dict()
  return data

def get_result() :
  data = get_data()
  chars  = [ val for (key,val) in data['char'].items() ]
  morses = [ val for (key,val) in data['code'].items() ]

  # inputs = input('Insert some words : ')
  inputs  = ['c', 'h', 'a', 'r', 'l', 'l', 'i', 'e']
  
  index_results = [
    chars.index(i.upper()) for i in inputs if 
    i.upper() in [v for v in chars]
  ]
  
  results = [ morses[i] for i in index_results ]

  for i in range( len(inputs)-1 ) :
    input = inputs[i].upper()
    if input not in [ c for c in chars] : print(f'{ inputs[i] } : ')
    else :
      index_result = 
      print(f'{ inputs[i] } : { results[ chars.index(input) ] }')

get_result()
