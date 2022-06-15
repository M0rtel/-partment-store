from django.db import models

class ApartmentCharacteristics(models.Model):
    image1 = models.ImageField(upload_to='projects/img/')
    image2 = models.ImageField(upload_to='projects/img/')
    image3 = models.ImageField(upload_to='projects/img/')
    image4 = models.ImageField(upload_to='projects/img/')
    image5 = models.ImageField(upload_to='projects/img/')
    image6 = models.ImageField(upload_to='projects/img/')
    image7 = models.ImageField(upload_to='projects/img/')
    image8 = models.ImageField(upload_to='projects/img/')
    image9 = models.ImageField(upload_to='projects/img/')
    image10 = models.ImageField(upload_to='projects/img/')
    what_apartment = models.CharField(max_length=300, default='1-ая квартира')
    price = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    name_object = models.CharField(max_length=300)
    total_area = models.CharField(max_length=300)
    living_area = models.CharField(max_length=300)
    kitchen = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    total_floors = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    condition = models.CharField(max_length=300)
    fund = models.CharField(max_length=300)
    certificate = models.CharField(max_length=300)
    windows = models.CharField(max_length=300)
    balcony = models.CharField(max_length=300)
    bathroom = models.CharField(max_length=300)
    hot_water = models.CharField(max_length=300)
    heating = models.CharField(max_length=300)
    rooms = models.CharField(max_length=300)
    elevator = models.CharField(max_length=300)
    area_with_cold_rooms = models.CharField(max_length=300, default='49')
    comments = models.TextField()

    def __str__(self):
        return self.name_object

    class Meta:
        verbose_name = 'Характеристику студии'
        verbose_name_plural = 'Характеристики студий'


class ApartmentCharacteristicsKV1(models.Model):
    image1 = models.ImageField(upload_to='projects/img/')
    image2 = models.ImageField(upload_to='projects/img/')
    image3 = models.ImageField(upload_to='projects/img/')
    image4 = models.ImageField(upload_to='projects/img/')
    image5 = models.ImageField(upload_to='projects/img/')
    image6 = models.ImageField(upload_to='projects/img/')
    image7 = models.ImageField(upload_to='projects/img/')
    image8 = models.ImageField(upload_to='projects/img/')
    image9 = models.ImageField(upload_to='projects/img/')
    image10 = models.ImageField(upload_to='projects/img/')
    what_apartment = models.CharField(max_length=300, default='1-ая квартира')
    price = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    name_object = models.CharField(max_length=300)
    total_area = models.CharField(max_length=300)
    living_area = models.CharField(max_length=300)
    kitchen = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    total_floors = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    condition = models.CharField(max_length=300)
    fund = models.CharField(max_length=300)
    certificate = models.CharField(max_length=300)
    windows = models.CharField(max_length=300)
    balcony = models.CharField(max_length=300)
    bathroom = models.CharField(max_length=300)
    hot_water = models.CharField(max_length=300)
    heating = models.CharField(max_length=300)
    rooms = models.CharField(max_length=300)
    elevator = models.CharField(max_length=300)
    area_with_cold_rooms = models.CharField(max_length=300, default='49')
    comments = models.TextField()

    def __str__(self):
        return self.name_object

    class Meta:
        verbose_name = 'Характеристику 1-ой квартиры'
        verbose_name_plural = 'Характеристики 1-ой квартиры'


class ApartmentCharacteristicsKV2(models.Model):
    image1 = models.ImageField(upload_to='projects/img/')
    image2 = models.ImageField(upload_to='projects/img/')
    image3 = models.ImageField(upload_to='projects/img/')
    image4 = models.ImageField(upload_to='projects/img/')
    image5 = models.ImageField(upload_to='projects/img/')
    image6 = models.ImageField(upload_to='projects/img/')
    image7 = models.ImageField(upload_to='projects/img/')
    image8 = models.ImageField(upload_to='projects/img/')
    image9 = models.ImageField(upload_to='projects/img/')
    image10 = models.ImageField(upload_to='projects/img/')
    what_apartment = models.CharField(max_length=300, default='1-ая квартира')
    price = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    name_object = models.CharField(max_length=300)
    total_area = models.CharField(max_length=300)
    living_area = models.CharField(max_length=300)
    kitchen = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    total_floors = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    condition = models.CharField(max_length=300)
    fund = models.CharField(max_length=300)
    certificate = models.CharField(max_length=300)
    windows = models.CharField(max_length=300)
    balcony = models.CharField(max_length=300)
    bathroom = models.CharField(max_length=300)
    hot_water = models.CharField(max_length=300)
    heating = models.CharField(max_length=300)
    rooms = models.CharField(max_length=300)
    elevator = models.CharField(max_length=300)
    area_with_cold_rooms = models.CharField(max_length=300, default='49')
    comments = models.TextField()

    def __str__(self):
        return self.name_object

    class Meta:
        verbose_name = 'Характеристику 2-ой квартиры'
        verbose_name_plural = 'Характеристики 2-ой квартиры'


