from django import forms
from django.apps import apps
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from . import conf
from .models import MultiPanel, Panel, PanelInfo


class MultiPanelPluginForm(forms.ModelForm):

    class Meta:
        model = MultiPanel
        fields = '__all__'
        widgets = {
            'css_class': forms.Select(
                choices=conf.MULTIPANEL_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.MULTIPANEL_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.MULTIPANEL_WIDTHS,
            )
        }


class MultiPanelPlugin(CMSPluginBase):
    allow_children = conf.MULTIPANEL_ALLOW_CHILDREN
    child_classes = conf.MULTIPANEL_PLUGINS
    fieldsets = conf.MULTIPANEL_FIELDSETS
    form = MultiPanelPluginForm
    model = MultiPanel
    name = _('Panels wrap')
    module = _('content')
    render_template = 'cms/plugins/cms_panels_multipanel.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(MultiPanelPlugin)


class PanelPluginForm(forms.ModelForm):

    class Meta:
        model = Panel
        fields = '__all__'
        widgets = {
            'css_class': forms.Select(
                choices=conf.PANEL_CSS_CLASSES,
            ),
            'height': forms.Select(
                choices=conf.PANEL_HEIGHTS,
            ),
            'width': forms.Select(
                choices=conf.PANEL_WIDTHS,
            )
        }


class PanelPlugin(CMSPluginBase):
    allow_children = conf.PANEL_ALLOW_CHILDREN
    child_classes = conf.PANEL_PLUGINS
    fieldsets = conf.PANEL_FIELDSETS
    form = PanelPluginForm
    model = Panel
    name = _('Panel')
    module = _('content')
    render_template = 'cms/plugins/cms_panels_panel.html'

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(PanelPlugin)


if conf.PANELINFO_LINK_MODEL:
    class PanelInfoLinkInline(admin.StackedInline):
        extra = 1
        max_num = 1
        model = apps.get_model(conf.PANELINFO_LINK_MODEL)
        fields = conf.PANELINFO_LINK_FIELDS


class PanelInfoPluginForm(forms.ModelForm):

    class Meta:
        model = PanelInfo
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(
                attrs={'rows': 5},
            ),
        }


class PanelInfoPlugin(CMSPluginBase):
    allow_children = conf.PANELINFO_ALLOW_CHILDREN
    child_classes = conf.PANELINFO_PLUGINS
    form = PanelInfoPluginForm
    fieldsets = conf.PANELINFO_FIELDSETS
    model = PanelInfo
    module = _('content')
    name = _('Panel info')
    inlines = []
    if conf.PANELINFO_LINK_MODEL:
        inlines = [
            PanelInfoLinkInline
        ]

    render_template = 'cms/plugins/cms_panels_panelinfo.html'
    change_form_template = "admin/cms/plugins/panelinfo_change_form.html"

    class Media:
        css = {
            'all': [
                'admin/cms_panels/css/panelinfo.css',
            ]
        }
        js = [
            'admin/js/vendor/jquery/jquery.js',
            'admin/js/jquery.init.js',
            'admin/cms_panels/js/panelinfo.js',
        ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context

    def render_change_form(self, request, context, *args, **kwargs):
        obj = kwargs.get('obj', None)
        if obj and obj.parent:
            parent = obj.parent
        else:
            parent = self._cms_initial_attributes.get('parent', None)
        if parent:
            context['parent_plugin'], pclass = parent.get_plugin_instance()
        return super(PanelInfoPlugin, self).render_change_form(
            request,
            context,
            *args,
            **kwargs
        )


plugin_pool.register_plugin(PanelInfoPlugin)
