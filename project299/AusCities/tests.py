from django.test import TestCase
from AusCities.models  import User, Location, Admin

class LocationTests(TestCase):
	
	def setUp(self):
		Location.objects.create(name="USQ", locationtype="College")
		
	def test(self):
		ab = Location.objects.get(name="USQ")
		
		self.assertEqual(ab, "USQ")
