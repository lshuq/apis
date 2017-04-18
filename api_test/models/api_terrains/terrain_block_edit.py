from api_test.models.api_terrains.terrain_block_model import *
from api_test.models.api_terrains.terrain_block_model import Zb_terrain_block as Block


# 插入数据
def upload_terrain(data):
    try:
        if Block.get(Block.order_id == data['order_id']) is not None:
            return False
    except:
        pass
    block = Block()
    block.order_id = data['order_id']
    block.name = data['name']
    block.type = data['type']
    block.area = data['area']
    block.edge = str(data['edge'])
    block.save()
    return block


# 删除数据
def delete_terrain(datas):
    for data in datas:
        try:
            block = Block.get(Block.order_id == data.order_id)
            block.delete_instance()
        except:
            pass
    return datas


# 查找数据
def search_terrain(datas):
    new_datas = []
    for data in datas:
        try:
            block = None
            if data.order_id is not None:
                block = Block.get(Block.order_id == data.order_id)
            elif data.name is not None:
                block = Block.get(Block.order_id == data.name)
            elif data.type is not None:
                block = Block.get(Block.order_id == data.type)
            elif data.area is not None:
                block = Block.get(Block.order_id == data.data.area)
            elif data.edge is not None:
                block = Block.get(Block.order_id == data.data.edge)
            if block is not None:
                new_datas.append(block)
        except:
            pass
    return new_datas
