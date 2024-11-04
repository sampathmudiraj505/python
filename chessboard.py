w=input()
if w[0] in 'abcdefgh' and w[1] in '12345678':
    if w[0] in 'aceg':
      if w[1] in '1357':
          print('Black')
      else:
           print('White')   
    else:
       if w[0] in 'bdfh':
          if w[1] in '2468':
              print('Black')
          else:
            print('White')