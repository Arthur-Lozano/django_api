from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Note

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Note.objects.create(name='rake', owner=testuser1,description='Better for collecting leaves than a shovel.')
        test_thing.save()

    def test_things_model(self):
        thing = Note.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
