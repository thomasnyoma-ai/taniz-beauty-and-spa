import reflex as rx

from copy_of_taniz_beauty_and_spa.components.homepage import about, hero, treatments, homepage_previews
from copy_of_taniz_beauty_and_spa.components.layout import site_layout
from copy_of_taniz_beauty_and_spa.pages.treatments import treatments_page
from copy_of_taniz_beauty_and_spa.pages.products import products_page
from copy_of_taniz_beauty_and_spa.pages.experience import experience_page
from copy_of_taniz_beauty_and_spa.pages.contact import contact_page


def index() -> rx.Component:
    return site_layout(
        rx.fragment(hero(), treatments(), about(), homepage_previews())
    )


app = rx.App(
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Outfit:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index,
    route="/",
    title="Taniz Beauty & Spa | Your moment of care in Abuja",
    description="Explore facial care, massage and beauty treatments at Taniz Beauty & Spa in Gwarinpa, Abuja. View treatment prices and start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability.",
)
app.add_page(
    treatments_page,
    route="/treatments",
    title="Treatments & Prices | Taniz Beauty & Spa, Abuja",
    description="Browse Taniz Beauty & Spa’s facial treatments, body treatments, massages, waxing, lashes, piercings, manicure, pedicure and Veejay Steaming. See durations and naira prices, then arrange a spa appointment and confirm availability with Taniz via WhatsApp.",
)
app.add_page(
    products_page,
    route="/products",
    title="Skincare Products | Taniz Beauty & Spa, Abuja",
    description="Explore Taniz’s face care, body care, soaps and scrubs. Enquire about individual products on WhatsApp to confirm details and current availability.",
)
app.add_page(
    experience_page,
    route="/experience",
    title="The Spa Experience | Taniz Beauty & Spa, Abuja",
    description="Discover Taniz Beauty & Spa in Gwarinpa, Abuja through authentic photographs from its public gallery. Explore the treatment menu and start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability.",
)
app.add_page(
    contact_page,
    route="/contact",
    title="Contact & Visit Us | Taniz Beauty & Spa, Gwarinpa, Abuja",
    description="Visit Taniz Beauty & Spa at House 19 Kwara Drive, War College Estate, Gwarinpa, Abuja. Find opening hours, directions, phone, WhatsApp and email, or arrange a spa appointment and confirm availability with Taniz via WhatsApp.",
)
