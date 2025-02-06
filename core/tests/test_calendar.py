from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from core.models.calendar import Calendar
from django.contrib.auth import get_user_model


class CalendarTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        User = get_user_model()
        # 관리자 사용자 생성
        cls.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
        )
        cls.admin_user.save()

        # 일반 사용자 생성
        cls.normal_user = User.objects.create_user(
            username="user",
            password="userpassword",
        )
        cls.normal_user.save()

        cls.calendar = Calendar.objects.create(
            name="test calendar",
            owner=cls.normal_user,
            description="test description",
        )

        # URL 설정
        cls.list_create_url = reverse("calendar-list_create")
        cls.retrieve_update_destroy_url = reverse("calendar-retrieve_update_destroy", kwargs={"pk": str(cls.calendar.id)})

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "new calendar",
            "ownerId": self.normal_user.id,
            "description": "new description",
        }


    def authenticate(self, user):
        refresh = RefreshToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_list_calendars(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "test calendar")

    def test_create_calendar(self):
        self.authenticate(self.normal_user)
        response = self.client.post(self.list_create_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Calendar.objects.count(), 2)
        self.assertEqual(Calendar.objects.get(name="new calendar").description, "new description")

    def test_retreive_calendar(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.retrieve_update_destroy_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Calendar.objects.count(), 1)
        self.assertEqual(Calendar.objects.get(name="test calendar").description, "test description")

    def test_update_calendar(self):
        self.authenticate(self.normal_user)
        response = self.client.get(self.retrieve_update_destroy_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Calendar.objects.count(), 1)
        self.assertEqual(Calendar.objects.get(name="test calendar").description, "test description")

    def test_delete_calendar(self):
        self.authenticate(self.normal_user)
        response = self.client.delete(self.retrieve_update_destroy_url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Calendar.objects.count(), 0)
