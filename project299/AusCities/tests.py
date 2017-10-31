from django.test import TestCase
from AusCities.models  import User, Location, Admin

class LocationTests(TestCase):
	
	def setUp(self):
		Location.objects.create(name="USQ", locationtype="College")
		
	def test(self):
		ab = Location.objects.get(name="USQ")
		
		self.assertEqual(ab, "USQ")

class UserViewTests(TestCase):
    def test_access_logged_in(self):
        session = self.client.session
        session['logged'] = 1
        session.save()
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'logged in.')
    def test_access_logged_out(self):
        session = self.client.session
        session['logged'] = 0
        session.save()
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Remember me')
    def test_admin_access_as_user(self):
        session = self.client.session
        session['logged'] = 1
        session.save()
        response = self.client.get('/admin/add_info/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'administrator')
    def test_admin_access_as_admin(self):
        session = self.client.session
        session['logged'] = 2
        session.save()
        response = self.client.get('/admin/add_info/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Location name:')
    def test_null_location(self):
        Location.objects.create(name='QUT', locationtype='College')
        response = self.client.get('/location/1/')
        self.assertEqual(response.status_code, 500)