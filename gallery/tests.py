from datetime import date

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Category, Image


class GalleryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание объектов для тестирования
        cls.category1 = Category.objects.create(name="Category 1")
        cls.category2 = Category.objects.create(name="Category 2")
        cls.image1 = Image.objects.create(
            title="Image 1",
            image="test_image1.jpg",
            created_date=date.today(),
            age_limit=18,
        )
        cls.image2 = Image.objects.create(
            title="Image 2",
            image="test_image2.jpg",
            created_date=date.today(),
            age_limit=18,
        )
        cls.image1.categories.add(cls.category1)
        cls.image2.categories.add(cls.category2)

    def test_gallery_view_status_code(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)

    def test_gallery_view_template(self):
        response = self.client.get(reverse("main"))
        self.assertTemplateUsed(response, "gallery.html")

    def test_gallery_view_context(self):
        response = self.client.get(reverse("main"))
        self.assertIn("categories", response.context)
        categories = response.context["categories"]
        self.assertEqual(
            len(categories), 2
        )  # Проверяем, что все категории передаются в контекст

    def test_gallery_view_display(self):
        response = self.client.get(reverse("main"))
        self.assertContains(
            response, self.category1.name
        )  # Проверяем, что имя категории отображается
        self.assertContains(response, self.category2.name)
        self.assertContains(
            response, self.image1.title
        )  # Проверяем, что заголовки изображений отображаются
        self.assertContains(response, self.image2.title)


class ImageDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание объекта для тестирования
        cls.image = Image.objects.create(
            title="Test Image",
            image="test_image.jpg",
            created_date=timezone.now(),
            age_limit=18,
        )

    def test_image_detail_view_with_existing_pk(self):
        response = self.client.get(
            reverse("image_detail", kwargs={"pk": self.image.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "image_detail.html")
        self.assertContains(response, self.image.title)

    def test_image_detail_view_with_non_existing_pk(self):
        non_existing_pk = self.image.pk + 1
        response = self.client.get(
            reverse("image_detail", kwargs={"pk": non_existing_pk})
        )
        self.assertEqual(response.status_code, 404)
