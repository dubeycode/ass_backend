from django.db import models

# Create your models here.
from django.db import models

class BmbcChecksheet(models.Model):
    adjustingTube = models.CharField(max_length=100)
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)

    def __str__(self):
        return f"BMB Checksheet #{self.id}"


class BogieChecksheet(models.Model):
    axleGuide = models.CharField(max_length=100)
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)

    def __str__(self):
        return f"Bogie Checksheet #{self.id}"


class BogieDetails(models.Model):
    bogieNo = models.CharField(max_length=20)
    dateOfIOH = models.DateField()
    deficitComponents = models.TextField()
    incomingDivAndDate = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)

    def __str__(self):
        return self.bogieNo


class BogieChecksheetForm(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()

    bmbcChecksheet = models.OneToOneField(BmbcChecksheet, on_delete=models.CASCADE)
    bogieChecksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bogieDetails = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.formNumber


#####################################################

class WheelFields(models.Model):
    condemningDia = models.CharField(max_length=50)
    lastShopIssueSize = models.CharField(max_length=50)
    treadDiameterNew = models.CharField(max_length=50)
    wheelGauge = models.CharField(max_length=50)

    def __str__(self):
        return f"WheelFields #{self.id}"


class WheelSpecificationForm(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    
    fields = models.OneToOneField(WheelFields, on_delete=models.CASCADE)

    def __str__(self):
        return self.formNumber