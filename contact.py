import reflex as rx

from copy_of_taniz_beauty_and_spa.states.contact_enquiry_state import ContactEnquiryState
from copy_of_taniz_beauty_and_spa.components.homepage import (
    ADDRESS,
    DIRECTIONS_URL,
    WHATSAPP_URL,
    booking_link,
    section_label,
)
from copy_of_taniz_beauty_and_spa.components.layout import site_layout

MAP_URL = "https://www.google.com/maps?q=House%2019%20Kwara%20Drive%2C%203rd%20Avenue%2C%20War%20College%20Estate%2C%20Gwarinpa%2C%20Abuja%2C%20Nigeria&output=embed"


def contact_method(
    icon: str, title: str, detail: str, description: str, href: str
) -> rx.Component:
    return rx.el.article(
        rx.icon(
            icon,
            class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
            aria_hidden=True,
        ),
        rx.el.h2(
            title,
            class_name="mt-6 font-['Cormorant_Garamond'] text-[32px] font-medium text-[#0F0F0F]",
        ),
        rx.el.p(
            description, class_name="mt-2 text-sm leading-6 text-[#645B57]"
        ),
        rx.el.a(
            detail,
            rx.icon(
                "arrow-up-right",
                class_name="h-4 w-4 shrink-0",
                aria_hidden=True,
            ),
            href=href,
            class_name="mt-5 inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A] [&]:break-all",
        ),
        class_name="min-w-0 rounded-sm border border-[#0F0F0F]/10 bg-white p-6 sm:p-8",
    )


def contact_intro() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_label("Visit Taniz · Gwarinpa, Abuja"),
            rx.el.h1(
                "Make room for",
                rx.el.br(),
                rx.el.em(
                    "your next pause.", class_name="font-normal text-[#E8008A]"
                ),
                class_name="mt-5 font-['Cormorant_Garamond'] text-[52px] font-medium leading-[1.04] tracking-[-0.025em] text-[#0F0F0F] sm:text-[72px] lg:text-[84px]",
            ),
        ),
        rx.el.div(
            rx.el.p(
                "Find us in War College Estate, Gwarinpa. Arrange a spa appointment via WhatsApp, or get in touch with Taniz to ask about your visit.",
                class_name="max-w-md text-base leading-7 text-[#645B57]",
            ),
            rx.el.div(booking_link("Book via WhatsApp"), class_name="mt-7"),
            rx.el.p(
                "Tap to start a WhatsApp conversation with Taniz to arrange a spa appointment and confirm availability.",
                class_name="mt-4 max-w-sm text-xs leading-5 text-[#645B57]",
            ),
        ),
        class_name="grid items-end gap-8 py-14 sm:py-20 lg:grid-cols-[1.4fr_1fr] lg:gap-14",
    )


def visit_details() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.icon(
                "map-pin",
                class_name="h-6 w-6 stroke-[1.3] text-[#E8008A]",
                aria_hidden=True,
            ),
            rx.el.h2(
                "Find your way to Taniz.",
                class_name="mt-5 font-['Cormorant_Garamond'] text-[38px] font-medium leading-tight text-[#0F0F0F] sm:text-[46px]",
            ),
            rx.el.address(
                ADDRESS,
                class_name="mt-5 max-w-md text-base not-italic leading-8 text-[#645B57]",
            ),
            rx.el.a(
                "Get driving directions",
                rx.icon(
                    "arrow-up-right",
                    class_name="h-4 w-4 shrink-0",
                    aria_hidden=True,
                ),
                rx.el.span(
                    "(opens in Google Maps in a new tab)", class_name="sr-only"
                ),
                href=DIRECTIONS_URL,
                target="_blank",
                rel="noopener noreferrer",
                class_name="mt-5 inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] underline decoration-[#E8008A]/30 underline-offset-4 hover:decoration-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "clock",
                    class_name="h-5 w-5 text-[#E8008A]",
                    aria_hidden=True,
                ),
                section_label("Opening hours"),
                class_name="flex items-center gap-3",
            ),
            rx.el.h2(
                "A little time for you.",
                class_name="mt-5 font-['Cormorant_Garamond'] text-[34px] font-medium leading-tight text-[#0F0F0F]",
            ),
            rx.el.dl(
                rx.el.div(
                    rx.el.dt("Monday–Saturday", class_name="text-[#645B57]"),
                    rx.el.dd("9:00 AM–6:00 PM", class_name="text-[#0F0F0F]"),
                    class_name="flex flex-wrap justify-between gap-3 border-b border-[#0F0F0F]/10 py-5",
                ),
                rx.el.div(
                    rx.el.dt("Sunday", class_name="text-[#645B57]"),
                    rx.el.dd("Closed", class_name="text-[#0F0F0F]"),
                    class_name="flex justify-between gap-3 py-5",
                ),
                class_name="mt-4 text-sm",
            ),
            rx.el.p(
                "All times are West Africa Time (WAT, UTC+1).",
                class_name="text-xs leading-5 text-[#645B57]",
            ),
            rx.el.p(
                "Hours published on Taniz’s live Setmore listing. Contact Taniz if you need to confirm arrangements for a particular date.",
                class_name="mt-3 text-xs leading-5 text-[#645B57]",
            ),
            class_name="rounded-sm border border-[#0F0F0F]/10 bg-white p-6 sm:p-9",
        ),
        aria_label="Spa address and opening hours",
        class_name="grid items-start gap-10 border-t border-[#0F0F0F]/10 py-14 md:grid-cols-2 lg:gap-20 sm:py-16",
    )


