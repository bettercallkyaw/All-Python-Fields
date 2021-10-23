class GrumpyDict(dict):
    def __repr__(self):
        print('NONE OF YOUR BUNISESS')
        return super().__repr__()

    def __missing__(self,key):
        print(f'YOU WANT {key}? WELL IT AINT HERE!')

    def __setitem__(self,key,value):
        print('YOU WANT OT CHANGE THE DICTIONARY?')
        print('OK FINE...')
        super().__setitem__(key,value)

    def __contains__(self,item):
        print('NO IT AINT HERE!')
        return False

data=GrumpyDict({'frist':'Tom','animal':'cat'})
print(data)
data['city']='Boston'
print(data)
'city' in data
          
               