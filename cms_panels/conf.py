from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


DEFAULT_IMAGE_HEIGHT = getattr(
    settings,
    'CMS_PANELS_DEFAULT_IMAGE_HEIGHT',
    675
)
DEFAULT_IMAGE_WIDTH = getattr(
    settings,
    'CMS_PANELS_DEFAULT_IMAGE_WIDTH',
    900
)


MULTIPANEL_ALLOW_CHILDREN = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_ALLOW_CHILDREN',
    True
)
MULTIPANEL_PLUGINS = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_PLUGINS',
    [
        'PanelPlugin',
    ]
)
MULTIPANEL_FIELDSETS = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': [
                'name',
            ],
        }),
        (_('layout'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
                'height',
            ],
        }),
    ]
)
MULTIPANEL_CSS_CLASSES = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_CSS_CLASSES',
    [
        ('', _('None')),
    ]
)
MULTIPANEL_HEIGHTS = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_HEIGHTS',
    [
        ('', _('auto')),
    ]
)
MULTIPANEL_WIDTHS = getattr(
    settings,
    'CMS_PANELS_MULTIPANEL_WIDTHS',
    [
        ('', _('auto')),
    ]
)


PANEL_ALLOW_CHILDREN = getattr(
    settings,
    'CMS_PANELS_PANEL_ALLOW_CHILDREN',
    True
)
PANEL_PLUGINS = getattr(
    settings,
    'CMS_PANELS_PANEL_PLUGINS',
    [
        'PanelInfoPlugin',
    ]
)
PANEL_FIELDSETS = getattr(
    settings,
    'CMS_PANELS_PANEL_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': [
                'name',
                'filer_image',
            ],
        }),
        (_('layout'), {
            'classes': [
                'section',
                'collapse',
            ],
            'fields': [
                'css_class',
                'width',
                'height',
            ],
        }),
    ]
)
PANEL_CSS_CLASSES = getattr(
    settings,
    'CMS_PANELS_PANEL_CSS_CLASSES',
    [
        ('', _('None')),
    ]
)
PANEL_HEIGHTS = getattr(
    settings,
    'CMS_PANELS_PANEL_HEIGHTS',
    [
        ('', _('auto')),
    ]
)
PANEL_WIDTHS = getattr(
    settings,
    'CMS_PANELS_PANEL_WIDTHS',
    [
        ('', _('auto')),
    ]
)

PANELINFO_FIELDSETS = getattr(
    settings,
    'CMS_PANELS_PANELINFO_FIELDSETS',
    [
        (_('content'), {
            'classes': ['section'],
            'fields': [
                'name',
                'filer_icon',
                'body',
            ],
        }),
        (_('menu'), {
            'classes': ['section'],
            'fields': [
                'menu_name',
                'menu_filer_icon',
            ],
        }),
        (_('coordinates'), {
            'classes': [
                'section',
                'coordinates',
            ],
            'fields': [
                ['coordinate_x', 'coordinate_y'],
            ],
        }),
    ]
)
PANELINFO_ALLOW_CHILDREN = getattr(
    settings,
    'CMS_PANELS_PANELINFO_ALLOW_CHILDREN',
    True
)
PANELINFO_PLUGINS = getattr(
    settings,
    'CMS_PANELS_PANELINFO_PLUGINS',
    []
)
PANELINFO_LINK_MODEL = getattr(
    settings,
    'CMS_PANELS_PANELINFO_LINK_MODEL',
    None
)
PANELINFO_LINK_FIELDS = getattr(
    settings,
    'CMS_PANELS_PANELINFO_LINK_FIELDS',
    []
)
