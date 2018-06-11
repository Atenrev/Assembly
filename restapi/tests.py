from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from rest_framework.test import force_authenticate


from django.contrib.auth.models import User
from citizens.models import *
from votes.models import *

# Create your tests here.
class CitizenTestCase(TestCase):

    def setUp(self):
        self.user_username = "test"
        self.user_email = "test@test"
        self.user_password = "test"
        self.user = User(id=1, username=self.user_username, email=self.user_email,
            password=self.user_password)
        self.profile_national_id = "1234"
        self.profile_user = Profile(user=self.user,
            national_id=self.profile_national_id)

    def test_model_can_create_a_citizen(self):
        old_count = Profile.objects.count()
        self.user.save()
        self.profile_user.save()
        new_count = Profile.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewCitizenTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.citizen_data = {
            "national_id": "1234",
            "user": {
                "username": "test",
                "email": "test@test.com",
                "password": "test",
                "first_name": "test",
                "last_name": "test"
            }
        }
        self.response = self.client.post(
            reverse('citizen_create'),
            self.citizen_data,
            format="json")

    def test_api_can_create_a_citizen(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_citizen(self):
        token = Token.objects.get(user__username='test')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        profile = Profile.objects.get()
        response = self.client.get(
            reverse('citizen_record',
            kwargs={'user__username': profile.user.username}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, profile)


class ViewVoteTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User(id=1, username="test", email="test@test.com",
            password="test")
        self.user.save()
        self.phase = Phase(slug="review", title="review")
        self.phase.save()
        self.proposal = Proposal(
            id=1,
            title="proposal",
            description="proposal",
            phase=self.phase,
            user=self.user
        )
        self.proposal.save()

    def test_api_can_vote_review(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.vote_data = {
            "phase" : self.phase.slug,
            "proposal" : self.proposal.id,
            "user" : self.user.id
        }
        response = self.client.post(
            reverse('reviewing_vote_proposal'),
            self.vote_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
