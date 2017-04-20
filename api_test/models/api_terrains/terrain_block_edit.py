import re

from api_test.models.api_terrains.terrain_block_model import *
from api_test.models.api_terrains.terrain_block_model import Zb_terrain_block as Block


def edge_turn(edge):
    edge = edge.replace(',', ' ')
    edge = edge.replace('[', '')
    edge = edge.replace(']', '')
    edge = edge.replace('{', '')
    edge = edge.replace('}', '')
    edge = edge.replace(':', '')
    edge = edge.replace('\'', '')
    edge = re.split(r'\s+', edge)
    dictionary = {}
    edge_list = []
    for i in range(len(edge)):
        if i % 4 == 0:
            edge_list.append(dictionary)
        if i % 2 == 0:
            dictionary[str(edge[i])] = edge[i + 1]
    return edge_list


def show_terrain(block):
    new_block = {}
    new_block['order_id'] = block.order_id
    new_block['name'] = block.name
    new_block['type'] = block.type
    new_block['area'] = block.area
    new_block['edge'] = edge_turn(block.edge)
    return new_block


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
def delete_terrain(datas=None, order_id=None):
    if datas is not None:
        for data in datas:
            try:
                block = Block.get(Block.order_id == data.order_id)
                block.delete_instance()
            except:
                return False
        return datas
    if order_id is not None:
        try:
            block = Block.get(Block.order_id == order_id)
            block.delete_instance()
        except:
            return False
        return block
    return False


# 查找数据
def search_terrain(datas=None, order_id=None, name=None):
    if datas is not None:
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
        if new_datas is not []:
            return new_datas
    if order_id is not None:
        try:
            block = Block.get(Block.order_id == order_id)
            return block
        except:
            pass
    if name is not None:
        try:
            block = Block.get(Block.name == name)
            return block
        except:
            pass
    return False
