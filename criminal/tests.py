from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models.criminal import Criminal
from .models.classification import Classification


class CriminalCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.classification = Classification.objects.create(name='Class A')
        self.client.login(username='testuser', password='12345')

    def test_create_criminal(self):
        url = reverse('criminal_create')
        data = {
            'name': 'John Doe',
            'criminal_classification_id': self.classification.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Criminal.objects.count(), 1)
        self.assertEqual(Criminal.objects.first().name, 'John Doe')
        self.assertEqual(Criminal.objects.first().user_id, self.user)
