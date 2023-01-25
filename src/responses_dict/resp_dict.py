class RespDicts(dict):
    USER_NOT_FOUND = {'code': 1, 'type': 'error', 'message': 'User not found'}
    ORDER_NOT_FOUND = {'code': 1, 'type': 'error', 'message': 'Order not found'}
    ORDER = {'id': 989, 'petId': 900, 'quantity': 436, 'shipDate': '1998-11-12T15:35:39.098+0000', 'status': 'placed',
             'complete': False}
    PET = {'id': 502, 'category': {'id': 81, 'name': 'fvlogqru'}, 'name': 'izpanhukki',
           'photoUrls': ['pyxjqnefksrwgtj', 'eievebknorsa'],
           'tags': [{'id': 672, 'name': 'vmrbweuu'}, {'id': 404, 'name': 'hwmeiqid'}], 'status': 'available'}
    SUCCESS = {'code': 200, 'type': str, 'message': str}
    USER_DATA = {'id': 185, 'username': 'okxvx', 'firstName': 'otyotp', 'lastName': 'pdypwbk',
                 'email': 'rdddefxe@test.ru', 'password': 'qwerty12', 'phone': 'nlxbbfsfme', 'userStatus': 1}