def visit_map() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                section_label("Your route to a little care"),
                rx.el.h2(
                    "Meet us in Gwarinpa.",
                    id="map-heading",
                    class_name="mt-3 font-['Cormorant_Garamond'] text-[40px] font-medium text-[#0F0F0F] sm:text-[50px]",
                ),
            ),
            rx.el.a(
                "Open directions in Google Maps",
                rx.icon(
                    "arrow-up-right",
                    class_name="h-4 w-4 shrink-0",
                    aria_hidden=True,
                ),
                href=DIRECTIONS_URL,
                target="_blank",
                rel="noopener noreferrer",
                aria_label="Open driving directions to Taniz in Google Maps (opens in a new tab)",
                class_name="inline-flex min-h-12 items-center gap-3 text-sm text-[#E8008A] hover:underline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
            ),
            class_name="mb-7 flex flex-col justify-between gap-4 md:flex-row md:items-end",
        ),
        rx.el.iframe(
            src=MAP_URL,
            title="Map showing Taniz Beauty & Spa at House 19 Kwara Drive, 3rd Avenue, War College Estate, Gwarinpa, Abuja, Nigeria",
            loading="eager",
            referrer_policy="strict-origin-when-cross-origin",
            allow_full_screen=True,
            class_name="h-[340px] w-full rounded-sm border border-[#0F0F0F]/10 bg-[#EDE5DE] sm:h-[460px]",
        ),
        rx.el.p(
            "Map provided by Google. If the embedded map does not load, use the directions link above.",
            class_name="mt-4 text-xs leading-5 text-[#645B57]",
        ),
        aria_labelledby="map-heading",
        class_name="border-t border-[#0F0F0F]/10 py-14 sm:py-16",
    )


def enquiry_form() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            section_label("A note to Taniz"),
            rx.el.h2(
                "How can we help?",
                class_name="mt-3 font-['Cormorant_Garamond'] text-[40px] font-medium leading-tight text-[#0F0F0F] sm:text-[50px]",
            ),
            rx.el.p(
                "Send a treatment or visit question and the team will reply by email.",
                class_name="mt-4 max-w-xl text-base leading-7 text-[#645B57]",
            ),
        ),
        rx.cond(
            ContactEnquiryState.email_form_connected,
            rx.fragment(),
            rx.el.p(
                "Email form not connected yet — use WhatsApp or email for now",
                role="status",
                class_name="mt-6 border border-[#E8008A]/30 bg-[#FDF9F7] px-4 py-3 text-sm leading-6 text-[#0F0F0F]",
            ),
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "Your name",
                        html_for="enquiry-name",
                        class_name="mb-2 block text-sm font-medium text-[#0F0F0F]",
                    ),
                    rx.el.input(
                        id="enquiry-name",
                        name="name",
                        type="text",
                        required=True,
                        min_length=2,
                        max_length=100,
                        auto_complete="name",
                        placeholder="Name",
                        class_name="min-h-12 w-full rounded-sm border border-[#0F0F0F]/20 bg-white px-4 text-sm text-[#0F0F0F] placeholder:text-[#645B57]/70 focus:border-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Email address",
                        html_for="enquiry-email",
                        class_name="mb-2 block text-sm font-medium text-[#0F0F0F]",
                    ),
                    rx.el.input(
                        id="enquiry-email",
                        name="email",
                        type="email",
                        required=True,
                        max_length=254,
                        auto_complete="email",
                        placeholder="you@example.com",
                        class_name="min-h-12 w-full rounded-sm border border-[#0F0F0F]/20 bg-white px-4 text-sm text-[#0F0F0F] placeholder:text-[#645B57]/70 focus:border-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "What is your enquiry about?",
                        html_for="enquiry-type",
                        class_name="mb-2 block text-sm font-medium text-[#0F0F0F]",
                    ),
                    rx.el.select(
                        rx.el.option(
                            "Choose an enquiry type",
                            value="",
                            disabled=True,
                        ),
                        rx.el.option("Treatment", value="treatment"),
                        rx.el.option("Visit", value="visit"),
                        id="enquiry-type",
                        name="enquiry_type",
                        required=True,
                        default_value="",
                        class_name="min-h-12 w-full appearance-none rounded-sm border border-[#0F0F0F]/20 bg-white px-4 text-sm text-[#0F0F0F] focus:border-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A]",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Your message",
                        html_for="enquiry-message",
                        class_name="mb-2 block text-sm font-medium text-[#0F0F0F]",
                    ),
                    rx.el.textarea(
                        id="enquiry-message",
                        name="message",
                        required=True,
                        min_length=10,
                        max_length=5000,
                        rows=6,
                        placeholder="Tell us a little about what you would like to know.",
                        class_name="w-full rounded-sm border border-[#0F0F0F]/20 bg-white px-4 py-3 text-sm leading-6 text-[#0F0F0F] placeholder:text-[#645B57]/70 focus:border-[#E8008A] focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#E8008A]",
                    ),
                ),
                class_name="mt-7 grid gap-5 md:grid-cols-2",
            ),
            rx.cond(
                ContactEnquiryState.feedback != "",
                rx.el.p(
                    ContactEnquiryState.feedback,
                    role="status",
                    aria_live="polite",
                    class_name=rx.cond(
                        ContactEnquiryState.send_succeeded,
                        "mt-5 border border-green-700/20 bg-green-50 px-4 py-3 text-sm leading-6 text-green-800",
                        "mt-5 border border-red-700/20 bg-red-50 px-4 py-3 text-sm leading-6 text-red-800",
                    ),
                ),
                rx.fragment(),
            ),
            rx.el.button(
                rx.cond(
                    ContactEnquiryState.is_sending,
                    "Sending your enquiry…",
                    "Send enquiry",
                ),
                type="submit",
                disabled=(
                    ContactEnquiryState.is_sending
                    | ~ContactEnquiryState.email_form_connected
                ),
                class_name="mt-6 inline-flex min-h-12 items-center justify-center rounded-full bg-[#E8008A] px-7 py-3 text-sm font-medium text-white transition-colors hover:bg-[#C90077] focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A] disabled:cursor-not-allowed disabled:bg-[#0F0F0F]/35",
            ),
            on_submit=ContactEnquiryState.submit_enquiry,
            class_name="mt-2",
        ),
        rx.el.p(
            "Your details are used only to respond to this enquiry and are not saved by this form.",
            class_name="mt-4 text-xs leading-5 text-[#645B57]",
        ),
        aria_label="Send a treatment or visit enquiry by email",
        class_name="border-t border-[#0F0F0F]/10 py-14 sm:py-16",
    )


