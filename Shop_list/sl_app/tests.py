import uuid
from django.test import Client
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from sl_app.models import User_to_list, MallList, Item, Shop_list

# Create your tests here.
class InviteTestCase(TestCase):
    def setUp(self):
        self.user1 = 'test_usr1'
        self.user2 = 'test_usr2'
        self.user1_email = 'test_usr1@user.com'
        self.user2_email = 'test_usr2@user.com'

        user1 = User.objects.create_user(self.user1, self.user1_email, '111')
        user1.save()
        self.user1_id = user1.id
        self.list1_id = uuid.uuid4()

        user2 = User.objects.create_user(self.user2, self.user2_email, '222')
        user2.save()
        self.user2_id = user2.id
        self.list2_id = uuid.uuid4()

        slist1 = User_to_list(user_id=self.user1_id, list_id=self.list1_id, or_list=self.list1_id)
        slist1.save()

        slist2 = User_to_list(user_id=self.user2_id, list_id=self.list2_id, or_list=self.list2_id)
        slist2.save()

    def test_email(self):
        c = Client()
        c.login(username=self.user1, password='111')

        responce = c.post('/user/invite', {'email': self.user2_email})
        self.assertEqual(responce.status_code, 200)

        bad_email = 'bad_email@user.com'
        responce = c.post('/user/invite', {'email': bad_email})
        self.assertEqual(responce.status_code, 404)

    def test_invite(self):
        c = Client()
        c.login(username= self.user1, password='111')

        responce = c.post('/user/invite', {'email': self.user2_email})
        sh_list_1 = User_to_list.objects.filter(user_id=self.user1_id).first()
        sh_list_2 = User_to_list.objects.filter(user_id=self.user2_id).first()
        self.assertEqual(sh_list_1.list_id, sh_list_2.list_id)

class RegisterTestCase(TestCase):
    def setUp(self) -> None:
        self.username_1 = 'test_usr3'
        self.email_1 = 'test_usr3@user.com'
        self.password_1 = '333'

        self.username_2 = 'test_usr4'
        self.email_2 = 'test_usr4@user.com'
        self.password_2 = '444'

    def test_signup_page_url(self):
        response = self.client.get("/user/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_create_user(self):
        response = self.client.post(reverse('register'), data={
        'login': self.username_1,
        'email': self.email_1,
        'psw': self.password_1 })

        self.assertEqual(response.status_code, 302)
        usr3 = User.objects.filter(username=self.username_1).first()
        self.assertIsNotNone(usr3)
        u3_list = User_to_list.objects.filter(user_id=usr3.id).first()
        self.assertIsNotNone(u3_list)

        response = self.client.post(reverse('register'), data={
            'login': self.username_2,
            'email': self.email_2,
            'psw': self.password_2 })

        self.assertEqual(response.status_code, 302)
        usr4 = User.objects.filter(username=self.username_2).first()
        self.assertIsNotNone(usr4)
        u4_list = User_to_list.objects.filter(user_id=usr4.id).first()
        self.assertIsNotNone(u4_list)

        self.assertNotEqual(u3_list.list_id, u4_list.list_id)

class BuyItemTestCase(TestCase):
    fixtures = ['sl_app.json']
    def setUp(self):
        self.quantity = 10
        self.price = 0
        self.id = 1

    def test_buy_item(self):
        c = Client()
        c.login(username='u1', password='1')

        slis = Shop_list.objects.get(list_id='947f811d-525c-4a4a-bcd5-0ac9fa396ee9', id=1)
        self.assertIsNotNone(slis)

        response = c.post('/shop_list/<1,хлеб>/buy', {
            'quantity': self.quantity,
            'price': self.price,
            'id': self.id})
        slis_eq = Shop_list.objects.get(list_id='947f811d-525c-4a4a-bcd5-0ac9fa396ee9', id=1)

        self.assertEqual('куплено', slis_eq.status)

