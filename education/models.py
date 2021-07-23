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


class EducationListingPage(Page):
	template = "education/education_listing_page.html"
	max_count = 1
	ad_image = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	content_panels = Page.content_panels + [
	ImageChooserPanel("ad_image"),
	]	

	def get_context(self, request):
		context = super().get_context(request)
		context['social'] = SocialMediaModel.objects.all()
		context['posts'] = EducationDetailPage.objects.all()
		return context


class EducationDetailPage(Page):
	template = "education/education_datail_page.html"
	custom_title = models.CharField(
		max_length=100,
		blank=False,
		null=False,
		help_text='Overwrites the default title',
		unique=True,
		)

	ad_image = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	img = models.ForeignKey(
		"wagtailimages.Image",
		blank=False,
		null=True,
		related_name="+",
		on_delete=models.SET_NULL,
		)

	author = models.ForeignKey(
		User,
		on_delete=models.PROTECT, 
		related_name='details_posts', 
		verbose_name='نویسنده',
		)

	overview = models.TextField(
		'خلاصه', 
		max_length=200,
		)

	content = RichTextField(
		'محتوا',
		)

	pdf_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    	)

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

	updated_time = models.DateTimeField(
		auto_now=True,
		)

	created_time = models.DateTimeField(
		auto_now_add=True,
		)

	pub_time = models.DateTimeField(
		'تاریخ انتشار',
		auto_now_add=True,
		)

	content_panels = Page.content_panels + [
	ImageChooserPanel("ad_image"),
	ImageChooserPanel("img"),
	FieldPanel('custom_title', classname="full"),
	FieldPanel('author', classname="full"),
	FieldPanel('overview', classname="full"),
	FieldPanel('content', classname="full"),
	DocumentChooserPanel('pdf_file'),
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

		context['social'] = SocialMediaModel.objects.all()
		return context