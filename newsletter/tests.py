import datetime

from django.core import mail
from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile
from .models import Email
from django.utils.html import escape
from django.utils import timezone

# ------------ MODEL TESTING ------------

class TestEmail(TestCase):
    """Tests the Email model in the newsletter app."""

    def setUp(self):
        """
        Makes a sample Email object
        """

        email = "test@emailtest.com"
        email1 = Email.objects.create(
            email=email
            )

        email1.save()

    def test_str(self):
        """Tests the string method on the email."""
        # Retrieves the most recently created email and gets its string
        email1 = Email.objects.latest('pk')
        email_string = str(email1.email)

        # Cofirms the email string is correct.
        self.assertEqual((email_string), (email1.email))


# ------------ VIEWS TESTING ------------

class NewslettterViewTestCase(TestCase):
    """
    Test case for testing newsletter views.
    """

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Next, creates a sample email object.
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

        email = "testuser2@test.com"
        email1 = Email.objects.create(
            email=email,
            )

        email1.save()



    def test_newsletter_render_context(self):
        """
        Tests that the newsletter page is rendered properly
        """

        response = self.client.get('/newsletter/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'newsletter/email_form.html', 'base.html'
            )



    def test_email_create_render_form(self):
        """
        Creates a sample email subscription using the page form. Next,
        checks if the confirmation email is sent. Then, checks
        that that sample email object was created successfully by
        checking that the newest object is not the same
        as the object that existed previously
        """

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the user is correctly retrieved
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser
        self.client.force_login(test_user)

        # Get the ID of the most recently created email
        originalEmail = Email.objects.latest('pk')
        originalEmailId = originalEmail.pk

        # Create a new test email using the page form
        response = self.client.post(('/newsletter/'), {
            'email': 'testuser@test.com'
            })

        # Check if the confirmation email is sent
        self.assertEqual(len(mail.outbox), 1)

         # Check if the confirmation email is sent to the correct address
        self.assertIn(escape('testuser@test.com'), mail.outbox[0].to)

        # Get the most recent email
        # (should be new_test_email that we just created)
        newTestEmail = Email.objects.latest('pk')
        newTestEmailId = newTestEmail.pk

        # Check that the most recent reservation created is
        # not the original reservation, meaning a new one
        # was successfully created
        self.assertNotEqual((originalEmailId), (newTestEmailId))


    def test_email_delete_render_form(self):
        """
        First, logs in as user who is not the owner of the subscribed email address
        & tries to delete the email. Next, checks that the email was not deleted.
        Next, logs in as the email's owner and deletes the most recent 
        email using the delete view. Lastly, checks that the email was deleted successfully.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('pk')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Get the most recently subscribed email
        emailToDelete = Email.objects.latest('pk')

        # Log in as testUser (not the owner of
        # the email)
        self.client.force_login(test_user)

        # Attempt to delete the object (unsubscribe) using the delete view
        response = self.client.post(
            f'/newsletter/unsubscribe/{emailToDelete}', follow=True
            )

        # Check that the object was not deleted
        self.assertEqual(Email.objects.latest('pk'), emailToDelete)

        # Log in as testUserStaff (the owner of
        # the email)
        self.client.force_login(test_user_staff)

        # Get the to-be-deleted email's ID
        deletedEmailId = (emailToDelete.pk)

        # Delete the email using the delete view
        response = self.client.post(
            f'/newsletter/unsubscribe/{emailToDelete}', follow=True
            )
        self.assertEqual(response.status_code, 200)

        # Check if there are any email objects in the database,
        # if not, that means that the deletion was successful
        if Email.objects.exists():
            # If there are email objects remaining, we need to
            # check that the one we tried to delete has been deleted.
            # Get the ID of the latest email object in the database
            newLastEmail = Email.objects.latest('pk')
            newLastEmailId = newLastEmail.pk

            # Check if the latest email object in the database is the
            # same one that we tried to delete, if not, that
            # means the deletion was successful
            print(deletedEmailId)
            print(newLastEmailId)
            self.assertNotEqual(deletedEmailId, newLastEmailId)
