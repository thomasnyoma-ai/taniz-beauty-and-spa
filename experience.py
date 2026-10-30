import reflex as rx

from copy_of_taniz_beauty_and_spa.components.homepage import booking_link, section_label
from copy_of_taniz_beauty_and_spa.components.layout import site_layout

GALLERY_URL = "https://tanizbeautyandspa.setmore.com/gallery"


def gallery_image(src: str, number: str, classes: str) -> rx.Component:
    return rx.el.figure(
        rx.el.a(
            rx.el.span(
                f"Spa and treatment moment from the public Taniz Beauty & Spa gallery, photograph {number}.",
                class_name="sr-only",
            ),
            style={
                "background_image": f"url('{src}')",
                "background_position": "center",
                "background_size": "cover",
                "background_repeat": "no-repeat",
            },
            href=src,
            target="_blank",
            rel="noopener noreferrer",
            aria_label=f"View Taniz gallery photograph {number} in full (opens in a new tab)",
            class_name="group block h-full w-full overflow-hidden rounded-sm bg-[#EDE5DE] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
        ),
        rx.el.figcaption(
            f"Taniz gallery · {number}",
            class_name="mt-3 text-xs tracking-wide text-[#645B57]",
        ),
        class_name=classes,
    )


def experience_intro() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_label("The Taniz experience · Gwarinpa, Abuja"),
            rx.el.h1(
                "Step out of the rush.",
                rx.el.br(),
                rx.el.em(
                    "Into your moment.", class_name="font-normal text-[#E8008A]"
                ),
                class_name="mt-5 font-['Cormorant_Garamond'] text-[52px] font-medium leading-[1.04] tracking-[-0.025em] text-[#0F0F0F] sm:text-[72px] lg:text-[84px]",
            ),
            class_name="min-w-0",
        ),
        rx.el.div(
            rx.el.p(
                "A facial, a massage, a little attention to the details. Taniz Beauty & Spa brings beauty and body care together in Gwarinpa, Abuja, with room in the treatment menu for your kind of pause.",
                class_name="text-base leading-7 text-[#645B57]",
            ),
            rx.el.div(
                booking_link("Find your moment via WhatsApp"), class_name="mt-7"
            ),
            rx.el.a(
                "Explore the gallery",
                rx.icon("arrow-down", class_name="h-4 w-4", aria_hidden=True),
                href="#spa-gallery",
                class_name="mt-4 inline-flex min-h-12 items-center gap-3 text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
            class_name="max-w-md lg:pt-10",
        ),
        class_name="grid gap-8 py-14 sm:py-20 lg:grid-cols-[1.4fr_1fr] lg:items-end lg:gap-14",
    )


def spa_gallery() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_label("A glimpse inside"),
                rx.el.h2(
                    "Moments at Taniz.",
                    id="gallery-heading",
                    class_name="mt-3 font-['Cormorant_Garamond'] text-[42px] font-medium text-[#0F0F0F] sm:text-[52px]",
                ),
            ),
            rx.el.p(
                "Authentic photographs shared in Taniz’s public Setmore gallery. Select any image to view it in full.",
                class_name="max-w-sm text-sm leading-6 text-[#645B57]",
            ),
            class_name="mb-8 flex flex-col justify-between gap-4 md:flex-row md:items-end",
        ),
        rx.el.div(
            gallery_image(
                "/taniz-gallery-1.jpg",
                "01",
                "flex min-w-0 flex-col [&>a]:h-[340px] sm:col-span-2 sm:[&>a]:h-[440px] lg:col-span-7 lg:[&>a]:h-[520px]",
            ),
            gallery_image(
                "/taniz-gallery-2.jpg",
                "02",
                "flex min-w-0 flex-col [&>a]:h-[340px] sm:[&>a]:h-[360px] lg:col-span-5 lg:[&>a]:h-[520px]",
            ),
            gallery_image(
                "/taniz-gallery-3.jpg",
                "03",
                "flex min-w-0 flex-col [&>a]:h-[340px] sm:[&>a]:h-[360px] lg:col-span-4 lg:[&>a]:h-[340px]",
            ),
            gallery_image(
                "/taniz-gallery-4.jpg",
                "04",
                "flex min-w-0 flex-col [&>a]:h-[340px] sm:[&>a]:h-[360px] lg:col-span-4 lg:[&>a]:h-[340px]",
            ),
            gallery_image(
                "/taniz-gallery-5.jpg",
                "05",
                "flex min-w-0 flex-col [&>a]:h-[340px] sm:[&>a]:h-[360px] lg:col-span-4 lg:[&>a]:h-[340px]",
            ),
            class_name="grid grid-cols-1 gap-x-5 gap-y-8 sm:grid-cols-2 lg:grid-cols-12",
        ),
        rx.el.a(
            "View the public Setmore gallery",
            rx.icon("arrow-up-right", class_name="h-4 w-4", aria_hidden=True),
            href=GALLERY_URL,
            target="_blank",
            rel="noopener noreferrer",
            class_name="mt-6 inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
        ),
        id="spa-gallery",
        aria_labelledby="gallery-heading",
        class_name="scroll-mt-28 border-t border-[#0F0F0F]/10 py-14 sm:py-16",
    )


def experience_story() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_label("Beauty & wellbeing, together"),
            rx.el.h2(
                "More than one way\nto take a pause.",
                class_name="mt-4 whitespace-pre-line font-['Cormorant_Garamond'] text-[42px] font-medium leading-[1.08] text-[#0F0F0F] sm:text-[54px]",
            ),
            rx.el.p(
                "Taniz’s public service menu includes facials, massages, body scrubbing, body polishing and milk baths, alongside waxing, lashes, manicure and pedicure. Choose the care you want to make time for.",
                class_name="mt-6 max-w-xl text-base leading-7 text-[#645B57]",
            ),
            rx.el.a(
                "Explore treatments & prices",
                rx.icon("arrow-right", class_name="h-4 w-4", aria_hidden=True),
                href="/treatments",
                class_name="mt-5 inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] hover:underline focus-visible:outline-2 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.div(
            rx.icon(
                "calendar-days",
                class_name="h-7 w-7 stroke-[1.3] text-[#E8008A]",
                aria_hidden=True,
            ),
            rx.el.h3(
                "Your visit starts with a conversation.",
                class_name="mt-5 font-['Cormorant_Garamond'] text-[34px] font-medium leading-tight text-[#0F0F0F]",
            ),
            rx.el.p(
                "Tap to start a WhatsApp conversation with Taniz to arrange a spa appointment. Share your preferred treatment and date, and confirm current treatment details and availability with the team.",
                class_name="mt-4 text-sm leading-6 text-[#645B57]",
            ),
            rx.el.p(
                "Please arrive 10 minutes early and let Taniz know about any allergies or health conditions. Confirm cancellation and rescheduling terms directly with Taniz when arranging your appointment.",
                class_name="mt-4 text-sm leading-6 text-[#645B57]",
            ),
            rx.el.div(booking_link("Book via WhatsApp"), class_name="mt-7"),
            class_name="rounded-sm border border-[#0F0F0F]/10 bg-white p-7 sm:p-9",
        ),
        class_name="grid items-center gap-10 border-t border-[#0F0F0F]/10 py-16 md:grid-cols-2 lg:gap-20 sm:py-20",
    )


def experience_page() -> rx.Component:
    return site_layout(
        rx.el.div(
            experience_intro(),
            spa_gallery(),
            experience_story(),
            class_name="mx-auto w-full max-w-[1280px] px-5 sm:px-8 lg:px-12",
        ),
        active_page="experience",
    )
