import reflex as rx

from copy_of_taniz_beauty_and_spa.components.homepage import footer, header


def site_layout(
    content: rx.Component, active_page: str = "home"
) -> rx.Component:
    return rx.el.div(
        rx.el.a(
            "Skip to content",
            href="#main-content",
            class_name="sr-only z-50 rounded-full bg-[#0F0F0F] px-5 py-3 text-white focus:not-sr-only focus:fixed focus:left-4 focus:top-4",
        ),
        header(active_page),
        rx.el.main(content, id="main-content"),
        footer(),
        id="home",
        class_name="min-h-screen w-full bg-[#FDF9F7] font-['Outfit'] text-[#0F0F0F] selection:bg-[#E8008A]/15",
    )
