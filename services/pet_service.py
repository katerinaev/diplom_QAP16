from data.body import new_pet
from data.headers import headers_1, headers_2
from helpers.base_service import BaseServices


class PetServices(BaseServices):
    def get_pet_by_id(self):
        path = 'v2/pet/1'
        response = self.get(path, headers=headers_1)
        return response

    def post_pet(self, headers, pet):
        path = 'v2/pet'
        response = self.post(path, headers, pet)
        return response

    def delete_order(self, headers, id):
        path = 'v2/store/order/' + id
        response = self.delete(path, 404)
        return response

    def post_users_list(self, headers, ulist):
        path = 'v2/user/createWithArray'
        response = self.post(path, headers, ulist)
        return response

    def put_user(self, headers, user):
        path = 'v2/user/User1'
        response = self.put(path, headers, user)
        return response

    def upload_image(self, headers, file):
        path = 'v2/pet/177/uploadImage'
        response = self.upload(path, headers, file)
        return response
