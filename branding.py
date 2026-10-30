import reflex as rx


def draft_logo() -> rx.Component:
    return rx.el.a(
        rx.el.img(
            src="/taniz-logo.jpg",
            alt="Taniz Beauty & Spa logo",
            class_name="h-16 w-24 object-contain sm:h-20 sm:w-28",
        ),
        href="/",
        aria_label="Taniz Beauty & Spa home",
        class_name="inline-flex shrink-0 flex-col items-center justify-center rounded-sm bg-white px-2 py-1 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[#E8008A]",
    )
