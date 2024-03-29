# Another class with a class attribute, used for validation purposes
class Pet:
    allowed=['cat','dog','fish','rat']

    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f'you can not have a {species} pet!')
        self.name=name
        self.species=species

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f'you can not have a {species} pet!')
        self.species=species

cat=Pet('Blue','cat')
dog=Pet('Wyatt','dog')
print(type(cat))
print(type(dog))