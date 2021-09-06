from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 60)
    image_path = models.ImageField(upload_to = 'uploads/')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image_location = models.ForeignKey('Location', on_delete=models.CASCADE)
    image_category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id ,name, image, description , image_location, image_category):
        update = cls.objects.filter(id = id).update(name = name, image=image,description = description ,image_location = image_location,image_category = image_category)
    

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(image_category__name__icontains=search_term)
        return images

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images


    @classmethod
    def filter_by_location(cls, search_term):
        images_location = cls.objects.filter(image_location__id=search_term)
        return images_location

    @property
    def get_photo_url(self):
        if self.image_path and hasattr(self.image_path, 'url'):
            return self.image_path.url
        else:
            return "/static/images/noimage.png"


    def __str__(self):
        return self.name

class Location (models.Model):
    place = models.CharField(max_length = 60)

    def save_location(self):
        self.save()

    def clear_location(self):
        self.delete()
    
    def change_location(self, update):
        self.name=update
        self.save()

    def get_location(cls, id):
        map = Location.objects.get(pk = id)
        return map

    def __str__(self):
        return self.place

class Category(models.Model):
    name =models.CharField(max_length = 60)

    def save_category(self):
        self.save()

    def clear_category(self):
        self.delete()

    def change_category(self, update):
        self.name=update
        self.save()
    def __str__(self):
        return self.name