from django.db import models
from django.utils import timezone

class LabPersonnel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    license_upload = models.FileField(upload_to='licenses/')
    certificate_upload = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TestAvailable(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    test = models.ForeignKey(TestAvailable, on_delete=models.CASCADE)
    result = models.TextField()
    date_performed = models.DateTimeField(auto_now_add=True)
    performed_by = models.ForeignKey(LabPersonnel, on_delete=models.CASCADE)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.patient.first_name} {self.patient.last_name} - {self.test.name}"

class PaymentRequest(models.Model):
    test = models.ForeignKey('TestAvailable', on_delete=models.CASCADE)  # Change 'Test' to 'TestAvailable'
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2)
    requested_at = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment Request for {self.test.name} - Amount: {self.amount_requested}"


class BroadcastedRequest(models.Model):
    lab_personnel = models.ForeignKey(LabPersonnel, on_delete=models.CASCADE)
    message = models.TextField()
    broadcasted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Broadcasted Request by {self.lab_personnel.first_name} {self.lab_personnel.last_name} at {self.broadcasted_at}"
