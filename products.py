import reflex as rx

from urllib.parse import quote

from copy_of_taniz_beauty_and_spa.components.homepage import section_label
from copy_of_taniz_beauty_and_spa.components.layout import site_layout


def _catalog(names: list[str]) -> list[dict[str, str]]:
    return [
        {
            "name": name,
            "url": f"https://wa.me/2349012824009?text={quote(f'Hello Taniz Beauty & Spa, I would like to enquire about {name}. Please confirm the product details and current availability. Thank you.', safe='')}",
        }
        for name in names
    ]


FACE_PRODUCTS = _catalog(
    [
        "Face Treatment Cleanser",
        "Sunburn Cleanser",
        "Spot Corrector",
        "Glow Face Cream",
        "Princess Beulah Face Cream",
        "Acne Face Wash",
        "Face Black Soap",
        "Sunscreen",
        "Facial Scrub",
    ]
)
BODY_PRODUCTS = _catalog(
    [
        "Glow Body Butter",
        "Caramel Body Milk",
        "Kids Body Butter",
        "Queen Hephzibah Oil",
        "Glow Oil",
        "Customized Body Wash",
    ]
)
SOAP_PRODUCTS = _catalog(
    [
        "Sugar Scrub",
        "Coffee Scrub",
        "Milk & Oats Bar Soap",
        "Egg Soap",
        "Upgraded Customized Soap",
    ]
)


def product_card(product: dict[str, str]) -> rx.Component:
    return rx.el.article(
        rx.el.h3(
            product["name"],
            class_name="font-['Cormorant_Garamond'] text-[28px] font-medium leading-tight text-[#0F0F0F]",
        ),
        rx.el.a(
            "Enquire on WhatsApp",
            rx.icon(
                "arrow-up-right",
                class_name="h-4 w-4 shrink-0",
                aria_hidden=True,
            ),
            href=product["url"],
            target="_blank",
            rel="noopener noreferrer",
            aria_label=f"Enquire about {product['name']} on WhatsApp (opens in a new tab)",
            class_name="mt-6 inline-flex min-h-12 w-fit items-center gap-3 text-sm text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
        ),
        key=product["name"],
        class_name="flex h-full flex-col justify-between rounded-sm border border-[#0F0F0F]/10 bg-white p-6 transition-colors hover:border-[#E8008A]/40 sm:p-7",
    )


def category_jump(label: str, anchor: str) -> rx.Component:
    return rx.el.a(
        label,
        rx.icon("arrow-down", class_name="h-4 w-4", aria_hidden=True),
        href=f"#{anchor}",
        class_name="inline-flex min-h-12 items-center justify-center gap-4 rounded-full border border-[#E8008A]/25 bg-white px-5 py-3 text-sm text-[#0F0F0F] hover:border-[#E8008A] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
    )


def product_category(
    number: str,
    title: str,
    anchor: str,
    icon: str,
    description: str,
    products: list[dict[str, str]],
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.span(
                number,
                class_name="font-['Cormorant_Garamond'] text-xl italic text-[#A1948D]",
            ),
            rx.icon(
                icon,
                class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                aria_hidden=True,
            ),
            class_name="mb-5 flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.h2(
                title,
                id=f"{anchor}-heading",
                class_name="font-['Cormorant_Garamond'] text-[42px] font-medium leading-tight text-[#0F0F0F] sm:text-[52px]",
            ),
            rx.el.p(
                description,
                class_name="max-w-md text-sm leading-6 text-[#645B57]",
            ),
            class_name="mb-8 flex flex-col justify-between gap-4 md:flex-row md:items-end",
        ),
        rx.el.div(
            rx.foreach(products, product_card),
            class_name="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3",
        ),
        id=anchor,
        aria_labelledby=f"{anchor}-heading",
        class_name="scroll-mt-28 border-b border-[#0F0F0F]/10 py-14 sm:py-16",
    )


def products_intro() -> rx.Component:
    return rx.el.section(
        section_label("The Taniz skincare collection"),
        rx.el.h1(
            "A little care.",
            rx.el.br(),
            rx.el.em(
                "Beyond the spa.", class_name="font-normal text-[#E8008A]"
            ),
            class_name="mt-5 font-['Cormorant_Garamond'] text-[54px] font-medium leading-[1.02] tracking-[-0.025em] text-[#0F0F0F] sm:text-[76px] lg:text-[88px]",
        ),
        rx.el.p(
            "Explore the skincare collection named in the Taniz product catalogue. From face care to body care, soaps and scrubs, start a conversation about the products that interest you.",
            class_name="mt-7 max-w-2xl text-base leading-7 text-[#645B57]",
        ),
        rx.el.nav(
            category_jump("Face Care", "face-care"),
            category_jump("Body Care", "body-care"),
            category_jump("Soaps & Scrubs", "soaps-scrubs"),
            aria_label="Jump to a product category",
            class_name="mt-9 flex flex-wrap gap-3",
        ),
        rx.el.div(
            rx.icon(
                "message-circle",
                class_name="mt-1 h-5 w-5 shrink-0 text-[#E8008A]",
                aria_hidden=True,
            ),
            rx.el.p(
                "Each enquiry opens WhatsApp with the product name included. Please confirm product details and current availability with Taniz before purchasing. Prices are not listed in the draft catalogue.",
                class_name="max-w-2xl text-sm leading-6 text-[#645B57]",
            ),
            class_name="mt-8 flex items-start gap-3",
        ),
        class_name="border-b border-[#0F0F0F]/10 pb-12 pt-14 sm:pb-16 sm:pt-20",
    )


def products_page() -> rx.Component:
    return site_layout(
        rx.el.div(
            products_intro(),
            product_category(
                "01",
                "Face Care",
                "face-care",
                "sparkles",
                "Explore cleansers, creams and the rest of the face care collection.",
                FACE_PRODUCTS,
            ),
            product_category(
                "02",
                "Body Care",
                "body-care",
                "droplets",
                "Browse body butters, milk, oils and body wash.",
                BODY_PRODUCTS,
            ),
            product_category(
                "03",
                "Soaps & Scrubs",
                "soaps-scrubs",
                "flower-2",
                "Discover the soaps and scrubs in the Taniz collection.",
                SOAP_PRODUCTS,
            ),
            rx.el.section(
                section_label("A conversation comes first"),
                rx.el.h2(
                    "Not sure where to begin?",
                    class_name="mt-4 font-['Cormorant_Garamond'] text-[40px] font-medium leading-tight text-[#0F0F0F] sm:text-[48px]",
                ),
                rx.el.p(
                    "Ask Taniz about ingredients, directions for use and which products are currently available. Product names alone do not establish suitability for your skin.",
                    class_name="mt-4 max-w-xl text-base leading-7 text-[#645B57]",
                ),
                rx.el.a(
                    "Talk to Taniz on WhatsApp",
                    rx.icon(
                        "arrow-up-right", class_name="h-4 w-4", aria_hidden=True
                    ),
                    href="https://wa.me/2349012824009?text=Hello%20Taniz%20Beauty%20%26%20Spa%2C%20I%20would%20like%20to%20enquire%20about%20your%20skincare%20collection%20and%20current%20availability.",
                    target="_blank",
                    rel="noopener noreferrer",
                    class_name="mt-7 inline-flex min-h-12 items-center justify-center gap-4 rounded-full bg-[#E8008A] px-6 py-3 text-sm font-medium text-white hover:bg-[#C90077] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
                ),
                class_name="py-16 sm:py-20",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 sm:px-8 lg:px-12",
        ),
        active_page="products",
    )
