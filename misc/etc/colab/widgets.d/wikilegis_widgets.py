from colab.widgets.widget_manager import WidgetManager
from colab_wikilegis.widgets.home_section import WikilegisHomeSectionWidget
from colab_wikilegis.widgets.navigation_links import (
    WikilegisNavigationLinksWidget
)

WidgetManager.register_widget('home_section', WikilegisHomeSectionWidget())
WidgetManager.register_widget('navigation_links',
                              WikilegisNavigationLinksWidget())
