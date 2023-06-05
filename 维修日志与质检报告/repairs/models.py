from django.db import models

# class Order(models.Model):
#     order_id = models.IntegerField(primary_key=True)
#     order_type = models.CharField(max_length=20)
#     order_content = models.TextField()
#     order_fee = models.FloatField()
#     order_state = models.CharField(max_length=50)
#     order_time = models.DateTimeField()
#     user_name = models.CharField(max_length=20)

class Log(models.Model):
    log_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    log_type = models.CharField(max_length=20)
    log_content = models.TextField()
    log_time = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return f"Log ID: {self.log_id}"

class Inspection(models.Model):
    ins_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    ins_result = models.CharField(max_length=20)
    ins_content = models.TextField()
    ins_time = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return f"Inspection ID: {self.ins_id}"



class Repair(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 添加其他字段...

    def __str__(self):
        return self.name

# class RepairLog(models.Model):
#     repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
#     log_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     # 添加其他字段...
#
#     def __str__(self):
#         return f"Log for {self.repair}"
#
# class InspectionReport(models.Model):
#     repair = models.ForeignKey(Repair, on_delete=models.CASCADE)
#     report_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     # 添加其他字段...
#
#     def __str__(self):
#         return f"Report for {self.repair}"
