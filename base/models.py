from django.db import models


class Website(models.Model):
    """Represent a front-end website that will send us requests"""
    title = models.CharField(max_length=100, unique=True, primary_key=True)
    link = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.title)


class Email(models.Model):
    """Represent an email form inside the requests that we will receive"""
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient} at {self.created_at}: {self.subject}"
