import reflex as rx

from copy_of_taniz_beauty_and_spa.components.branding import draft_logo

BOOKING_URL = "https://wa.me/2349012824009"
ADDRESS = "House 19 Kwara Drive, 3rd Avenue, War College Estate, Gwarinpa, Abuja FCT 900108, Nigeria"
WHATSAPP_URL = "https://wa.me/2349012824009?text=Hello%20Taniz%20Beauty%20%26%20Spa%2C%20I%20would%20like%20to%20plan%20a%20visit.%20Please%20help%20me%20confirm%20treatment%20details%20and%20appointment%20availability.%20Thank%20you."
DIRECTIONS_URL = "https://www.google.com/maps/dir/?api=1&destination=House%2019%20Kwara%20Drive%2C%203rd%20Avenue%2C%20War%20College%20Estate%2C%20Gwarinpa%2C%20Abuja%2C%20Nigeria&travelmode=driving"


def booking_link(label: str = "Book an appointment") -> rx.Component:
    return rx.el.a(
        label,
        rx.icon(
            "arrow-up-right", class_name="h-4 w-4 shrink-0", aria_hidden=True
        ),
        href=BOOKING_URL,
        aria_label=f"{label} — start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability",
        class_name="inline-flex min-h-12 items-center justify-center gap-5 rounded-full bg-[#E8008A] px-6 py-3 text-sm font-medium text-white transition-colors hover:bg-[#C90077] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
    )


def wordmark() -> rx.Component:
    return draft_logo()


