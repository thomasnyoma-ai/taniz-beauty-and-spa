import reflex as rx

from typing import TypedDict

from copy_of_taniz_beauty_and_spa.components.homepage import BOOKING_URL, booking_link, section_label


class Service(TypedDict):
    name: str
    duration: str
    price: str


class Category(TypedDict):
    id: str
    title: str
    number: str
    icon: str
    services: list[Service]


CATALOG: list[Category] = [
    {
        "id": "facials",
        "title": "Facial Treatments",
        "number": "01",
        "icon": "sparkles",
        "services": [
            {"name": "Basic Facials", "duration": "40 min", "price": "₦15,000"},
            {
                "name": "Acne Treatment Facials",
                "duration": "1 hr",
                "price": "₦25,000",
            },
            {
                "name": "Anti-Aging Facials",
                "duration": "1 hr",
                "price": "₦22,000",
            },
            {
                "name": "Derma-Planning Facials",
                "duration": "1 hr",
                "price": "₦20,000",
            },
            {
                "name": "Deep Cleansing Facials",
                "duration": "1 hr",
                "price": "₦18,000",
            },
        ],
    },
    {
        "id": "body",
        "title": "Body Treatment",
        "number": "02",
        "icon": "flower-2",
        "services": [
            {
                "name": "Egyptian Milk Bath",
                "duration": "3 hr",
                "price": "₦45,000",
            },
            {
                "name": "Complete Body Polishing",
                "duration": "2 hr",
                "price": "₦35,000",
            },
            {
                "name": "Face and Body Scrubbing",
                "duration": "1 hr 30 min",
                "price": "₦30,000",
            },
        ],
    },
    {
        "id": "massages",
        "title": "Massages",
        "number": "03",
        "icon": "waves",
        "services": [
            {
                "name": "Hot Stone Massage",
                "duration": "1 hr",
                "price": "₦35,000",
            },
            {
                "name": "Deep Tissue Massage",
                "duration": "1 hr",
                "price": "₦30,000",
            },
            {"name": "Swedish Massage", "duration": "1 hr", "price": "₦25,000"},
            {"name": "Back and Leg", "duration": "30 min", "price": "₦15,000"},
            {
                "name": "Face and Head Massage",
                "duration": "30 min",
                "price": "₦10,000",
            },
        ],
    },
    {
        "id": "waxing",
        "title": "Waxing",
        "number": "04",
        "icon": "feather",
        "services": [
            {
                "name": "Full Body Waxing",
                "duration": "1 hr",
                "price": "₦35,000",
            },
            {"name": "Veejay Waxing", "duration": "30 min", "price": "₦15,000"},
            {"name": "Chest Waxing", "duration": "20 min", "price": "₦7,000"},
            {
                "name": "Bikini Line Waxing",
                "duration": "20 min",
                "price": "₦12,000",
            },
            {
                "name": "Full Hand Waxing",
                "duration": "30 min",
                "price": "₦15,000",
            },
            {
                "name": "Full Leg Waxing",
                "duration": "30 min",
                "price": "₦20,000",
            },
            {"name": "Face Waxing", "duration": "20 min", "price": "₦8,000"},
            {
                "name": "Underarm Waxing",
                "duration": "20 min",
                "price": "₦7,000",
            },
            {"name": "Chin Waxing", "duration": "10 min", "price": "₦5,000"},
        ],
    },
    {
        "id": "lashes",
        "title": "Lashes",
        "number": "05",
        "icon": "eye",
        "services": [
            {"name": "Volume Lashes", "duration": "40 min", "price": "₦20,000"},
            {"name": "Hybrid Lashes", "duration": "40 min", "price": "₦17,000"},
            {
                "name": "Classic Lashes",
                "duration": "30 min",
                "price": "₦14,000",
            },
        ],
    },
    {
        "id": "piercings",
        "title": "Piercings",
        "number": "06",
        "icon": "gem",
        "services": [
            {"name": "Bellybutton", "duration": "10 min", "price": "₦15,000"},
            {
                "name": "Upper Ear Lobes",
                "duration": "10 min",
                "price": "₦5,000",
            },
            {
                "name": "Earlobes Per Hole",
                "duration": "10 min",
                "price": "₦3,000",
            },
        ],
    },
    {
        "id": "mani-pedi",
        "title": "Mani & Pedi",
        "number": "07",
        "icon": "hand",
        "services": [
            {"name": "Manicure", "duration": "25 min", "price": "₦3,000"},
            {"name": "Pedicure", "duration": "40 min", "price": "₦10,000"},
        ],
    },
    {
        "id": "steaming",
        "title": "Veejay Steaming",
        "number": "08",
        "icon": "wind",
        "services": [
            {
                "name": "Veejay Steaming",
                "duration": "15 min",
                "price": "₦5,000",
            },
        ],
    },
]


