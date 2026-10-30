import reflex as rx

from copy_of_taniz_beauty_and_spa.components.layout import site_layout
from copy_of_taniz_beauty_and_spa.components.treatment_menu import treatment_menu


def treatments_page() -> rx.Component:
    return site_layout(treatment_menu(), active_page="treatments")
