# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class KfAi(models.Model):
    problem_type = models.IntegerField(db_column='Problem_type', primary_key=True)  # Field name made lowercase.
    kf_order = models.ForeignKey('KfOrder', models.DO_NOTHING, db_column='KF_order_id', blank=True, null=True)  # Field name made lowercase.
    solution = models.TextField(blank=True, null=True)
    solution_evaluation_level = models.IntegerField(db_column='Solution_evaluation_level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kf_ai'


class KfOrder(models.Model):
    kf_order_id = models.IntegerField(db_column='KF_order_id', primary_key=True)  # Field name made lowercase.
    kf_problem_type = models.IntegerField(db_column='KF__Problem_type', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    user = models.ForeignKey('UserOrigon', models.DO_NOTHING, blank=True, null=True)
    kf_kf_servicers_id = models.CharField(db_column='KF__KF_Servicers_id', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    kf_servicers_id = models.CharField(db_column='KF_Servicers_id', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kf_creation_time = models.DateField(db_column='KF_creation_time', blank=True, null=True)  # Field name made lowercase.
    problem_type = models.IntegerField(db_column='Problem_type', blank=True, null=True)  # Field name made lowercase.
    kf_problem_content = models.TextField(db_column='KF_problem_content', blank=True, null=True)  # Field name made lowercase.
    kf_collaborative_department = models.IntegerField(db_column='KF_collaborative_department', blank=True, null=True)  # Field name made lowercase.
    solution = models.TextField(db_column='Solution', blank=True, null=True)  # Field name made lowercase.
    solution_level = models.IntegerField(db_column='Solution_level', blank=True, null=True)  # Field name made lowercase.
    service_elevel = models.IntegerField(db_column='Service_Elevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kf_order'


class KfServer(models.Model):
    kf_servicers_id = models.CharField(db_column='KF_Servicers_id', primary_key=True, max_length=10)  # Field name made lowercase.
    kf_order = models.ForeignKey(KfOrder, models.DO_NOTHING, db_column='KF_order_id', blank=True, null=True)  # Field name made lowercase.
    kf_evaluation_level = models.IntegerField(db_column='KF_evaluation_level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kf_server'


class UserCharge(models.Model):
    user = models.OneToOneField('UserOrigon', models.DO_NOTHING, primary_key=True)
    user_cr_loc = models.TextField(db_column='USER_CR_LOC', blank=True, null=True)  # Field name made lowercase.
    user_cr_power = models.FloatField(db_column='USER_CR_POWER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_charge'


class UserEmergency(models.Model):
    user = models.OneToOneField('UserOrigon', models.DO_NOTHING, primary_key=True)
    wb_dr = models.ForeignKey('WbCartask', models.DO_NOTHING, db_column='WB_DR_ID', blank=True, null=True)  # Field name made lowercase.
    user_eme_loc = models.TextField(db_column='USER_EME_LOC', blank=True, null=True)  # Field name made lowercase.
    user_eme_prob = models.TextField(db_column='USER_EME_Prob', blank=True, null=True)  # Field name made lowercase.
    user_eme_date = models.TimeField(db_column='USER_EME_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_emergency'


class UserHistory(models.Model):
    user = models.OneToOneField('UserOrigon', models.DO_NOTHING, primary_key=True)
    server_id = models.CharField(max_length=10, blank=True, null=True)
    inf = models.TextField(db_column='INF', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_history'


class UserNeed(models.Model):
    user = models.OneToOneField('UserOrigon', models.DO_NOTHING, primary_key=True)
    wb_pr = models.ForeignKey('WbProject', models.DO_NOTHING, db_column='WB_PR_ID', blank=True, null=True)  # Field name made lowercase.
    user_nd_inf = models.TextField(db_column='USER_ND_INF', blank=True, null=True)  # Field name made lowercase.
    user_nd_date = models.TimeField(db_column='USER_ND_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_need'


class UserOrigon(models.Model):
    user_id = models.CharField(primary_key=True, max_length=10)
    user_key = models.CharField(max_length=12)
    user_birthday = models.DateField(blank=True, null=True)
    user_car = models.TextField(blank=True, null=True)
    user_other = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_origon'


class WbCartask(models.Model):
    wb_dr = models.OneToOneField('WbDriver', models.DO_NOTHING, db_column='WB_DR_ID', primary_key=True)  # Field name made lowercase.
    wb_car_loc = models.TextField(db_column='WB_CAR_LOC', blank=True, null=True)  # Field name made lowercase.
    wb_car_mode = models.IntegerField(db_column='WB_CAR_MODE', blank=True, null=True)  # Field name made lowercase.
    wb_car_num = models.CharField(db_column='WB_CAR_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wb_cartask'


class WbCharge(models.Model):
    wb_cr_id = models.CharField(db_column='WB_CR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_cr_name = models.CharField(db_column='WB_CR_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wb_cr_working = models.TextField(db_column='WB_CR_Working', blank=True, null=True)  # Field name made lowercase.
    wb_cr_loc = models.TextField(db_column='WB_CR_LOC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_charge'


class WbDriver(models.Model):
    wb_dr_id = models.CharField(db_column='WB_DR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_wb_dr_id = models.CharField(db_column='WB__WB_DR_ID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    wb_dr_mode = models.IntegerField(db_column='WB_DR_MODE', blank=True, null=True)  # Field name made lowercase.
    wb_dr_num = models.CharField(db_column='WB_DR_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_driver'


class WbProject(models.Model):
    wb_pr_id = models.CharField(db_column='WB_PR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_or = models.ForeignKey('WbSvId', models.DO_NOTHING, db_column='WB_OR_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(max_length=10, blank=True, null=True)
    wb_pr_sever = models.CharField(db_column='WB_PR_SEVER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wb_pr_project = models.TextField(db_column='WB_PR_Project', blank=True, null=True)  # Field name made lowercase.
    wb_pr_price = models.FloatField(db_column='WB_PR_Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_project'


class WbQualityInspection(models.Model):
    wb_qi_id = models.CharField(db_column='WB_QI_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_or = models.ForeignKey('WbSvId', models.DO_NOTHING, db_column='WB_OR_ID', blank=True, null=True)  # Field name made lowercase.
    wb_qi_ans = models.IntegerField(db_column='WB_QI_ANS', blank=True, null=True)  # Field name made lowercase.
    wb_qi_inf = models.TextField(db_column='WB_QI_INF', blank=True, null=True)  # Field name made lowercase.
    wb_qi_server = models.CharField(db_column='WB_QI_Server', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_quality_inspection'


class WbServer(models.Model):
    wb_sv_id = models.CharField(db_column='WB_SV_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_or = models.ForeignKey('WbSvId', models.DO_NOTHING, db_column='WB_OR_ID', blank=True, null=True)  # Field name made lowercase.
    wb_sv_mode = models.IntegerField(db_column='WB_SV_mode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_server'


class WbSvId(models.Model):
    wb_or_id = models.CharField(db_column='WB_OR_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    wb_pr_id = models.CharField(db_column='WB_PR_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wb_or_date = models.DateField(db_column='WB_OR_DATE', blank=True, null=True)  # Field name made lowercase.
    wb_or_inf = models.TextField(db_column='WB_OR_INF', blank=True, null=True)  # Field name made lowercase.
    wb_or_price = models.DecimalField(db_column='WB_OR_Price', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    wb_or_server = models.CharField(db_column='WB_OR_SERVER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    wb_or_mode = models.IntegerField(db_column='WB_OR_MODE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wb_sv_id'
