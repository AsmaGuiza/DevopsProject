from django.db import models

class AIModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    f1_score =models.DecimalField(decimal_places=2,max_digits=5,default=0.0)
    accuracy = models.DecimalField(decimal_places=2,max_digits=5,default=0.0)
    confusion_matrix = models.ImageField(upload_to='images/',null=True,blank=True)
    train_validation_acc = models.ImageField(upload_to='images/',null=True,blank=True)
    train_validation_loss = models.ImageField(upload_to='images/',null=True,blank=True)
    model_file = models.FileField(upload_to='models/')
    dataset = models.CharField(max_length=100,default='')

    

    def __str__(self):
        return self.name