def contact_page() -> rx.Component:
    return site_layout(
        rx.el.div(
            contact_intro(),
            rx.el.section(
                rx.el.div(
                    contact_method(
                        "phone",
                        "Give us a call.",
                        "+234 903 789 7510",
                        "Speak with Taniz about treatments or planning your visit.",
                        "tel:+2349037897510",
                    ),
                    contact_method(
                        "message-circle",
                        "Send a WhatsApp.",
                        "+234 901 282 4009",
                        "Start a conversation with a visit enquiry already filled in.",
                        WHATSAPP_URL,
                    ),
                    contact_method(
                        "mail",
                        "Drop us a note.",
                        "tanizbeautyandspa986@gmail.com",
                        "Prefer email? Send your questions directly to the spa.",
                        "mailto:tanizbeautyandspa986@gmail.com",
                    ),
                    class_name="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-3",
                ),
                aria_label="Contact Taniz by phone, WhatsApp or email",
                class_name="pb-14 sm:pb-16",
            ),
            enquiry_form(),
            visit_details(),
            visit_map(),
            rx.el.section(
                rx.el.div(
                    section_label("Your visit starts here"),
                    rx.el.h2(
                        "Choose your kind of care.",
                        class_name="mt-4 font-['Cormorant_Garamond'] text-[40px] font-medium leading-tight text-[#0F0F0F] sm:text-[50px]",
                    ),
                    rx.el.p(
                        "Browse the treatment menu, then tap to start a WhatsApp conversation with Taniz to arrange your spa appointment and confirm availability.",
                        class_name="mt-4 max-w-xl text-base leading-7 text-[#645B57]",
                    ),
                ),
                rx.el.div(
                    booking_link("Book an appointment"),
                    rx.el.a(
                        "Explore treatments & prices",
                        rx.icon(
                            "arrow-right",
                            class_name="h-4 w-4",
                            aria_hidden=True,
                        ),
                        href="/treatments",
                        class_name="inline-flex min-h-12 items-center gap-3 text-sm text-[#0F0F0F] hover:text-[#E8008A] focus-visible:outline-2 focus-visible:outline-[#E8008A]",
                    ),
                    class_name="flex flex-col items-start gap-3",
                ),
                class_name="flex flex-col justify-between gap-8 border-t border-[#0F0F0F]/10 py-16 lg:flex-row lg:items-center sm:py-20",
            ),
            class_name="mx-auto w-full max-w-[1280px] px-5 sm:px-8 lg:px-12",
        ),
        active_page="contact",
    )
