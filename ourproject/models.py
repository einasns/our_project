from django.db import models


# Create your models here.
#we don't need this any more

class Customer(models.Model):
	full_name = models.CharField(max_length=200, null=True)
	user_name=models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address=models.CharField(max_length=200,null=True)
	customer_id = models.CharField(max_length=9,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	password=models.CharField(max_length=15,null=True)
	def __str__(self):
		return self.full_name

#we don't need this any more

class Worker(models.Model):
	full_name = models.CharField(max_length=200, null=True)
	user_name=models.CharField(max_length=200,null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	address=models.CharField(max_length=200,null=True)
	worker_id = models.CharField(max_length=9,null=True)
	password=models.CharField(max_length=15,null=True)
	bank_acccount=models.CharField(max_length=16,null=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name
#we don't need this any more
class Admin(models.Model):
	user_name=models.CharField(max_length=200,null=True)
	pass_word=models.CharField(max_length=200,null=True)

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name
class Product(models.Model):
	CATEGORY = (
			('Pen-Markers', 'Pen-Markers'),
			('Paint', 'Paint'),('Brushes', 'Brushes'),
			('Art paper&board', 'Art paper&board'),
			('Canvas', 'Canvas'),
			('Drawing media', 'Drawing media')
			)

	name = models.CharField(max_length=200, null=True)
	bar_code=models.CharField(max_length=10,null=True)
	price = models.IntegerField(default=0)
	amount=models.IntegerField(default=0)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags=models.ManyToManyField(Tag)
	def __str__(self):
		return self.name
class Order(models.Model):
	order_number=models.IntegerField(default=0)
	price=models.IntegerField(default=0)
	amount=models.IntegerField(default=0)
	name_of_product=models.CharField(max_length=200)
	customer_name=models.CharField(max_length=200,null=True)
	customer =models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
	product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
class Feedback(models.Model):
	customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	feedback=models.CharField(max_length=1200,null=True)
class cart(models.Model):
	customer=models.OneToOneField(Customer,null=True,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
# class work_schedule(models.Model):




# we need to add two tabels carts and feedback