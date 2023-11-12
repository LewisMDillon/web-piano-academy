from django.test import TestCase
from django.core import mail
from .models import Contact
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils import timezone


# ------------ MODEL TESTING ------------

class TestContact(TestCase):
    """Tests the Contact model in the contact app."""
    
    def setUp(self):
        """
        Makes a sample Contact object
        """

        name = "Test Test"
        email = "test@test.com"
        subject = 'Other'
        message = 'test message'
        date_created = timezone.now()
        responded = False
        contact1 = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            date_created=date_created,
            responded=responded
            )

        contact1.save()

    def test_str(self):
        """Tests the string method on the contact object."""
        # Retrieves the most recently created contact object and gets its string
        contact1 = Contact.objects.latest('pk')
        contact_string_name = str(contact1.name)

        # Cofirms the contact object string is correct.
        self.assertEqual((contact_string_name), (contact1.name))


# ------------ VIEWS TESTING ------------

class ContactViewTestCase(TestCase):
    """
    Test case for testing Contact views.
    """

    def setUp(self):
        """
        Makes two sample users, one with superuser status and one without.
        Next, makes a sample Contact object
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

        name = "Test Test"
        email = "test@test.com"
        subject = 'Other'
        message = 'test message'
        date_created = timezone.now()
        responded = False
        contact1 = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            date_created=date_created,
            responded=responded
            )

        contact1.save()

    def test_contact_render_context(self):
        """
        Tests that the contact page is rendered properly
        """

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'contact/contact_form.html', 'base.html'
            )

    def test_contact_create_render_form(self):
        """
        Creates a new test contact object using the page form.
        Checks that the object was successfully created.
        """

        # Get the ID of the most recently created contact object
        originalContact = Contact.objects.latest('pk')
        originalContactId = originalContact.pk

        # Create a new test contact using the page form
        response = self.client.post(('/contact/'), {
            'name': 'CreateContactTest',
            'email': 'createcontacttest@test.com',
            'subject': 'Other',
            'message': 'create contact test message',
            'date_created': timezone.now(),
            'responded': False,
            })

        # Get the most recent contact object
        # (should be CreateContactTest that we just created)
        newTestContact = Contact.objects.latest('pk')
        newTestContactId = newTestContact.pk
        
        # Check that the most recent contact object created is
        # not the original contact object, meaning a new one
        # was successfully created
        self.assertNotEqual((originalContactId), (newTestContactId))

        # Check that the most recently created object is
        # our test contact object
        self.assertEqual(
            'CreateContactTest', Contact.objects.latest('pk').name
            )

    def test_contact_list_render_context(self):
        """
        First, tests that the contact list page can only be
        accessed by superusers. Then, tests that the page is
        rendered properly and the correct context is passed in
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser (no staff privileges)
        self.client.force_login(test_user)

        # Try to access contact list page (staff-only)
        response = self.client.get('/contact/list/')

        # Check that page access is forbidden
        self.assertEqual(response.status_code, 403)

        # Check that we do not reach the contact list page
        self.assertTemplateNotUsed('contact/contact_list.html')

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access reservation list page (staff-only)
        response = self.client.get('/contact/list/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Check that the page is rendered properly
        response = self.client.get('/contact/list/')
        self.assertTemplateUsed(
            response, 'contact/contact_list.html', 'base.html'
            )
        # Check that the context item is passed in
        self.assertTrue(response.context['contacts'])

    def test_contact_success_render(self):
        """
        Tests that the contact_success page is rendered properly
        """

        response = self.client.get('/contact/success/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'contact/contact_success.html', 'base.html'
            )
  
    def test_contact_detail_render_respond_delete(self):
        """
        Tests the url path by passing in the primary key of new test
        contact. Checks that the contact detail page is rendered properly.
        Checks that the contact detail view matches the test contact passed
        into the url.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Get the pk of the object
        contact1 = Contact.objects.latest('pk')

        # Log in as testUser (no staff privileges)
        self.client.force_login(test_user)

        # Try to access contact details page (staff-only)
        response = self.client.get(f'/contact/{contact1.pk}/update')

        # Check that page access is forbidden
        self.assertEqual(response.status_code, 403)

        # Check that we do not reach the contact details page
        self.assertTemplateNotUsed('contact/contact_update_form.html')

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access contact details page (staff-only)
        response = self.client.get(f'/contact/{contact1.pk}/update')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'contact/contact_update_form.html',
            'base.html'
            )

        # Cofirms that the view is
        # displaying the correct contact object.
        contact_string_name = str(contact1.name)
        contact_string_email = str(contact1.email)

        self.assertEqual((contact_string_name), ('Test Test'))
        self.assertEqual((contact_string_email), ('test@test.com'))

        # Respond to contact using the page form
        response = self.client.post((f'/contact/{contact1.pk}/update'), {
            'email_body': 'test-email-body-content'
            })

        # Check if the response email is sent
        self.assertEqual(len(mail.outbox), 1)

        # Check if the email is sent to the correct address
        self.assertIn(escape(f'{contact1.email}'), mail.outbox[0].to)

        # Check if the response email contains the correct subject & body text
        self.assertIn(escape('Other'), mail.outbox[0].subject)
        self.assertIn(escape('test-email-body-content'), mail.outbox[0].body)

        # ------------ Deleting an object ------------

        # Get the most recently created contact object
        contactToDelete = Contact.objects.latest('pk')

        # Get the to-be-deleted contact object's ID
        deletedContactId = (contactToDelete.pk)

        # Log in as testUser (not superuser)
        self.client.force_login(test_user)

        # Attempt to delete the contact object using the delete view
        response = self.client.post(
            f'/contact/{contactToDelete.pk}/delete', follow=True
            )

        # Check that access is denied
        self.assertEqual(response.status_code, 403)

        # Log in as testUserStaff (superuser)
        self.client.force_login(test_user_staff)

        # Delete the contact object using the delete view
        response = self.client.post(
            f'/contact/{contactToDelete.pk}/delete', follow=True
            )
        self.assertEqual(response.status_code, 200)

        # Check if there are any contact objects in the database,
        # if not, that means that the deletion was successful
        if Contact.objects.exists():
            # If there are contact objects remaining, we need to
            # check that the one we tried to delete has been deleted.
            # Get the ID of the last contact object in the database
            newLastContact = Contact.objects.latest('pk')
            newLastContactId = newLastContact.pk

            # Check if the last contact object in the database is the
            # same one that we tried to delete, if not, that
            # means the deletion was successful
            self.assertNotEqual(deletedContactId, newLastContactId)
