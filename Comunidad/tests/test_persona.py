import unittest
import datetime
from sqlalchemy import and_

from Comunidad.persona import Persona
from Comunidad.base import Session, Base, engine


class PersonaTestCase(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        self.persona1 = Persona(nombre='Alejandra', edad=25)
        self.persona2 = Persona(nombre='Diego', edad=22)
        self.persona3 = Persona(nombre='Alejandra', edad=25)
        self.persona4 = Persona(nombre='Diana', edad=25)
        self.grupo = [self.persona1, self.persona2, self.persona3]

    def tearDown(self):
        session = Session()
        session.query(Persona).delete()
        session.commit()
        session.close()

    def test_prueba(self):
        self.assertEqual(0, 0)

    def test_constructor(self):
        self.assertEqual(self.persona1.dar_nombre(), 'Alejandra')
        self.assertEqual(self.persona1.dar_edad(), 25)

    def test_anio_nacimiento(self):
        anio_actual = datetime.datetime.now().year
        self.assertEqual(self.persona1.calcular_anio_nacimiento(True), anio_actual - 25)
        self.assertNotEqual(self.persona1.calcular_anio_nacimiento(False), anio_actual - 25)

    def test_asignacion(self):
        self.persona2.asignar_edad(28)
        self.persona2.asignar_nombre("Felipe")
        self.assertTrue(self.persona2.dar_nombre() == 'Felipe')
        self.assertTrue(self.persona2.dar_edad() == 28)

    def test_objetos_iguales(self):
        persona_nueva = self.persona1
        self.assertIsNot(self.persona1, self.persona3)
        self.assertIs(self.persona1, persona_nueva)

    def test_elemento_en_conjunto(self):
        self.assertIn(self.persona3, self.grupo)
        self.assertNotIn(self.persona4, self.grupo)

    def test_instancia_clase(self):
        self.assertIsInstance(self.persona1, Persona)
        self.assertNotIsInstance(self.grupo, Persona)

    def test_almacenar(self):
        self.persona1.almacenar()

        session = Session()
        persona = session.query(Persona).filter(
            and_(Persona.nombre == 'Alejandra', Persona.edad == 25)
        ).first()

        self.assertIsNotNone(persona)
        self.assertEqual(persona.dar_nombre(), 'Alejandra')
        self.assertEqual(persona.dar_edad(), 25)
        session.close()

    def test_recuperar(self):
        session = Session()
        session.add(self.persona2)
        session.commit()
        session.close()

        persona = Persona("", 0)
        persona.recuperar("Diego", 22)

        self.assertEqual(persona.dar_nombre(), 'Diego')
        self.assertEqual(persona.dar_edad(), 22)


if __name__ == '__main__':
    unittest.main()