import pytest
from .serializers import ModuleSerializer

from .models import Module


@pytest.mark.django_db
def test_module_create():
    Module.objects.create(title='First', description='First module')
    assert Module.objects.count() == 1

@pytest.mark.django_db
def test_module_get():
    Module.objects.create(title='First', description='First module')
    response = Module.objects.get(id=1)
    assert response.title == 'First'


@pytest.mark.django_db
def test_module_update():
    Module.objects.create(title='First', description='First module')
    response = Module.objects.get(id=1)
    response.title = 'Second'
    assert response.title == 'Second'


@pytest.mark.django_db
def test_module_delete():
    Module.objects.create(title='First', description='First module')
    Module.objects.get(id=1).delete()
    assert Module.objects.count() == 0


@pytest.mark.django_db
def test_serializer_positive():
    data = {"title": "First", "description": "First Module"}
    serializer = ModuleSerializer(data=data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_serializer_negative_title():
    data = {"description": "First Module"}
    serializer = ModuleSerializer(data=data)
    assert not serializer.is_valid()
    assert "This field is required." in serializer.errors["title"]


@pytest.mark.django_db
def test_serializer_negative_description():
    data = {"title": "First"}
    serializer = ModuleSerializer(data=data)
    assert not serializer.is_valid()
    assert "This field is required." in serializer.errors["description"]


@pytest.mark.django_db
def test_serializer_negative_length_title():
    data = {"title": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "description": "First Module"}
    serializer = ModuleSerializer(data=data)
    assert not serializer.is_valid()
    assert "Ensure this field has no more than 50 characters." in serializer.errors["title"]


@pytest.mark.django_db
def test_api_create_module(api_client):

    data = {"title": "First", "description": "First Module"}
    response = api_client.post('/api/module/create/', data=data)
    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['title'] == 'First'
    assert response.data['description'] == 'First Module'


@pytest.mark.django_db
def test_api_delete_module(api_client):

    data = {"title": "First", "description": "First Module"}
    api_client.post('/api/module/create/', data=data)
    response = api_client.delete('/api/module/delete/1')
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_get_module_list(api_client):

    data = {"title": "First", "description": "First Module"}
    api_client.post('/api/module/create/', data=data)
    response = api_client.get('/api/module/')
    expected = [{"id": 1,"title": "First", "description": "First Module"}]
    assert response.data == expected


@pytest.mark.django_db
def test_api_get_module_obj(api_client):

    data = {"title": "First", "description": "First Module"}
    api_client.post('/api/module/create/', data=data)
    response = api_client.get('/api/module/1')
    expected = {"id": 1,"title": "First", "description": "First Module"}
    assert response.data == expected


@pytest.mark.django_db
def test_api_update_module(api_client):
    data = {"title": "First", "description": "First Module"}
    api_client.post('/api/module/create/', data=data)
    update_data = {"title": "Update", "description": "Update"}
    response = api_client.patch('/api/module/update/1', data=update_data)

    assert response.data == {"id": 1,"title": "Update", "description": "Update"}
