from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order
from profiles.models import UserProfile
from products.models import Product
from django.utils import timezone

import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()


# ------------ MODEL TESTING ------------

class TestOrder(TestCase):
    """Tests the Order model in the checkout app."""
    
    def setUp(self):
        """
        Makes a sample user with a linked UserProfile.
        Then makes a sample Order object
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

    def test_str(self):
        """Tests the string method on the order."""
        # Retrieves the most recently created order and gets its string
        order1 = Order.objects.latest('pk')
        order_string = str(order1.full_name)

        # Cofirms the email string is correct.
        self.assertEqual((order_string), (order1.full_name))


# ------------ VIEWS TESTING ------------

class CheckoutViewTestCase(TestCase):
    """
    Test case for testing checkout views.
    """

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Then creates a test product.
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

        name = "test_product"
        description = "test_product_description"
        price = '999.99'
        date_created = timezone.now()
        product1 = Product.objects.create(
            name=name,
            description=description,
            price=price,
            date_created=date_created
            )

        product1.save()

        # Get the most recently created product (test product)
        product1 = Product.objects.latest('pk')

        # Try to add the test product to the basket
        response = self.client.post((f'/basket/add/1/'), {
            'product_id': 1,
            'quantity': 1,
            'redirect_url': '/',
        })

        # Check that the test item (id = 1) was added to the basket
        session = self.client.session
        self.assertEqual(session['basket'], {'1': 1})

    def test_checkout_render_context(self):
        """
        Tests that the checkout page is rendered properly
        """

        response = self.client.get('/checkout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'checkout/checkout.html', 'base.html'
            )

    def test_checkout_no_products(self):
        """
        Tests that the checkout page is not accessed
        when there are no products in the basket
        """

        # Check that the test item (id = 1) was added to the basket
        session = self.client.session
        self.assertEqual(session['basket'], {'1': 1})

        # Try to remove the test product from the basket
        response = self.client.post('/basket/remove/1/', follow=True)

        # Check that the basket remove action executes successfully
        self.assertEqual(response.status_code, 200)

        # Check that the basket is empty
        session = self.client.session
        self.assertEqual(session['basket'], {})

        # Check that we are redirected when attempting to 
        # access checkout with an empty basket
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

        # Check that we do not reach the checkout page
        self.assertTemplateNotUsed('checkout/checkout.html')

        # Check that the error message is raised
        self.assertRaises(
            Exception, msg="You don't have anything in your basket!"
            )

    def test_checkout_process(self):
        """
        Attempts to checkout and simulate purchase of the test product
        """

        # Check that the test item (id = 1) was added to the basket
        session = self.client.session
        self.assertEqual(session['basket'], {'1': 1})

        # Attempt to checkout
        # To get this to work a pid must be explicitly
        # declared in the checkout view. This test
        # will not override the pid variable from the view
        response = self.client.post(('/checkout/'), {
            'stripe_public_key': os.getenv("STRIPE_PUBLIC_KEY"),
            'stripe_secret_key': os.getenv("STRIPE_SECRET_KEY"),
            'full_name': 'test_full_name',
            'email': 'test@testemail.com',
            'phone_number': '0000000000',
            'country': 'US',
            'postcode': '42424',
            'town_or_city': 'test_town',
            'street_address1': 'test_street_1',
            'street_address2': 'test_street_2',
            'county': 'test_county',
            'pid': 'test_pid',
            'stripe_pid': 'test_stripe_pid',
        }, follow=True)
