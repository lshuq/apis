from api_test.models.basemodels import *


class Zb_terrain_block(MySQLModel):
    order_id = BigIntegerField()  # 订单号
    name = CharField(max_length=255)  # 地块名称
    type = IntegerField()  # 地块类型
    edge = CharField(max_length=5000)  # 经纬度列表，边界坐标
    area = FloatField()  # 面积


try:
    mysql_db.create_tables(models=[Zb_terrain_block])
except InternalError:
    pass
