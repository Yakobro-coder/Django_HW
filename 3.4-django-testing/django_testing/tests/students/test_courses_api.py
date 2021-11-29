import pytest
from django.urls import reverse
from students.models import Student, Course


@pytest.mark.django_db
def test_get_first_course(client, courses_factory):
    courses = courses_factory(_quantity=1)
    courses_first = Course.objects.first()
    url = reverse('courses-detail', args=(courses_first.id, ))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == courses_first.id
    assert response.data['name'] == courses_first.name


@pytest.mark.django_db
def test_course_list(client, courses_factory):
    courses = courses_factory(_quantity=7)
    courses_all = Course.objects.all()
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 7


@pytest.mark.django_db
def test_course_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=3)
    courses_one = Course.objects.first()
    url = reverse('courses-list')
    response = client.get(url + f'?id={courses_one.id}')
    assert response.status_code == 200
    assert response.data[0]['id'] == courses_one.id
    assert response.data[0]['name'] == courses_one.name
    assert response.data[0]['students'] == list(courses_one.students.all())


@pytest.mark.django_db
def test_course_filter_name(client, courses_factory):
    courses = courses_factory(_quantity=3)
    courses_one = Course.objects.first()
    url = reverse('courses-list')
    response = client.get(url + f'?name={courses_one.name}')
    assert response.status_code == 200
    assert response.data[0]['id'] == courses_one.id
    assert response.data[0]['name'] == courses_one.name
    assert response.data[0]['students'] == list(courses_one.students.all())


@pytest.mark.django_db
def test_create_course(client):
    course = {
        'id': 3,
        'name': 'Python-разработчик с нуля'
    }
    url = reverse('courses-list')
    request = client.post(url, data=course)
    assert request.status_code == 201


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    courses_fac = courses_factory(_quantity=1)
    courses_one = Course.objects.first()
    url = reverse('courses-detail', args=(courses_one.id, ))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == courses_one.id
    assert response.data['name'] == courses_one.name

    course = {
        'name': 'Python-разработчик с нуля'
    }
    url = reverse('courses-list')
    request = client.patch(url + f'{courses_one.id}/', data=course)
    assert request.status_code == 200

    update_course = Course.objects.get(id__exact=courses_one.id)
    assert update_course.id == courses_one.id
    assert update_course.name == 'Python-разработчик с нуля'


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    courses_first = Course.objects.first()
    url = reverse('courses-detail', args=(courses_first.id, ))
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['id'] == courses_first.id
    assert response.data['name'] == courses_first.name

    url = reverse('courses-list')
    response = client.get(url)
    assert len(response.data) == 1

    response = client.delete(url + f'{courses_first.id}/')
    assert response.status_code == 204 or 202 or 200
    assert response.data is None
