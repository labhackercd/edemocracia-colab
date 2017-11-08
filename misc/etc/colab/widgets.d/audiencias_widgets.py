from colab.widgets.widget_manager import WidgetManager
from colab_audiencias.widgets.home_section import AudienciasHomeSectionWidget
from colab_audiencias.widgets.navigation_links import (
    AudienciasNavigationLinksWidget
)


WidgetManager.register_widget('home_section', AudienciasHomeSectionWidget())
WidgetManager.register_widget('navigation_links',
                              AudienciasNavigationLinksWidget())