class ApartmentCharacteristicsKV3(models.Model):
    image1 = models.ImageField(upload_to='projects/img/')
    image2 = models.ImageField(upload_to='projects/img/')
    image3 = models.ImageField(upload_to='projects/img/')
    image4 = models.ImageField(upload_to='projects/img/')
    image5 = models.ImageField(upload_to='projects/img/')
    image6 = models.ImageField(upload_to='projects/img/')
    image7 = models.ImageField(upload_to='projects/img/')
    image8 = models.ImageField(upload_to='projects/img/')
    image9 = models.ImageField(upload_to='projects/img/')
    image10 = models.ImageField(upload_to='projects/img/')
    what_apartment = models.CharField(max_length=300, default='1-ая квартира')
    price = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    name_object = models.CharField(max_length=300)
    total_area = models.CharField(max_length=300)
    living_area = models.CharField(max_length=300)
    kitchen = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    total_floors = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    condition = models.CharField(max_length=300)
    fund = models.CharField(max_length=300)
    certificate = models.CharField(max_length=300)
    windows = models.CharField(max_length=300)
    balcony = models.CharField(max_length=300)
    bathroom = models.CharField(max_length=300)
    hot_water = models.CharField(max_length=300)
    heating = models.CharField(max_length=300)
    rooms = models.CharField(max_length=300)
    elevator = models.CharField(max_length=300)
    area_with_cold_rooms = models.CharField(max_length=300, default='49')
    comments = models.TextField()

    def __str__(self):
        return self.name_object

    class Meta:
        verbose_name = 'Характеристику 3-ой квартиры'
        verbose_name_plural = 'Характеристики 3-ой квартиры'


class ApartmentCharacteristicsR(models.Model):
    image1 = models.ImageField(upload_to='projects/img/')
    image2 = models.ImageField(upload_to='projects/img/')
    image3 = models.ImageField(upload_to='projects/img/')
    image4 = models.ImageField(upload_to='projects/img/')
    image5 = models.ImageField(upload_to='projects/img/')
    image6 = models.ImageField(upload_to='projects/img/')
    image7 = models.ImageField(upload_to='projects/img/')
    image8 = models.ImageField(upload_to='projects/img/')
    image9 = models.ImageField(upload_to='projects/img/')
    image10 = models.ImageField(upload_to='projects/img/')
    what_apartment = models.CharField(max_length=300, default='1-ая квартира')
    price = models.CharField(max_length=300)
    district = models.CharField(max_length=300)
    name_object = models.CharField(max_length=300)
    total_area = models.CharField(max_length=300)
    living_area = models.CharField(max_length=300)
    kitchen = models.CharField(max_length=300)
    floor = models.CharField(max_length=300)
    total_floors = models.CharField(max_length=300)
    material = models.CharField(max_length=300)
    condition = models.CharField(max_length=300)
    fund = models.CharField(max_length=300)
    certificate = models.CharField(max_length=300)
    windows = models.CharField(max_length=300)
    balcony = models.CharField(max_length=300)
    bathroom = models.CharField(max_length=300)
    hot_water = models.CharField(max_length=300)
    heating = models.CharField(max_length=300)
    rooms = models.CharField(max_length=300)
    elevator = models.CharField(max_length=300)
    area_with_cold_rooms = models.CharField(max_length=300, default='49')
    comments = models.TextField()

    def __str__(self):
        return self.name_object

    class Meta:
        verbose_name = 'Характеристику рекомендованной квартиры'
        verbose_name_plural = 'Характеристики рекомендованных квартир'
