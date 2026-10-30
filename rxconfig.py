import reflex as rx

config = rx.Config(
    app_name="copy_of_taniz_beauty_and_spa",
    default_color_mode="light",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
