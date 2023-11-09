import datetime

from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User
from products.models import Product
from django.utils.html import escape
from django.utils import timezone



# ------------ VIEWS TESTING ------------

class BasketViewTestCase(TestCase):
    """
    Test case for testing basket views.
    """

    def setUp(self):
        """
        Makes two sample users, one with superuser status and one without.
        Next, makes a sample product object
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



    def test_basket_render_context(self):
        """
        Tests that the basket page is rendered properly
        and the correct context is passed in
        """

        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'basket/basket.html', 'base.html'
            )
        self.assertTemplateUsed(
            response, 'products/includes/quantity_input_script.html'
            )

    def test_basket_add(self):
        """
        Adds the test product to the basket, tests whether it has been
        added successfully. Then attempts to add a duplicate item to
        the basket, checks that it is not successful.
        """

        # Get the most recently created product (test product)
        product1 = Product.objects.latest('pk')

        # Try to add the test product to the basket
        response = self.client.post((f'/basket/add/1/'), {
            'product_id': 1,
            'quantity': 1,
            'redirect_url': '/',
        }, follow=True)

        # Check that the basket action executes successfully
        self.assertEqual(response.status_code, 200)


        # Check that the test item (id = 1) was added to the basket
        session = self.client.session
        self.assertEqual(session['basket'], {'1': 1})

        # Try to add the test product to the basket again
        response = self.client.post((f'/basket/add/1/'), {
            'product_id': 1,
            'quantity': 1,
            'redirect_url': '/',
        })

        # Check that we are redirected
        self.assertEqual(response.status_code, 302)
        
        # Check that the exception is raised
        self.assertRaises(Exception, msg=f'{product1.name} is already in your basket!')

        # Check that a duplicate item was not added to the basket
        self.assertEqual(session['basket'], {'1': 1})



    def test_basket_remove(self):
        """
        Adds the test product to the basket, checks that it was added.
        Then deletes the product from the basket, checks that the
        basket is empty. Next, attempts to delete a non-existant item
        from the basket, checks that it is unsuccessful.
        """

        # Get the most recently created product (test product)
        product1 = Product.objects.latest('pk')

        # Try to add the test product to the basket
        response = self.client.post((f'/basket/add/1/'), {
            'product_id': 1,
            'quantity': 1,
            'redirect_url': '/',
        }, follow=True)

        # Check that the basket add action executes successfully
        self.assertEqual(response.status_code, 200)

        # Check that the test item (id = 1) was added to the basket
        session = self.client.session
        self.assertEqual(session['basket'], {'1': 1})

        # Try to remove the test product from the basket
        response = self.client.post('/basket/remove/1/', follow=True)

        # Check that the basket remove action executes successfully
        self.assertEqual(response.status_code, 200)

        # Check that the basket is empty, meaning deletion was successful
        session = self.client.session
        self.assertEqual(session['basket'], {})

        # Try to remove the test product from the basket
        # while the basket is empty
        response = self.client.post('/basket/remove/1/')

        # Check that we are redirected
        self.assertEqual(response.status_code, 302)

        # Check that the error message is raised
        self.assertRaises(Exception, msg="Oops, that didn't work, please try again.")