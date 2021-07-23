from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib.auth.models import User
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtailvideos.edit_handlers import VideoChooserPanel
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SocialMediaModel(SingletonModel):
    twitter = models.URLField(verbose_name='Twitter web page', null=True, blank=True, unique=True)
    facebook = models.URLField(verbose_name='Facebook web page', null=True, blank=True, unique=True)
    instagram = models.URLField(verbose_name='Instagram web page', null=True, blank=True, unique=True)
    skype = models.URLField(verbose_name='Skype web page', null=True, blank=True, unique=True)
    linkedin = models.URLField(verbose_name='Linedin web page', null=True, blank=True, unique=True)


class HomePage(Page):
    header_of_homepage = models.CharField('متن عنوان اول صفحه اصلی', max_length=300, blank=True)
    header2_of_homepage = models.CharField('متن عنوان دوم صفحه اصلی', max_length=300, blank=True)
    
    img_cover1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img_cover2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img_cover3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    img_about = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    header_about = models.CharField('عنوان درباره ما', max_length=300, blank=True)
    header_about_italic = models.CharField('عنوان دوم درباره ما با فونت ایتالیک', max_length=300, blank=True)
    about_paragraph_check1 = RichTextField('متن نکته اول قسمت درباره ما', max_length=2000, blank=True)
    about_paragraph_check2 = RichTextField('متن نکته دوم قسمت درباره ما', max_length=2000, blank=True)
    about_paragraph_check3 = RichTextField('متن نکته سوم قسمت درباره ما', max_length=2000, blank=True)
    
    about_paragraph = RichTextField('متن آخر قسمت درباره ما', max_length=200, blank=True)
    name_of_counter1 = models.CharField('کلمه اول شمارنده', max_length=30, blank=True)
    counter1 = models.DecimalField('عدد اول شمارنده', max_digits=4, decimal_places=0, default=10)
    name_of_counter2 = models.CharField('کلمه دوم شمارنده', max_length=30, blank=True)
    counter2 = models.DecimalField('عدد دوم شمارنده', max_digits=4, decimal_places=0, default=10)
    name_of_counter3 = models.CharField('کلمه سوم شمارنده', max_length=30, blank=True)
    counter3 = models.DecimalField('عدد سوم شمارنده', max_digits=4, decimal_places=0, default=10)
    name_of_counter4 = models.CharField('کلمه سوم شمارنده', max_length=30, blank=True)
    counter4 = models.DecimalField('عدد سوم شمارنده', max_digits=4, decimal_places=0, default=10)
    header_of_green_box = models.CharField('عنوان باکس سبز بزرگ', max_length=300, blank=True)
    text_of_green_box = models.TextField('متن باکس سبز بزرگ ', max_length=500, blank=True)
    header_of_box1 = models.CharField('عنوان باکس  سفید اول', max_length=300, blank=True)
    text_of_box1 = models.TextField('متن باکس سفید اول', max_length=500, blank=True)
    header_of_box2 = models.CharField('عنوان باکس سفید دوم', max_length=300, blank=True)
    text_of_box2 = models.TextField('متن باکس سفید دوم', max_length=500, blank=True)
    header_of_box3 = models.CharField('عنوان باکس سفید سوم', max_length=300, blank=True)
    text_of_box3 = models.TextField('متن باکس سفید سوم', max_length=500, blank=True)
    
    img_client1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    img_client2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    img_client3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_client4 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_client5 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_client6 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    updated_time = models.DateTimeField('تاریخ بروز رسانی', auto_now=True)
    created_time = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    pub_time = models.DateTimeField('تاریخ انتشار', auto_now_add=True)

    max_count = 1
    content_panels = Page.content_panels + [
        FieldPanel('header_of_homepage', classname="full"),
        FieldPanel('header2_of_homepage', classname="full"),
        ImageChooserPanel("img_cover1"),
        ImageChooserPanel("img_cover2"),
        ImageChooserPanel("img_cover3"),
        ImageChooserPanel("img1"),
        ImageChooserPanel("img2"),
        ImageChooserPanel("img3"),
        ImageChooserPanel('img_about'),
        FieldPanel('header_about', classname="full"),
        FieldPanel('header_about_italic', classname="full"),
        FieldPanel('about_paragraph_check1', classname="full"),
        FieldPanel('about_paragraph_check2', classname="full"),
        FieldPanel('about_paragraph_check3', classname="full"),
        FieldPanel('about_paragraph', classname="full"),
        FieldPanel('name_of_counter1', classname="full"),
        FieldPanel('counter1', classname="full"),
        FieldPanel('name_of_counter2', classname="full"),
        FieldPanel('counter2', classname="full"),
        FieldPanel('name_of_counter3', classname="full"),
        FieldPanel('counter3', classname="full"),
        FieldPanel('name_of_counter4', classname="full"),
        FieldPanel('counter4', classname="full"),
        FieldPanel('header_of_green_box', classname="full"),
        FieldPanel('text_of_green_box', classname="full"),
        FieldPanel('header_of_box1', classname="full"),
        FieldPanel('text_of_box1', classname="full"),
        FieldPanel('header_of_box2', classname="full"),
        FieldPanel('text_of_box2', classname="full"),
        FieldPanel('header_of_box3', classname="full"),
        FieldPanel('text_of_box3', classname="full"),
        ImageChooserPanel('img_client1'),
        ImageChooserPanel('img_client2'),
        ImageChooserPanel('img_client3'),
        ImageChooserPanel('img_client4'),
        ImageChooserPanel('img_client5'),
        ImageChooserPanel('img_client6'),
    ]
    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['social'] = SocialMediaModel.objects.all()
        return context
