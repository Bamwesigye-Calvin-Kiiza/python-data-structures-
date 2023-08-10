import random


class Hat:
    halls = ['lumumba','mitchel','africa','mary stuart','livingstone','nkrumah']
    
    @classmethod
    def sort(cls,name):
        hall = random.choice(cls.halls)
        print(f'{name} is in {hall}')


Hat.sort('harry')