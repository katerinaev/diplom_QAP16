from data.body import new_pet, users_list, user_1
from data.files import file_1
from data.headers import headers_1, headers_2, headers_3
from services.pet_service import PetServices


def test_get_pet_by_id():
    pet_services = PetServices()
    pet_services.get_pet_by_id()
    assert pet_services.get_pet_by_id().get("id") == 1
    assert pet_services.get_pet_by_id().get("name") == "doggie"


def test_add_new_pet():
    pet_services = PetServices()
    pet_services.post_pet(headers=headers_2, pet=new_pet)


def test_delete_purchase_order():
    pet_services = PetServices()
    pet_services.delete_order(headers_1, '10')


def test_post_list_of_users():
    pet_services = PetServices()
    pet_services.post_users_list(headers=headers_2, ulist=users_list)


def test_updated_user():
    pet_services = PetServices()
    pet_services.put_user(headers=headers_2, user=user_1)


def test_updload_image():
    pet_services = PetServices()
    pet_services.upload_image(headers=headers_3, file=file_1)
