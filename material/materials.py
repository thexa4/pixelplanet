from rock import Rock
from magma import Magma
from dirt import Dirt
from base import Base
from air import Air

class Materials:
	materials = {}
	
	@staticmethod
	def add_material(id, material):
		Materials.materials[id] = material;

Materials.add_material(Rock.id, Rock);
Materials.add_material(Magma.id, Magma);
Materials.add_material(Dirt.id, Dirt);
Materials.add_material(Base.id, Base);
Materials.add_material(Air.id, Air);
