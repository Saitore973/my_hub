from django.test import TestCase
from .models import *

# Create your tests here.

# test profile class
class ProfileTestCase(TestCase):
    def setUp(self):
        # create a user
        self.user = User.objects.create(
            username='test_user',
            full_name='john doe',
        )

        Profile.objects.create(
            bio='test bio',
            profilePhoto='https://res.cloudinary.com/james-m/image/upload/v1646636668/bbejbztp3i23jtfgoxzu.webp',
            user=self.user
        )

    def test_bio(self):
        profile = Profile.objects.get(user_id=self.user.id)
        self.assertEqual(profile.bio, 'test bio')