def category_jump(category_data: Category) -> rx.Component:
    return rx.el.a(
        category_data["title"],
        rx.icon(
            "arrow-down", class_name="h-3.5 w-3.5 shrink-0", aria_hidden=True
        ),
        href=f"#{category_data['id']}",
        class_name="inline-flex min-h-11 w-fit items-center gap-3 rounded-full border border-[#E8008A]/20 bg-white px-4 py-2 text-xs text-[#0F0F0F] transition-colors hover:border-[#E8008A] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A]",
        key=category_data["id"],
    )


def service_row(service_data: Service) -> rx.Component:
    return rx.el.li(
        rx.el.h3(
            service_data["name"],
            class_name="text-base font-medium text-[#0F0F0F] sm:text-lg",
        ),
        rx.el.div(
            rx.el.span(
                rx.icon(
                    "clock-3",
                    class_name="h-3.5 w-3.5 shrink-0",
                    aria_hidden=True,
                ),
                rx.el.span(service_data["duration"]),
                class_name="inline-flex items-center gap-2 text-sm text-[#645B57]",
            ),
            rx.el.span(
                service_data["price"],
                class_name="text-base font-medium tabular-nums text-[#0F0F0F]",
            ),
            class_name="flex flex-wrap items-center justify-between gap-3 sm:contents",
        ),
        rx.el.a(
            "Book",
            rx.icon("arrow-up-right", class_name="h-4 w-4", aria_hidden=True),
            href=BOOKING_URL,
            aria_label=f"Book {service_data['name']} — start a WhatsApp conversation with Taniz to arrange an appointment and confirm availability",
            class_name="inline-flex min-h-11 w-fit items-center gap-2 text-sm font-medium text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A] sm:justify-self-end",
        ),
        key=service_data["name"],
        class_name="grid gap-3 border-b border-[#0F0F0F]/10 bg-white px-5 py-5 last:border-b-0 hover:bg-[#FDF9F7] sm:grid-cols-[minmax(0,1fr)_110px_100px_65px] sm:items-center sm:gap-5 lg:px-7",
    )


CATEGORY_SERVICE_ROWS = {
    category["id"]: rx.fragment(
        *[service_row(service) for service in category["services"]]
    )
    for category in CATALOG
}