def navigation_links(active_page: str = "home") -> rx.Component:
    return rx.fragment(
        rx.el.a(
            "Home",
            href="/",
            aria_current=rx.cond(active_page == "home", "page", "false"),
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name=rx.cond(
                active_page == "home",
                "flex min-h-11 items-center text-sm text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                "flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.a(
            "Treatments",
            href="/treatments",
            aria_current=rx.cond(active_page == "treatments", "page", "false"),
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name=rx.cond(
                active_page == "treatments",
                "flex min-h-11 items-center text-sm text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                "flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.a(
            "Products",
            href="/products",
            aria_current=rx.cond(active_page == "products", "page", "false"),
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name=rx.cond(
                active_page == "products",
                "flex min-h-11 items-center text-sm text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                "flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.a(
            "Experience",
            href="/experience",
            aria_current=rx.cond(active_page == "experience", "page", "false"),
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name=rx.cond(
                active_page == "experience",
                "flex min-h-11 items-center text-sm text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                "flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.a(
            "About Taniz",
            href="/#about",
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name="flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
        ),
        rx.el.a(
            "Visit us",
            href="/contact",
            aria_current=rx.cond(active_page == "contact", "page", "false"),
            on_click=rx.call_script(
                "document.querySelectorAll('header details[open]').forEach(el => el.removeAttribute('open'))"
            ),
            class_name=rx.cond(
                active_page == "contact",
                "flex min-h-11 items-center text-sm text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                "flex min-h-11 items-center text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
    )


def header(active_page: str = "home") -> rx.Component:
    return rx.el.header(
        rx.el.div(
            wordmark(),
            rx.el.nav(
                navigation_links(active_page),
                aria_label="Main navigation",
                class_name="hidden items-center gap-6 xl:flex",
            ),
            rx.el.div(
                booking_link("Book now"),
                rx.el.details(
                    rx.el.summary(
                        rx.icon("menu", class_name="h-5 w-5", aria_hidden=True),
                        rx.el.span("Open navigation", class_name="sr-only"),
                        class_name="flex h-12 w-12 cursor-pointer list-none items-center justify-center rounded-full border border-[#0F0F0F]/15 bg-[#FDF9F7] text-[#0F0F0F] [&::-webkit-details-marker]:hidden focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    rx.el.nav(
                        navigation_links(active_page),
                        aria_label="Mobile navigation",
                        class_name="absolute right-0 top-[66px] flex max-h-[calc(100dvh-130px)] w-60 max-w-[calc(100vw-40px)] flex-col gap-1 overflow-y-auto overscroll-contain rounded-xl border border-[#0F0F0F]/10 bg-[#FDF9F7] p-5",
                    ),
                    class_name="relative xl:hidden",
                ),
                class_name="flex shrink-0 items-center gap-2 max-sm:[&>a]:gap-2 max-sm:[&>a]:px-3 max-sm:[&>a>svg]:hidden",
            ),
            class_name="mx-auto flex min-h-[96px] max-w-[1280px] items-center justify-between gap-2 px-5 sm:gap-4 sm:px-8 lg:px-12",
        ),
        class_name="sticky top-0 z-40 border-b border-[#0F0F0F]/10 bg-[#FDF9F7]/95 backdrop-blur-md",
    )


def section_label(text: str) -> rx.Component:
    return rx.el.p(
        text,
        class_name="text-[11px] font-medium uppercase tracking-[0.22em] text-[#E8008A]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(class_name="h-px w-8 bg-[#E8008A]"),
                    section_label("Your moment of care"),
                    class_name="mb-7 flex items-center gap-3",
                ),
                rx.el.h1(
                    "A little pause.",
                    rx.el.br(),
                    "A more ",
                    rx.el.em(
                        "beautiful", class_name="font-normal text-[#E8008A]"
                    ),
                    rx.el.br(),
                    "you.",
                    class_name="font-['Cormorant_Garamond'] text-[58px] font-medium leading-[0.98] tracking-[-0.035em] text-[#0F0F0F] sm:text-[76px] lg:text-[88px] xl:text-[98px]",
                ),
                rx.el.p(
                    "Welcome to Taniz Beauty & Spa. Make room for yourself with beauty treatments and a restorative pause in Gwarinpa, Abuja.",
                    class_name="mt-7 max-w-[365px] text-base leading-7 text-[#645B57]",
                ),
                rx.el.div(
                    booking_link(),
                    rx.el.a(
                        "Explore treatments",
                        rx.icon(
                            "arrow-down", class_name="h-4 w-4", aria_hidden=True
                        ),
                        href="#treatments",
                        class_name="inline-flex min-h-12 items-center justify-center gap-3 border-b border-[#0F0F0F]/25 px-1 text-sm text-[#0F0F0F] hover:border-[#E8008A] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    class_name="mt-9 flex flex-wrap items-center gap-x-6 gap-y-3",
                ),
                rx.el.div(
                    rx.icon(
                        "map-pin",
                        class_name="h-3.5 w-3.5 text-[#E8008A]",
                        aria_hidden=True,
                    ),
                    rx.el.span(
                        "GWARINPA, ABUJA",
                        class_name="text-[10px] tracking-[0.18em] text-[#645B57]",
                    ),
                    class_name="mt-10 flex items-center gap-2",
                ),
                class_name="py-4 lg:py-10",
            ),
            rx.el.figure(
                rx.el.div(
                    rx.el.img(
                        src="/spa_ivory_beauty.png",
                        alt="Editorial still-life of beauty and spa essentials in warm ivory tones; illustrative imagery, not the Taniz premises.",
                        fetch_priority="high",
                        class_name="h-full w-full object-cover",
                    ),
                    class_name="aspect-[4/5] max-h-[610px] w-full overflow-hidden rounded-t-[220px] rounded-b-[4px] bg-[#EDE5DE] sm:aspect-[5/6]",
                ),
                rx.el.figcaption(
                    rx.el.span(
                        "THE ART OF TAKING A MOMENT",
                        class_name="text-[9px] tracking-[0.2em] text-[#645B57]",
                    ),
                    rx.el.span(
                        "An editorial still-life",
                        class_name="font-['Cormorant_Garamond'] text-base italic text-[#645B57]",
                    ),
                    class_name="mt-4 flex flex-wrap items-center justify-between gap-2",
                ),
                class_name="w-full min-w-0 lg:pl-5",
            ),
            class_name="mx-auto grid max-w-[1280px] items-center gap-10 px-5 py-10 sm:px-8 sm:py-14 md:grid-cols-2 lg:gap-16 lg:px-12 lg:py-16",
        ),
        aria_label="Welcome to Taniz Beauty and Spa",
    )


def treatment_card(
    number: str,
    icon: str,
    category: str,
    title: str,
    description: str,
    price: str,
) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.span(
                number,
                class_name="font-['Cormorant_Garamond'] text-xl italic text-[#A1948D]",
            ),
            rx.icon(
                icon,
                class_name="h-7 w-7 stroke-[1.2] text-[#E8008A]",
                aria_hidden=True,
            ),
            class_name="mb-10 flex items-center justify-between",
        ),
        rx.el.p(
            category,
            class_name="mb-3 text-[10px] uppercase tracking-[0.2em] text-[#645B57]",
        ),
        rx.el.h3(
            title,
            class_name="font-['Cormorant_Garamond'] text-[34px] font-medium leading-tight text-[#0F0F0F]",
        ),
        rx.el.p(
            description,
            class_name="mt-3 max-w-xs text-sm leading-6 text-[#645B57]",
        ),
        rx.el.div(
            rx.el.span(price, class_name="text-lg font-medium text-[#0F0F0F]"),
            rx.el.a(
                "Book treatment",
                rx.icon(
                    "arrow-up-right", class_name="h-4 w-4", aria_hidden=True
                ),
                href=BOOKING_URL,
                aria_label=f"Book {title} — start a WhatsApp conversation with Taniz to arrange an appointment and confirm availability",
                class_name="inline-flex min-h-11 items-center gap-2 text-sm text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
            class_name="mt-auto flex flex-wrap items-center justify-between gap-3 border-t border-[#0F0F0F]/10 pt-5",
        ),
        class_name="flex min-h-[345px] flex-col rounded-sm border border-[#0F0F0F]/10 bg-[#FDF9F7] p-7 transition-colors hover:border-[#E8008A]/40 lg:p-8",
    )


def treatments() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    section_label("The treatment edit"),
                    rx.el.h2(
                        "Care, from head to toe.",
                        class_name="mt-3 font-['Cormorant_Garamond'] text-[42px] font-medium leading-tight tracking-[-0.02em] text-[#0F0F0F] sm:text-[52px]",
                    ),
                ),
                rx.el.p(
                    "A facial refresh, a slower moment, a finishing touch. Find a little something for you.",
                    class_name="max-w-[295px] text-sm leading-6 text-[#645B57]",
                ),
                class_name="mb-9 flex flex-col justify-between gap-5 md:flex-row md:items-end",
            ),
            rx.el.div(
                treatment_card(
                    "01",
                    "sparkles",
                    "Face & skin",
                    "Basic Facial",
                    "Make time for your skin with a simple facial refresh.",
                    "₦15,000",
                ),
                treatment_card(
                    "02",
                    "waves",
                    "Body & relaxation",
                    "Swedish Massage",
                    "Step out of your busy day and into a moment of relaxation.",
                    "₦25,000",
                ),
                treatment_card(
                    "03",
                    "flower-2",
                    "Hands & feet",
                    "Classic Pedicure",
                    "A little attention for your feet. A lovely finishing touch.",
                    "₦10,000",
                ),
                class_name="grid grid-cols-1 gap-5 md:grid-cols-3",
            ),
            rx.el.div(
                rx.el.p(
                    "A selection of our treatments. Tap Book to start a WhatsApp conversation with Taniz and confirm appointment availability.",
                    class_name="max-w-xl text-xs leading-5 text-[#645B57]",
                ),
                rx.el.a(
                    "View all treatments & prices",
                    rx.icon(
                        "arrow-right", class_name="h-4 w-4", aria_hidden=True
                    ),
                    href="/treatments",
                    class_name="inline-flex min-h-11 items-center gap-3 text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                ),
                class_name="mt-6 flex flex-col justify-between gap-2 sm:flex-row sm:items-center",
            ),
            class_name="mx-auto max-w-[1280px] px-5 py-16 sm:px-8 lg:px-12 lg:py-20",
        ),
        id="treatments",
        aria_label="Treatments and prices",
        class_name="scroll-mt-24 border-y border-[#0F0F0F]/10 bg-white",
    )


def about() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_label("A little about Taniz"),
                rx.el.h2(
                    "Not another task.\nTime for yourself.",
                    class_name="mt-4 whitespace-pre-line font-['Cormorant_Garamond'] text-[44px] font-medium leading-[1.08] tracking-[-0.02em] text-[#0F0F0F] sm:text-[56px]",
                ),
                rx.el.p(
                    "Beauty and wellbeing belong in the same moment. At Taniz Beauty & Spa, our treatment menu brings facial care, massage and beauty essentials together in Gwarinpa, Abuja.",
                    class_name="mt-6 max-w-md text-base leading-7 text-[#645B57]",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "heart",
                        class_name="h-5 w-5 shrink-0 stroke-[1.5] text-[#E8008A]",
                        aria_hidden=True,
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Choose your kind of care",
                            class_name="font-['Cormorant_Garamond'] text-2xl font-medium text-[#0F0F0F]",
                        ),
                        rx.el.p(
                            "From a facial to a pedicure, explore treatments that fit the moment.",
                            class_name="mt-2 text-sm leading-6 text-[#645B57]",
                        ),
                    ),
                    class_name="flex gap-5 border-b border-[#0F0F0F]/10 pb-7",
                ),
                rx.el.div(
                    rx.icon(
                        "calendar-days",
                        class_name="h-5 w-5 shrink-0 stroke-[1.5] text-[#E8008A]",
                        aria_hidden=True,
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Make a little room in your day",
                            class_name="font-['Cormorant_Garamond'] text-2xl font-medium text-[#0F0F0F]",
                        ),
                        rx.el.p(
                            "Tap to start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability.",
                            class_name="mt-2 text-sm leading-6 text-[#645B57]",
                        ),
                    ),
                    class_name="flex gap-5 pt-7",
                ),
                class_name="w-full max-w-md md:justify-self-end",
            ),
            class_name="mx-auto grid max-w-[1280px] items-center gap-12 px-5 py-16 sm:px-8 md:grid-cols-2 lg:gap-24 lg:px-12 lg:py-24",
        ),
        id="about",
        class_name="scroll-mt-24 bg-[#FDF9F7]",
    )


