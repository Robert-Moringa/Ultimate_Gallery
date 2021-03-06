from django.test import TestCase

from .models import Location, Image, Category

# Create your tests here.

class LocationTestCLass(TestCase):
    loc = Location(place="Amboseli")
    #Set up Method
    def setUp(self):
        self.loc = Location(place="Amboseli")
        self.loc.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_save_method(self):
        self.loc.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.loc.save_location()
        self.loc.clear_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="travel")
        self.cat.save_category()

        self.loc = Location(place="Amboseli")
        self.loc.save_location()

        self.image = Image(name='karura', description='fabulous', image_location=self.loc, image_category=self.cat)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_search_by_category(self):
        self.cat = Category(name="travel")
        self.cat.save_category()
        self.loc = Location(place="Amboseli")
        self.loc.save_location()
        self.image = Image(name='karura', description='fabulous', image_location=self.loc, image_category=self.cat)
        self.image.save_image()

        images = Image.search_by_category('travel')
        self.assertTrue(len(images)>0)



class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="travel")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.clear_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
