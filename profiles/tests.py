from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order
from django.utils import timezone


# ------------ MODEL TESTING ------------

class TestUserProfile(TestCase):
    """Tests the UserProfile model in the profiles app."""

    def setUp(self):
        """
        Makes a sample user & uses signal to create a linked
        UserProfile object
        """

        username1 = "testUser"
        email1 = "testuser@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        user1 = User.objects.create(
            username=username1,
            email=email1,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user1.save()

    def test_str(self):
        """Tests the string method on the userprofile."""
        # Retrieves the most recently created profile and gets its string
        profile1 = UserProfile.objects.latest('pk')
        profile_string = str(profile1.user.username)

        # Cofirms the profile string is correct.
        self.assertEqual((profile_string), (profile1.user.username))


# ------------ VIEWS TESTING ------------

class ProfilesViewTestCase(TestCase):
    """
    Test case for testing profiles views.
    """

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Then creates a sample order.
        """

        username1 = "testUser"
        email1 = "testuser@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        username2 = "testUserStaff"
        email2 = "testuser2@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        user1 = User.objects.create(
            username=username1,
            email=email1,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2 = User.objects.create(
            username=username2,
            email=email2,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2.is_staff = True
        user2.is_superuser = True

        user1.save()
        user2.save()

        order_number = 000000000000
        user_profile = UserProfile.objects.latest('pk')
        full_name = 'test_name'
        email = 'test_email'
        phone_number = '0000000000'
        country = 'US'
        postcode = '42424'
        town_or_city = 'test_town'
        street_address1 = 'test_street'
        date = timezone.now()
        order_total = '99.99'
        grand_total = '99.99'
        original_basket = 'test_original_basket'
        stripe_pid = 'test_stripe_pid'

        order1 = Order.objects.create(
            order_number=order_number,
            user_profile=user_profile,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            country=country,
            postcode=postcode,
            town_or_city=town_or_city,
            street_address1=street_address1,
            date=date,
            order_total=order_total,
            grand_total=grand_total,
            original_basket=original_basket,
            stripe_pid=stripe_pid
            )

        order1.save()

    def test_profile_render_context(self):
        """
        Tests that the profile page is rendered properly
        with the correct context passed in.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUserStaff
        self.client.force_login(test_user_staff)

        # Try to access profile page
        response = self.client.get(f'/profile/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'profiles/profile.html', 'base.html'
            )

        # Check whether the form context item is passed in
        self.assertTrue(response.context['form'])

        # Check whether the orders context item is passed in
        self.assertTrue(response.context['orders'])

    def test_edit_profile_render_form(self):
        """
        Updates the test user's profile information.
        Checks that the profile information has been
        successfully updated.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUserStaff
        self.client.force_login(test_user_staff)

        # update the profile information
        response = self.client.post(('/profile/'), {
            'default_street_address1': "test_street_updated",
            })

        # Get the UserProfile of testUserStaff
        staffProfile = UserProfile.objects.latest('pk')

        profile_string_street = str(staffProfile.default_street_address1)

        # Check that the profile has been successfuly updated
        self.assertEqual((profile_string_street), ("test_street_updated"))