def category_section(category_data: Category) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    category_data["number"],
                    class_name="font-['Cormorant_Garamond'] text-2xl italic text-[#A1948D]",
                ),
                rx.match(
                    category_data["icon"],
                    (
                        "sparkles",
                        rx.icon(
                            "sparkles",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "flower-2",
                        rx.icon(
                            "flower-2",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "waves",
                        rx.icon(
                            "waves",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "feather",
                        rx.icon(
                            "feather",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "eye",
                        rx.icon(
                            "eye",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "gem",
                        rx.icon(
                            "gem",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "hand",
                        rx.icon(
                            "hand",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    (
                        "wind",
                        rx.icon(
                            "wind",
                            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                            aria_hidden=True,
                        ),
                    ),
                    rx.icon(
                        "sparkles",
                        class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                        aria_hidden=True,
                    ),
                ),
                class_name="mb-4 flex items-center gap-4",
            ),
            rx.el.h2(
                category_data["title"],
                id=f"{category_data['id']}-heading",
                class_name="font-['Cormorant_Garamond'] text-[36px] font-medium leading-tight text-[#0F0F0F] sm:text-[42px]",
            ),
            class_name="lg:pt-5",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span("Treatment"),
                rx.el.span("Duration"),
                rx.el.span("Price · NGN"),
                rx.el.span("Booking", class_name="text-right"),
                class_name="hidden grid-cols-[minmax(0,1fr)_110px_100px_65px] gap-5 border-b border-[#E8008A]/15 bg-[#FDF9F7] px-5 py-4 text-[10px] uppercase tracking-[0.12em] text-[#645B57] sm:grid lg:px-7",
            ),
            rx.el.ul(
                CATEGORY_SERVICE_ROWS[category_data["id"]],
                class_name="list-none",
            ),
            class_name="min-w-0 overflow-hidden rounded-sm border border-[#E8008A]/20 bg-white",
        ),
        id=category_data["id"],
        aria_labelledby=f"{category_data['id']}-heading",
        key=category_data["id"],
        class_name="grid scroll-mt-32 gap-6 lg:grid-cols-[250px_minmax(0,1fr)] lg:gap-12",
    )


CATEGORY_JUMPS = [category_jump(category) for category in CATALOG]
CATEGORY_SECTIONS = [category_section(category) for category in CATALOG]


def treatment_menu() -> rx.Component:
    return rx.fragment(
        rx.el.section(
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "arrow-left", class_name="h-4 w-4", aria_hidden=True
                    ),
                    "Home",
                    href="/",
                    class_name="mb-9 inline-flex min-h-11 items-center gap-2 text-xs text-[#645B57] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                ),
                section_label("The complete treatment menu"),
                rx.el.div(
                    rx.el.div(
                        rx.el.h1(
                            "Your care. ",
                            rx.el.em(
                                "Your moment.",
                                class_name="font-normal text-[#E8008A]",
                            ),
                            class_name="mt-4 max-w-3xl font-['Cormorant_Garamond'] text-[52px] font-medium leading-[1.04] tracking-[-0.03em] text-[#0F0F0F] sm:text-[72px] lg:text-[82px]",
                        ),
                        rx.el.p(
                            "From facial care and body rituals to the finishing touches. Browse our treatments, then tap to start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability.",
                            class_name="mt-6 max-w-xl text-base leading-7 text-[#645B57]",
                        ),
                    ),
                    booking_link("Book via WhatsApp"),
                    class_name="flex flex-col items-start justify-between gap-8 lg:flex-row lg:items-end",
                ),
                rx.el.nav(
                    rx.fragment(*CATEGORY_JUMPS),
                    aria_label="Jump to a treatment category",
                    class_name="mt-10 flex flex-wrap gap-2 sm:gap-3",
                ),
                rx.el.p(
                    "Prices in Nigerian naira (NGN), as listed in the public Setmore catalog. Confirm current prices, service details and appointment availability directly with Taniz on WhatsApp.",
                    class_name="mt-6 max-w-3xl text-xs leading-6 text-[#645B57]",
                ),
                class_name="mx-auto max-w-[1280px] px-5 pb-12 pt-6 sm:px-8 sm:pb-16 lg:px-12 lg:pt-10",
            ),
            class_name="border-b border-[#0F0F0F]/10 bg-[#FDF9F7]",
        ),
        rx.el.div(
            rx.fragment(*CATEGORY_SECTIONS),
            class_name="mx-auto flex max-w-[1280px] flex-col gap-14 px-5 py-14 sm:px-8 sm:py-20 lg:gap-20 lg:px-12",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    section_label("Before your appointment"),
                    rx.el.h2(
                        "A little time to settle in.",
                        class_name="mt-3 font-['Cormorant_Garamond'] text-[38px] font-medium text-[#0F0F0F] sm:text-[46px]",
                    ),
                    rx.el.p(
                        "Please arrive 10 minutes early. Let the team know about allergies or health conditions, and confirm cancellation and rescheduling terms directly with Taniz when arranging your appointment.",
                        class_name="mt-4 max-w-2xl text-sm leading-7 text-[#645B57]",
                    ),
                ),
                booking_link("Arrange your appointment"),
                class_name="mx-auto flex max-w-[1280px] flex-col items-start justify-between gap-7 px-5 py-12 sm:px-8 lg:flex-row lg:items-center lg:px-12 lg:py-16",
            ),
            class_name="border-t border-[#E8008A]/15 bg-white",
        ),
    )
