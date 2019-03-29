from django.test import TestCase
from .models import Images,Profile

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.love= Images(title = 'Love',  caption ='If you love me, i love you too')

    def test_instance(self):
        self.assertTrue(isinstance(self.love,Images))

    def test_save_method(self):
        self.love.save_images()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)   


    def test_delete_method(self):
        self.love.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)   

    def test_update_method(self):
        self.love.save_images()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)                

class ProfileTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= user(user_name= 'vava',first_name = 'James', last_name ='Muriuki', bio='I have bechor in computer science')
        self.james.save_user()

        # Creating a new profileand saving it
        self.new_profile= profiles(name = 'testing')
        self.new_profile.save()

        self.profile= Profile(title = 'Test Profile',post = 'This is a pictures',user = self.james)
        self.profile.save()

        self.profile.profiles.add(self.new_profile)

    def tearDown(self):
        User.objects.all().delete()
        images.objects.all().delete()
        Profile.objects.all().delete()    

