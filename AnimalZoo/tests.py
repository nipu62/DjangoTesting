from django.test import TestCase
from django.urls import reverse
from AnimalZoo.models import Animal

class AnimalTestBase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")


class AnimalModelTestCase(AnimalTestBase):
    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')


class AnimalViewTestCase(AnimalTestBase):
    def test_animal_view(self):
        response = self.client.get(reverse('animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'animals.html')
        self.assertContains(response, "Lion")
