from colab.widgets.widget_manager import WidgetManager
from colab_discourse.widgets.home_section import DiscourseHomeSectionWidget
from colab_discourse.widgets.navigation_links import (
    DiscourseNavigationLinksWidget
)


WidgetManager.register_widget('home_section', DiscourseHomeSectionWidget())
WidgetManager.register_widget('navigation_links',
                              DiscourseNavigationLinksWidget())
