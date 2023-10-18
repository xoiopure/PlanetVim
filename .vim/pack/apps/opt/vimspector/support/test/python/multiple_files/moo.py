import cow


def Moo():
  for _ in range( 1, 100 ):
    cow.Say( 'Moo' )

  for _ in range( 1, 100 ):
    cow.Say( 'Ooom' )


if __name__ == '__main__':
  Moo()
