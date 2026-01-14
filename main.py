import flet as ft

def main(page: ft.Page):
    page.title = "الرئيسية"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.WHITE
    page.padding = 0

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    PRIMARY = "#5E4B87"

    # ---------------- App Bar ----------------
    app_bar = ft.Container(
        bgcolor=PRIMARY,
        padding=ft.padding.symmetric(horizontal=16, vertical=10),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.CircleAvatar(
                    content=ft.Icon(ft.icons.PERSON, color=PRIMARY),
                    bgcolor=ft.colors.WHITE,
                ),
                ft.Text(
                    "الرصيد المتاح",
                    color=ft.colors.WHITE,
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    expand=True,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.Stack(
                            controls=[
                                ft.Icon(ft.icons.NOTIFICATIONS_NONE, color=ft.colors.WHITE),
                                ft.Container(
                                    content=ft.Text("4", size=10, color=ft.colors.WHITE),
                                    bgcolor=ft.colors.RED,
                                    width=16,
                                    height=16,
                                    border_radius=8,
                                    alignment=ft.alignment.center,
                                    right=0,
                                    top=0,
                                )
                            ]
                        ),
                        ft.Icon(ft.icons.MENU, color=ft.colors.WHITE),
                    ]
                )
            ]
        )
    )

    # ---------------- Balance Card ----------------
    balance_card = ft.Container(
        bgcolor=PRIMARY,
        border_radius=16,
        padding=20,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.VISIBILITY_OFF, color=ft.colors.WHITE),
                ft.Text("*****", size=26, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.Icon(ft.icons.ACCOUNT_BALANCE_WALLET, color=ft.colors.WHITE),
            ]
        )
    )

    # ---------------- Quick Action ----------------
    def quick_action(icon, label):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=30,
                    height=30,
                    border_radius=12,
                    bgcolor=ft.colors.GREY_100,
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon, color=PRIMARY),
                ),
                ft.Text(label, size=12),
            ]
        )

    quick_bar = ft.Container(
        bgcolor=ft.colors.WHITE,
        border_radius=20,
        padding=12,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.GREY_300),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            controls=[
                quick_action(ft.icons.ADD, "اختر"),
                quick_action(ft.icons.ADD, "اختر"),
                quick_action(ft.icons.ADD, "اختر"),
                quick_action(ft.icons.LANGUAGE, "الويب"),
                quick_action(ft.icons.SWAP_HORIZ, "التحويل"),
            ]
        )
    )

    # ---------------- Services ----------------
    def service(icon, label, color):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=64,
                    height=64,
                    border_radius=16,
                    bgcolor=color,
                    alignment=ft.alignment.center,
                    content=ft.Icon(icon, size=32),
                ),
                ft.Text(label, size=13),
            ]
        )

    services = ft.GridView(
        max_extent=100,
        child_aspect_ratio=0.9,
        spacing=12,
        run_spacing=20,
        controls=[
            service(ft.icons.GAMES, "معرض الألعاب", "#E3F2FD"),
            service(ft.icons.APPS, "البرامج", "#E8F5E9"),
            service(ft.icons.WIFI, "كبينه WIFI", "#FFF3E0"),
            service(ft.icons.CREDIT_CARD, "كبينه السداد", "#EFEBE9"),
            service(ft.icons.HEADSET_MIC, "الدعم الفني", "#ECEFF1"),
            service(ft.icons.CALCULATE, "الدفتر المحاسبي", "#F3E5F5"),
            service(ft.icons.SETTINGS, "إدارة العملاء", "#FFFDE7"),
            service(ft.icons.ACCOUNT_BALANCE_WALLET, "غذي حسابك", "#E3F2FD"),
        ]
    )

    banner = ft.Container(height=180, border_radius=16, bgcolor="#6A8C95")

    bottom_nav = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.MORE_HORIZ, label="المزيد"),
            ft.NavigationBarDestination(icon=ft.icons.BAR_CHART, label="التقارير"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="حسابي"),
            ft.NavigationBarDestination(icon=ft.icons.APPS, label="الخدمات"),
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="الرئيسية"),
        ],
        selected_index=4,
        bgcolor=ft.colors.WHITE,
    )

    page.add(
        ft.SafeArea(
            ft.Column(
                expand=True,
                controls=[
                    app_bar,
                    ft.ListView(
                        expand=True,
                        padding=16,
                        controls=[
                            balance_card,
                            ft.Container(height=20),
                            quick_bar,
                            ft.Container(height=30),
                            ft.Text("الخدمات الأساسية", size=18, weight=ft.FontWeight.BOLD),
                            ft.Container(height=16),
                            services,
                            ft.Container(height=30),
                            banner,
                        ]
                    ),
                    bottom_nav,
                ]
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
