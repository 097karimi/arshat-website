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
from home.models import SocialMediaModel

class EmployeeModel(models.Model):
    name_of_employee = models.CharField('نام کادر اجرایی', max_length=50, blank=True)
    position_of_employee = models.CharField('عنوان شغل', max_length=50, blank=True)
    img_of_employee = models.ImageField('عکس کادر اجرایی 400 * 400')
    introduction_of_employee = RichTextField('یک متن مختصری از زبان کادر اجرایی', max_length=500, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name_of_employee, self.position_of_employee)

    class Meta:
        ordering = ['name_of_employee']
        verbose_name_plural = "Employee"


class AboutPage(Page):
    img_about_ad = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_about1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_about2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
        
    img_about3 = models.ForeignKey(
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
    name_of_counter2 = models.CharField('کلمه دوم شمارنده', max_length=30, default=" ", blank=True)
    counter2 = models.DecimalField('عدد دوم شمارنده', max_digits=4, decimal_places=0, default=10)
    name_of_counter3 = models.CharField('کلمه سوم شمارنده', max_length=30, default=" ", blank=True)
    counter3 = models.DecimalField('عدد سوم شمارنده', max_digits=4, decimal_places=0, default=10)
    name_of_counter4 = models.CharField('کلمه سوم شمارنده', max_length=30, default=" ", blank=True)
    counter4 = models.DecimalField('عدد سوم شمارنده', max_digits=4, decimal_places=0, default=10)
    
    header_video = models.ForeignKey('wagtailvideos.Video',
                                     related_name='+',
                                     blank=True,
                                     null=True,
                                     on_delete=models.SET_NULL)

    zip_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
        )

    gallery1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery4 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery5 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery6 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery7 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery8 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )

    gallery9 = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        )
    
    updated_time = models.DateTimeField('تاریخ بروز رسانی', auto_now=True)
    created_time = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    pub_time = models.DateTimeField('تاریخ انتشار', auto_now_add=True)

    max_count = 1
    content_panels = Page.content_panels + [
        ImageChooserPanel('img_about_ad', classname="full"),
        ImageChooserPanel('img_about1', classname="full"),
        ImageChooserPanel('img_about2', classname="full"),
        ImageChooserPanel('img_about3', classname="full"),
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
        VideoChooserPanel('header_video'),
        VideoChooserPanel('zip_file'),
        ImageChooserPanel("gallery1"),
        ImageChooserPanel("gallery2"),
        ImageChooserPanel("gallery3"),
        ImageChooserPanel("gallery4"),
        ImageChooserPanel("gallery5"),
        ImageChooserPanel("gallery6"),
        ImageChooserPanel("gallery7"),
        ImageChooserPanel("gallery8"),
        ImageChooserPanel("gallery9"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['employee'] = EmployeeModel.objects.all()
        context['social'] = SocialMediaModel.objects.all()
        return context