def preview_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        rx.icon("arrow-right", class_name="h-4 w-4 shrink-0", aria_hidden=True),
        href=href,
        class_name="mt-5 inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] hover:underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
    )


def homepage_previews() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_label("A little more to discover"),
                rx.el.h2(
                    "Your care, your way.",
                    class_name="mt-3 font-['Cormorant_Garamond'] text-[42px] font-medium leading-tight text-[#0F0F0F] sm:text-[52px]",
                ),
                class_name="mb-9",
            ),
            rx.el.div(
                rx.el.article(
                    rx.icon(
                        "droplets",
                        class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                        aria_hidden=True,
                    ),
                    rx.el.h3(
                        "Beyond the spa.",
                        class_name="mt-6 font-['Cormorant_Garamond'] text-[34px] font-medium text-[#0F0F0F]",
                    ),
                    rx.el.p(
                        "Explore Taniz’s face care, body care, soaps and scrubs. Ask about product details and current availability before choosing.",
                        class_name="mt-3 text-sm leading-6 text-[#645B57]",
                    ),
                    preview_link(
                        "Discover the skincare collection", "/products"
                    ),
                    class_name="flex flex-col justify-center rounded-sm border border-[#0F0F0F]/10 bg-[#FDF9F7] p-7 sm:p-8",
                ),
                rx.el.article(
                    rx.el.img(
                        src="/taniz-gallery-1.jpg",
                        alt="A photograph from Taniz Beauty & Spa’s public Setmore gallery",
                        loading="lazy",
                        class_name="h-56 w-full rounded-sm bg-[#EDE5DE] object-cover",
                    ),
                    rx.el.h3(
                        "A glimpse of Taniz.",
                        class_name="mt-6 font-['Cormorant_Garamond'] text-[34px] font-medium text-[#0F0F0F]",
                    ),
                    rx.el.p(
                        "Take a look at spa and treatment moments through the authentic photographs in Taniz’s public gallery.",
                        class_name="mt-3 text-sm leading-6 text-[#645B57]",
                    ),
                    preview_link("Explore the spa experience", "/experience"),
                    class_name="min-w-0",
                ),
                class_name="grid gap-8 md:grid-cols-2 lg:gap-12",
            ),
            rx.el.div(
                rx.el.div(
                    section_label("Find us in Gwarinpa"),
                    rx.el.h3(
                        "A pause, close to home.",
                        class_name="mt-3 font-['Cormorant_Garamond'] text-[34px] font-medium text-[#0F0F0F]",
                    ),
                    rx.el.p(
                        "House 19 Kwara Drive, War College Estate, Abuja. Monday–Saturday, 9:00 AM–6:00 PM WAT; Sunday closed.",
                        class_name="mt-3 max-w-xl text-sm leading-6 text-[#645B57]",
                    ),
                ),
                preview_link("Plan your visit", "/contact"),
                class_name="mt-12 flex flex-col justify-between gap-4 border-t border-[#0F0F0F]/10 pt-9 md:flex-row md:items-center",
            ),
            class_name="mx-auto max-w-[1280px] px-5 py-16 sm:px-8 lg:px-12 lg:py-20",
        ),
        aria_label="Discover products, the spa experience and visiting Taniz",
        class_name="border-t border-[#0F0F0F]/10 bg-white",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "COME AS YOU ARE",
                        class_name="text-[10px] tracking-[0.22em] text-[#F5A6D3]",
                    ),
                    rx.el.h2(
                        "Your next pause\nstarts here.",
                        class_name="mt-4 whitespace-pre-line font-['Cormorant_Garamond'] text-[48px] font-medium leading-[1.05] text-white sm:text-[64px]",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "map-pin",
                            class_name="h-5 w-5 text-[#F5A6D3]",
                            aria_hidden=True,
                        ),
                        rx.el.p(
                            "Find us in", class_name="text-sm text-white/65"
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.address(
                        ADDRESS,
                        class_name="mt-3 max-w-lg text-base not-italic leading-7 text-white",
                    ),
                    rx.el.p(
                        "Monday–Saturday · 9:00 AM–6:00 PM WAT\nSunday closed",
                        class_name="mt-4 whitespace-pre-line text-sm leading-6 text-white/65",
                    ),
                    rx.el.div(
                        booking_link("Book your moment"),
                        rx.el.a(
                            "Plan your visit",
                            rx.icon(
                                "arrow-right",
                                class_name="h-4 w-4",
                                aria_hidden=True,
                            ),
                            href="/contact",
                            class_name="inline-flex min-h-12 items-center gap-3 text-sm text-white/80 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                        ),
                        class_name="mt-6 flex flex-wrap items-center gap-5",
                    ),
                    rx.el.div(
                        rx.el.a(
                            "Call +234 903 789 7510",
                            href="tel:+2349037897510",
                            class_name="inline-flex min-h-11 items-center gap-2 text-sm text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                        ),
                        rx.el.a(
                            "WhatsApp +234 901 282 4009",
                            href=WHATSAPP_URL,
                            class_name="inline-flex min-h-11 items-center text-sm text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                        ),
                        rx.el.a(
                            "tanizbeautyandspa986@gmail.com",
                            href="mailto:tanizbeautyandspa986@gmail.com",
                            class_name="inline-flex min-h-11 items-center break-all text-sm text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                        ),
                        class_name="mt-4 flex min-w-0 flex-col items-start",
                    ),
                ),
                class_name="grid items-center gap-10 border-b border-white/15 pb-14 md:grid-cols-2",
            ),
            rx.el.div(
                rx.el.div(
                    wordmark(),
                    rx.el.p(
                        "A little care goes a long way.",
                        class_name="mt-1 text-xs text-white/60",
                    ),
                ),
                rx.el.nav(
                    rx.el.a(
                        "Treatments",
                        href="/treatments",
                        class_name="inline-flex min-h-11 items-center text-xs text-white/75 hover:text-white",
                    ),
                    rx.el.a(
                        "Products",
                        href="/products",
                        class_name="inline-flex min-h-11 items-center text-xs text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    rx.el.a(
                        "Experience",
                        href="/experience",
                        class_name="inline-flex min-h-11 items-center text-xs text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    rx.el.a(
                        "About",
                        href="/#about",
                        class_name="inline-flex min-h-11 items-center text-xs text-white/75 hover:text-white",
                    ),
                    rx.el.a(
                        "Visit us",
                        href="/contact",
                        class_name="inline-flex min-h-11 items-center text-xs text-white/75 hover:text-white focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    rx.el.a(
                        "Back to top",
                        rx.icon(
                            "arrow-up", class_name="h-3 w-3", aria_hidden=True
                        ),
                        href="#home",
                        class_name="inline-flex min-h-11 items-center gap-2 text-xs text-white/75 hover:text-white",
                    ),
                    aria_label="Footer navigation",
                    class_name="flex flex-wrap gap-x-6 gap-y-1",
                ),
                class_name="flex flex-col justify-between gap-6 pt-8 lg:flex-row lg:items-center",
            ),
            class_name="mx-auto max-w-[1280px] px-5 py-16 sm:px-8 lg:px-12 lg:py-20",
        ),
        id="visit",
        class_name="scroll-mt-24 bg-[#0F0F0F] text-white",
    )
