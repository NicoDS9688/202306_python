"""Main"""
from classes.ninja1 import Ninja
from classes.mascota import Mascota

sapo = Mascota('Gamakichi','sapo', 'Gusanos','Ribbit ribbit')
serpiente = Mascota('Aoda', 'serpiente', 'Ratones', 'Hiss hiss')

ninja1 = Ninja('Naruto', 'Uzumaki', 'Ramen', 'Gusanos', sapo)
ninja2 = Ninja('Sasuke', 'Uchiha', 'Onigiri', 'Ratones', serpiente)
ninja1.alimentar()
ninja2.alimentar()
ninja1.caminar()
ninja2.caminar()
ninja1.banhar()
ninja2.banhar()

print(ninja1.mascota.nombre)
print(ninja2.mascota.nombre)
