import base64

from api_test.models.basemodels import *


class Info(MySQLModel):
    company_id = IntegerField()
    code = CharField()
    pwd = CharField()
    name = CharField()
    company_type = IntegerField()  # 1:植保服务商；2:测评机构；3:监督机构
    address = CharField()
    comment = CharField()
    principal_name = CharField()
    principal_phone = CharField()
    contacts_name = CharField()
    contacts_phone = CharField()
    hotline = CharField()
    authentication = IntegerField()  # 认证状态，默认0,，未认证
    email = CharField()
    logo = CharField()
    business_licence = CharField()
    qualification = CharField()

    def logo_base64(self, picture):
        pic_base64 = picture.encode()
        self.logo = pic_base64

    def licence_base64(self, picture):
        pic_base64 = picture.encode()
        self.business_licence = pic_base64

    def qualification_base64(self, picture):
        pic_base64 = picture.encode()
        self.qualification = pic_base64


try:
    mysql_db.create_tables(models=[Info])
except InternalError:
    pass
