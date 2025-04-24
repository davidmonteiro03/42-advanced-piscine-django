from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from control.models import Article, UserFavouriteArticle


class AccessibilityTestCase(TestCase):
    def setUp(self):
        self.__username = 'new_user'
        self.__password = 'secret'

        try:
            User.objects.all().delete()
            Article.objects.all().delete()
            UserFavouriteArticle.objects.all().delete()

            User.objects.create_user(username=self.__username,
                                     password=self.__password)
        except Exception:
            print("Failed to create user. Skipping...")

    def __test_specific(self, feature):
        feature_url = reverse_lazy(feature)
        login_url = reverse_lazy('login')
        logout_url = reverse_lazy('logout')

        not_logged_user_response = self.client.get(feature_url)
        not_logged_user_last_url = not_logged_user_response.get('Location')
        if not not_logged_user_last_url:
            not_logged_user_last_url = feature_url

        self.assertNotEqual(not_logged_user_last_url, feature_url, "This page must not be accessible")

        self.client.post(login_url, {'username': self.__username,
                                     'password': self.__password})

        logged_user_response = self.client.get(feature_url)
        logged_user_last_url = logged_user_response.get('Location')
        if not logged_user_last_url:
            logged_user_last_url = feature_url

        self.assertEqual(logged_user_last_url, feature_url, "This page must be accessible")

        self.client.get(logout_url)

    def test_accessibility(self):
        self.__test_specific('favourites')
        self.__test_specific('publications')
        self.__test_specific('publish')


class CreationFormTestCase(TestCase):
    def setUp(self):
        self.__username = 'new_user'
        self.__password = 'secret'

        try:
            User.objects.all().delete()
            Article.objects.all().delete()
            UserFavouriteArticle.objects.all().delete()

            User.objects.create_user(username=self.__username,
                                     password=self.__password)
        except Exception:
            print("Failed to create user. Skipping...")

    def test_creation_form(self):
        feature_url = reverse_lazy('register')
        login_url = reverse_lazy('login')
        logout_url = reverse_lazy('logout')

        not_logged_user_response = self.client.get(feature_url)
        not_logged_user_last_url = not_logged_user_response.get('Location')
        if not not_logged_user_last_url:
            not_logged_user_last_url = feature_url

        self.assertEqual(not_logged_user_last_url, feature_url, "This page must be accessible")

        self.client.post(login_url, {'username': self.__username,
                                     'password': self.__password})

        logged_user_response = self.client.get(feature_url)
        logged_user_last_url = logged_user_response.get('Location')
        if not logged_user_last_url:
            logged_user_last_url = feature_url

        self.assertNotEqual(logged_user_last_url, feature_url, "This page must not be accessible")

        self.client.get(logout_url)


class DuplicateFavouritesTestCase(TestCase):
    def setUp(self):
        self.__username = 'new_user'
        self.__password = 'secret'
        try:
            User.objects.all().delete()
            Article.objects.all().delete()
            UserFavouriteArticle.objects.all().delete()
            User.objects.create_user(username=self.__username,
                                     password=self.__password)
        except Exception:
            print("Failed to create user. Skipping...")

    def test_duplicate_favourites(self):
        login_url = reverse_lazy('login')
        publish_url = reverse_lazy('publish')
        favourites_url = reverse_lazy('favourites')

        self.client.post(login_url, {'username': self.__username,
                                     'password': self.__password})

        self.client.post(publish_url, {'title': "Test title",
                                       'synopsis': "Test synopsis",
                                       'content': "Test content"})

        article = Article.objects.all().first()

        add_to_favourite_url = reverse_lazy('add_to_favourite', kwargs={'pk': article.pk})

        new_favourite_response = self.client.post(add_to_favourite_url)
        new_favourite_url = new_favourite_response.get('Location')
        if not new_favourite_url:
            new_favourite_url = add_to_favourite_url

        self.assertEqual(new_favourite_url, favourites_url, "You should be able to add this article to favourites.")

        duplicate_favourite_response = self.client.post(add_to_favourite_url)
        duplicate_favourite_url = duplicate_favourite_response.get('Location')
        if not duplicate_favourite_url:
            duplicate_favourite_url = add_to_favourite_url

        self.assertNotEqual(duplicate_favourite_url, favourites_url, "You should not be able to add this article to favourites.")
