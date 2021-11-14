from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin, Page
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField

from . import conf


class MultiPanel(CMSPlugin):

    css_class = models.CharField(
        max_length=200,
        blank=True,
        default='',
        verbose_name=_('CSS class'),
    )
    in_navigation = models.BooleanField(
        default=False,
        verbose_name=_('In navigation'),
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name=_('Visible'),
    )
    height = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('Height'),
    )
    width = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('Width'),
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('Name'),
    )
    slug = models.SlugField(
        max_length=150,
        default='',
        blank=True,
        editable=False,
        verbose_name=_('Slug'),
    )
    cms_page = models.ForeignKey(
        Page,
        editable=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="cms_panels_multipanel_set"
    )

    class Meta:
        verbose_name = _('Panel ')
        verbose_name_plural = _('Panels')

    def __str__(self):
        return '{}'.format(self.name or self.pk or '')

    def save(self, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(MultiPanel, self).save(**kwargs)


class Panel(CMSPlugin):
    css_class = models.CharField(
        max_length=200,
        blank=True,
        default='',
        verbose_name=_('CSS class'),
    )
    in_navigation = models.BooleanField(
        default=False,
        verbose_name=_('In navigation'),
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name=_('Visible'),
    )
    height = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name=_('Height'),
    )
    width = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name=_('Width'),
    )
    name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('Name'),
    )
    slug = models.SlugField(
        max_length=150,
        default='',
        blank=True,
        editable=False,
        verbose_name=_('Slug'),
    )
    filer_image = FilerImageField(
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Image'),
        related_name="cms_panels_panel_image_set"
    )
    menu_name = models.CharField(
        max_length=150,
        default='',
        blank=True,
        verbose_name=_('Name'),
    )
    menu_filer_icon = FilerFileField(
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Icon'),
        related_name='cms_panels_panelinfo_menu_filer_icon_set',
    )
    cms_page = models.ForeignKey(
        Page,
        editable=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="cms_panels_panel_set"
    )

    class Meta:
        verbose_name = _('Panel')
        verbose_name_plural = _('Panels')

    def __str__(self):
        return '{}'.format(self.name or self.pk or '')

    def save(self, **kwargs):
        super(Panel, self).save(**kwargs)

    def get_menu_name(self):
        return self.menu_name or self.name

    def get_menu_filer_icon(self):
        return self.menu_filer_icon

    @property
    def image_height(self):
        if self.image:
            return self.image.height
        return conf.DEFAULT_IMAGE_HEIGHT

    @property
    def image_width(self):
        if self.image:
            return self.image.width
        return conf.DEFAULT_IMAGE_WIDTH


class PanelInfo(CMSPlugin):
    name = models.CharField(
        max_length=150,
        default='',
        verbose_name=_('Name'),
    )
    body = models.TextField(
        default='',
        blank=True,
        verbose_name=_('Text'),
    )
    filer_icon = FilerFileField(
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        verbose_name=_('Icon'),
        related_name='cms_panels_panelinfo_filer_icon_set',
    )
    coordinate_x = models.PositiveIntegerField(
        blank=True,
        default='5000',
        verbose_name=_('X coordinat'),
    )
    coordinate_y = models.PositiveIntegerField(
        blank=True,
        default='5000',
        verbose_name=_('Y coordinat'),
    )

    class Meta:
        verbose_name = _('Panel Info')
        verbose_name_plural = _('Panel Infos')

    def __str__(self):
        return '{}'.format(self.name or self.pk or '')

    def copy_relations(self, original):
        link = original.get_link()
        if link:
            link.id = None
            link.panelinfo = self
            link.save()

    def get_link(self):
        link = None
        if conf.PANELINFO_LINK_MODEL:
            field_name = self.get_link_field_name()
            if field_name:
                link = getattr(self, field_name, None)
        return link

    def get_link_field_name(self):
        field_name = None
        if conf.PANELINFO_LINK_MODEL:
            for f in self._meta.get_fields():
                if f.one_to_one:
                    field_model = '{}.{}'.format(
                        f.related_model._meta.app_label,
                        f.related_model._meta.model_name,
                    )
                    if field_model == conf.PANELINFO_LINK_MODEL.lower():
                        field_name = f.name
                        break
        return field_name

    @property
    def link(self):
        if conf.PANELINFO_LINK_MODEL:
            return self.get_link()

    @property
    def coordinate_x_percent(self):
        return str(float(self.coordinate_x) / 100.0).replace(',', '.')

    @property
    def coordinate_y_percent(self):
        return str(float(self.coordinate_y) / 100.0).replace(',', '.')


class PanelInfoLinkMixin(models.Model):

    panelinfo = models.OneToOneField(
        PanelInfo,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('Panel Info')
    )

    class Meta:
        abstract = True
