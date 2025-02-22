import flet as ft
import pyrebase

# Configuración de Firebase
firebaseConfig = {
    'apiKey': "AIzaSyC_GLuiC7AWd6iEy3NW6f1GsATvI3ylovA",
    'authDomain': "libreria-18fbd.firebaseapp.com",
    'projectId': "libreria-18fbd",
    'storageBucket': "libreria-18fbd.firebasestorage.app",
    'databaseURL': "https://libreria-18fbd-default.firebaseio.com",
    'messagingSenderId': "649375944859",
    'appId': "1:649375944859:web:5e9594006bef4c9261b63e",
    'measurementId': "G-2RHHZDG91F"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Clase para poder ver el libro en la clase principal
class ProductPage(ft.View):
    def __init__(self, page, img_src, title, sub_title, rating):
        super().__init__(
            bgcolor="#BE5A38",
        )

        self.page = page
        self.img_src = img_src
        self.title = title
        self.sub_title = sub_title
        self.rating = rating

        # Colores
        self.color_book = "#ECB390"
        self.bg_color = "#F5EEDC"
        self.nav_color = "#C0D8C0"
        self.container_color = "#C0D8C0"

        self.build_view()

    def build_view(self):
        self.controls.append(
            ft.Container(
                alignment=ft.alignment.center,
                bgcolor=self.bg_color,
                margin=10,
                expand=True,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        ft.Stack(
                            expand=8,
                            controls=[
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    border_radius=20,
                                    content=ft.Image(src=f"assets/{self.img_src}.png", fit=ft.ImageFit.COVER,
                                                     width=450, height=720,),
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Container(
                                            margin=10,
                                            on_click=self.close_product_page,
                                            width=30, height=30, border_radius=10, bgcolor="black",
                                            content=ft.Icon(ft.Icons.KEYBOARD_ARROW_LEFT, color=self.color_book)
                                        ),
                                        ft.Container(
                                            margin=10,
                                            on_click=self.add_favorites,
                                            width=30, height=30, border_radius=10, bgcolor="black",
                                            content=ft.Icon(ft.Icons.FAVORITE, color=self.color_book)
                                        )

                                    ]
                                ),
                                ft.Container(
                                    bgcolor=ft.Colors.with_opacity(0.6, "white"),
                                    expand=True,
                                    padding=20,
                                    alignment=ft.alignment.center_left,
                                    margin=ft.margin.only(top=550),
                                    shadow=ft.BoxShadow(
                                        spread_radius=15, blur_radius=20,
                                        color=ft.Colors.with_opacity(0.3, "black"),
                                    ),
                                    content = ft.Column(
                                        spacing=2,
                                        controls=[
                                            ft.Text(self.title, size=30, weight="bold"),
                                            ft.Text(self.sub_title, size=20, weight="bold"),
                                            ft.Row([ft.Icon(ft.Icons.STAR, color=self.color_book)],
                                                   spacing=5)
                                        ],
                                    )
                                )

                            ]

                        )
                    ]
                )
            )
        )


    def close_product_page(self,e):
        self.page.views.pop()
        self.page.update()

    def add_favorites(self,e):
        self.page.views.pop()
        self.page.update()

# Clase para poder ver el libro en grande
class ProductBook(ft.Container):
    def __init__(self, page, img_src, title, sub_title, rating):
        super().__init__(
            alignment= ft.alignment.center,
            width=150,
            height=150,
            border_radius=10,
            bgcolor="#ECB390",
            padding=10,
            margin=ft.margin.only(top=10)
        )

        self.page = page
        self.img_src = img_src
        self.title = title
        self.sub_title = sub_title
        self.rating = rating

        # Colores
        self.color_book = "#DD4A48"
        self.bg_color = "#F5EEDC"
        self.nav_color = "#C0D8C0"
        self.container_color = "#C0D8C0"

        self.content = ft.Column(expand=True,
            spacing=0,
            controls=[
                ft.Stack(controls=[
                    ft.Container(border_radius=10,
                                 on_click=self.show_container,
                                 content=ft.Image(src=f"assets/{self.img_src}.png", width=250,
                                                  fit=ft.ImageFit.CONTAIN, height=200)
                                 ),
                    ft.Container(
                        width=60,
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.only(top_left=10, bottom_right=10),
                        bgcolor=ft.Colors.with_opacity(0.6, "white"),
                        content=ft.Row(
                            spacing=5,
                            controls=[
                            ft.Icon(ft.Icons.STAR, color=self.color_book),
                            ft.Text(f"{self.rating}", weight="bold")
                        ])
                    )
                ]),
                ft.Text(value=self.title, weight="bold"),
                ft.Text(value=self.sub_title, color="#BE5A38"),
                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                       controls=[
                           ft.Container(content=ft.Icon(ft.Icons.ADD, color="white"),
                                        bgcolor=self.color_book,
                                        width=30,
                                        height=30,
                                        border_radius=10,
                                        on_click=self.add_favorites,
                                        )
                       ])
            ])

    def show_container(self, e):
        product_view = ProductPage(self.page, self.img_src, self.title, self.sub_title, self.rating)
        self.page.views.append(product_view)
        self.page.update()

    def add_favorites(self,e):
        pass

# Clase principal
class AppLibreria(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page

        # Establecer el tamaño de la ventana
        self.page.window.width = 450
        self.page.window.height = 800
        self.page.window.resizable = False  # Permitir redimensionar la ventana

        # Colores
        self.color_book = "#DD4A48"
        self.bg_color = "#F5EEDC"
        self.nav_color = "#AAC8A7"
        self.container_color = "#AAC8A7"

        self.page.spacing = 5
        self.page.padding = 5
        self.page.bg_color = self.bg_color
        self.page.fonts = {"Playfair Display": "fonts/PlayfairDisplay-Italic-VariableFont_wght.ttf"}
        self.page.theme = ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thumb_color=self.container_color), font_family="Playfair Display")

        self.products=[
            ProductBook(self.page, "acomaf", "Una corte de Niebla y Furia", "Sarah J.Maas", "4.9"),
            ProductBook(self.page, "euvucr", "Eráse una vez un corazón roto", "Stephanie Garber", "4.5"),
            ProductBook(self.page, "crue", "El príncipe cruel", "Holly Black", "4.5"),
            ProductBook(self.page, "caraval", "Caraval", "Stephanie Garber", "4.0"),
        ]

        self.grid_view = ft.GridView(
            runs_count=2,
            child_aspect_ratio=0.6,
            controls= self.products
        )

        self.container_1 = ft.Container(expand=True,
                                        padding=10,
                                        offset = ft.transform.Offset(0,0),
                                        content = ft.Column(expand=True,
                                                            controls=[
                                                                ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                       controls=[
                                                                           ft.IconButton(icon=ft.Icons.MENU, icon_color="white"),
                                                                           ft.Container(ft.Image(src="assets/icono.jpg", height=30, ), border_radius=5)
                                                                       ]),

                                                            ft.Text("Libros pendientes", size=25, weight="bold"),

                                                            ft.TextField(prefix_icon=ft.Icons.SEARCH, hint_text="Buscador", border_radius=10,
                                                                         bgcolor=self.container_color, border_color="transparent",
                                                                         on_change=self.filtrar_libros),

                                                            ft.Container(expand=True,
                                                                content=ft.Tabs(
                                                                    selected_index=0,
                                                                    expand=True,
                                                                    indicator_color="transparent",
                                                                    label_color=self.color_book,

                                                                    # Géneros de los libros
                                                                    tabs=[
                                                                        ft.Tab(
                                                                            text="Fantasía",
                                                                            content=self.grid_view
                                                                        ),
                                                                        ft.Tab(
                                                                            text="Terror/Thriller",
                                                                            content=ft.GridView(
                                                                                runs_count=2,
                                                                                child_aspect_ratio=0.6,
                                                                                controls=[
                                                                                    ProductBook(self.page, "acomaf",
                                                                                                "Una corte de Niebla y Furia",
                                                                                                "Sarah J.Maas", "4.9"),
                                                                                    ProductBook(self.page, "euvucr",
                                                                                                "Eráse una vez un corazón roto",
                                                                                                "Stephanie Garber",
                                                                                                "4.5"),
                                                                                    ProductBook(self.page, "crue",
                                                                                                "El príncipe cruel",
                                                                                                "Holly Black", "4.5"),

                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Tab(
                                                                            text="Romance",
                                                                            content=ft.GridView(
                                                                                runs_count=2,
                                                                                child_aspect_ratio=0.6,
                                                                                controls=[
                                                                                    ProductBook(self.page, "acomaf",
                                                                                                "Una corte de Niebla y Furia",
                                                                                                "Sarah J.Maas", "4.9"),
                                                                                    ProductBook(self.page, "euvucr",
                                                                                                "Eráse una vez un corazón roto",
                                                                                                "Stephanie Garber",
                                                                                                "4.5"),
                                                                                    ProductBook(self.page, "crue",
                                                                                                "El príncipe cruel",
                                                                                                "Holly Black", "4.5"),

                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Tab(
                                                                            text="Histórico",
                                                                            content=ft.GridView(
                                                                                runs_count=2,
                                                                                child_aspect_ratio=0.6,
                                                                                controls=[
                                                                                    ProductBook(self.page, "acomaf",
                                                                                                "Una corte de Niebla y Furia",
                                                                                                "Sarah J.Maas", "4.9"),
                                                                                    ProductBook(self.page, "euvucr",
                                                                                                "Eráse una vez un corazón roto",
                                                                                                "Stephanie Garber",
                                                                                                "4.5"),
                                                                                    ProductBook(self.page, "crue",
                                                                                                "El príncipe cruel",
                                                                                                "Holly Black", "4.5"),

                                                                                ]
                                                                            )
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                            ])
                                        )

        # Libros que no han gustado
        self.container_2 = ft.Container(expand=True,
                    offset = ft.transform.Offset(-2,0),
                    content = ft.Column(expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text("¡Libros que fueron 1 estrellas!", size=20),
                                            ft.Container(alignment=ft.alignment.center,
                                                         content=ft.Image(src="assets/estrella.png",
                                                                          fit=ft.ImageFit.CONTAIN, width=150),),
                                            ft.Container(expand=True,
                                                         content=ft.Tabs(
                                                             selected_index=0,
                                                             expand=True,
                                                             indicator_color="transparent",
                                                             label_color=self.color_book,

                                                             tabs=[
                                                                 ft.Tab(
                                                                     content=ft.GridView(
                                                                         runs_count=2,
                                                                         child_aspect_ratio=0.6,
                                                                         controls=[
                                                                             ProductBook(self.page, "after",
                                                                                         "After",
                                                                                         "Anna Tod", "0.5"),
                                                                             ProductBook(self.page, "seis_signos",
                                                                                         "Los seis signos de la luz",
                                                                                         "Susan Cooper",
                                                                                         "2.0"),
                                                                             ProductBook(self.page, "chocolate",
                                                                                         "Como agua para chocolate",
                                                                                         "Laura Esquivel", "1.5"),

                                                                         ]
                                                                     )
                                                                 ),
                                                             ]
                                                         )
                                                         )
                                        ])

                                        )

        # Libros que te han gustado
        self.container_3 = ft.Container(expand=True,
                                        offset=ft.transform.Offset(-2, 0),
                                        content=ft.Column(expand=True,
                                                          alignment=ft.MainAxisAlignment.CENTER,
                                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                          controls=[
                                                              ft.Text("¡Libros que fueron 5 estrellas!", size=20),
                                                              ft.Container(alignment=ft.alignment.center,
                                                                           content=ft.Image(src="assets/estrella5.png",
                                                                                            fit=ft.ImageFit.CONTAIN,
                                                                                            width=150), ),
                                                              ft.Container(expand=True,
                                                                           content=ft.Tabs(
                                                                               selected_index=0,
                                                                               expand=True,
                                                                               indicator_color="transparent",
                                                                               label_color=self.color_book,

                                                                               tabs=[
                                                                                   ft.Tab(
                                                                                       content=ft.GridView(
                                                                                           runs_count=2,
                                                                                           child_aspect_ratio=0.6,
                                                                                           controls=[
                                                                                               ProductBook(self.page,
                                                                                                           "acomaf",
                                                                                                           "Una corte de Niebla y Furia",
                                                                                                           "Sarah J.Maas",
                                                                                                           "5"),
                                                                                               ProductBook(self.page,
                                                                                                           "amor_verdadero",
                                                                                                           "La maldición del amor verdadero",
                                                                                                           "Stephanie Garber",
                                                                                                           "5"),
                                                                                               ProductBook(self.page,
                                                                                                           "roja",
                                                                                                           "Reina Roja",
                                                                                                           "Juan Gómez-Jurado",
                                                                                                           "5")
                                                                                           ]
                                                                                       )
                                                                                   ),
                                                                               ]
                                                                           )
                                                                           )
                                                          ])
                                        )

        # Libros que estoy leyendo ahora
        self.container_4 = ft.Container(expand=True,
                                        offset=ft.transform.Offset(-2, 0),
                                        content=ft.Column(expand=True,
                                                          alignment=ft.MainAxisAlignment.CENTER,
                                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                          controls=[
                                                              ft.Text("Libros que estás leyendo ahora", size=20),
                                                              ft.Container(alignment=ft.alignment.center,
                                                                           content=ft.Image(src="assets/librosinFondo.png",
                                                                                            fit=ft.ImageFit.CONTAIN,
                                                                                            width=120), ),
                                                              ft.Container(expand=True,
                                                                           content=ft.Tabs(
                                                                               selected_index=0,
                                                                               expand=True,
                                                                               indicator_color="transparent",
                                                                               label_color=self.color_book,

                                                                               tabs=[
                                                                                   ft.Tab(
                                                                                       content=ft.GridView(
                                                                                           runs_count=2,
                                                                                           child_aspect_ratio=0.6,
                                                                                           controls=[
                                                                                               ProductBook(self.page,
                                                                                                           "alas",
                                                                                                           "Una corte de Alas y Ruina",
                                                                                                           "Sarah J.Maas",
                                                                                                           "¿?"),
                                                                                               ProductBook(self.page,
                                                                                                           "brujas",
                                                                                                           "La sociedad secreta de las brujas rebeldes",
                                                                                                           "Sangu Mandanna",
                                                                                                           "¿?"),
                                                                                           ]
                                                                                       )
                                                                                   ),
                                                                               ]
                                                                           )
                                                                           )
                                                          ])
                                        )

        self.selected = ft.Container(
            shape=ft.BoxShape.CIRCLE,
            offset = ft.transform.Offset(-0.375, 0.66),
            bgcolor=self.nav_color,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=10),
            height=10,
            content=ft.Icon(ft.Icons.HOME_FILLED, color=self.color_book),
        )

        self.nav = ft.Container(
            bgcolor=self.nav_color,
            alignment=ft.alignment.center,
            border_radius=10,
            padding=0,
            height=50,
            margin=ft.margin.only(top=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    #En función de cuantas pestañas tengamos
                    ft.IconButton(icon=ft.Icons.HOME_FILLED, data="1", icon_color="white", on_click=self.change_position),
                    ft.IconButton(icon=ft.Icons.BOOK_ONLINE_OUTLINED, data="2", icon_color="white", on_click=self.change_position),
                    ft.IconButton(icon=ft.Icons.BOOK, data="3", icon_color="white", on_click=self.change_position),
                    ft.IconButton(icon=ft.Icons.FAVORITE, data="4", icon_color="white", on_click=self.change_position),

                ]
            )
        )

        self.page.add(
            ft.Column(expand=True,
                      controls=[
                          ft.Stack(
                              expand=True,
                              controls=[
                                  self.container_1,
                                  self.container_2,
                                  self.container_3,
                                  self.container_4,
                              ]
                          ),
                          ft.Stack(
                              height=60,
                              controls=[
                                  self.nav,
                                  self.selected
                              ]
                          ),
                      ])
        )

    def filtrar_libros(self, e):
        search_text = e.control.value.lower()
        filteredProducts = [
            product for product in self.products if search_text in product.title.lower() or product.sub_title.lower()
        ]

        self.grid_view.controls = filteredProducts
        self.grid_view.update()

    def change_position(self, e):
        if e.control.data == "1":
            self.selected.offset = ft.transform.Offset(-0.375, 0.66)
            self.selected.content = ft.Icon(name=ft.Icons.HOME_FILLED, color=self.color_book)
            self.container_1.offset = ft.transform.Offset(0, 0)
            self.container_2.offset = ft.transform.Offset(-2, 0)
            self.container_3.offset = ft.transform.Offset(-2, 0)
            self.container_4.offset = ft.transform.Offset(-2, 0)
        if e.control.data == "2":
            self.selected.offset = ft.transform.Offset(-0.125, 0.66)
            self.selected.content = ft.Icon(name=ft.Icons.BOOK_ONLINE_OUTLINED, color=self.color_book)
            self.container_1.offset = ft.transform.Offset(-2, 0)
            self.container_2.offset = ft.transform.Offset(0, 0)
            self.container_3.offset = ft.transform.Offset(-2, 0)
            self.container_4.offset = ft.transform.Offset(-2, 0)
        if e.control.data == "3":
            self.selected.offset = ft.transform.Offset(0.125, 0.66)
            self.selected.content = ft.Icon(name=ft.Icons.BOOK, color=self.color_book)
            self.container_1.offset = ft.transform.Offset(-2, 0)
            self.container_2.offset = ft.transform.Offset(-2, 0)
            self.container_3.offset = ft.transform.Offset(0, 0)
            self.container_4.offset = ft.transform.Offset(-2, 0)
        if e.control.data == "4":
            self.selected.offset = ft.transform.Offset(0.375, 0.66)
            self.selected.content = ft.Icon(name=ft.Icons.FAVORITE, color=self.color_book)
            self.container_1.offset = ft.transform.Offset(-2, 0)
            self.container_2.offset = ft.transform.Offset(-2, 0)
            self.container_3.offset = ft.transform.Offset(-2, 0)
            self.container_4.offset = ft.transform.Offset(0, 0)

        self.page.update()

# Página que sirve para que el usuario se registre
class regisPage(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        # Configuración de la ventana
        page.window.width = 450  # Ancho de la ventana
        page.window.height = 800  # Alto de la ventana
        page.window.resizable = False  # Permitir redimensionar la ventana
        page.bgcolor = "#C0D8C0"

        page.theme_mode =ft.ThemeMode.LIGHT
        page.vertical_alignment = "center"
        page.horizontal_alignment = "center"

        # SnackBar inicializado con contenido predeterminado
        snack_bar = ft.SnackBar(content=ft.Text(""))

        # Función de registrar usuario
        def btn_regis(e):
            try:
                auth.create_user_with_email_and_password(usuario.value, contra.value)
                usuario.value = ""
                contra.value = ""
                snack_bar.content = ft.Text("Registro Exitoso", color="white")
                snack_bar.bgcolor = "green"
                snack_bar.open = True

            except:
                snack_bar.content = ft.Text("Registro no Exitoso", color="white")
                snack_bar.bgcolor = "red"
                snack_bar.open = True

            page.update()

        def btn_login(e):
            page.clean()
            main(page)

        usuario = ft.TextField(
            label="Usuario",
            border_color="#DD4A48",
            color="#DD4A48",
            width=400,
        )

        # Elementos de la UI
        texto_registrar = ft.Text(
            value="¿Eres nuevo? ¡Registrate ahora!",
            size=40,
            weight="bold",
            color="#DD4A48",
        )

        texto_contra = ft.Text(
            value="La contraseña tiene que tener un mínimo de 6 carácteres",
            size=12,
            weight="bold",
            color="#DD4A48",
        )

        contra = ft.TextField(
            label="Contraseña",
            border_color="#DD4A48",
            color="#DD4A48",
            password=True,
            can_reveal_password=True,
            width=400,
        )

        boton_regis = ft.ElevatedButton(
            text="Registrar cuenta",
            color="#F5EEDC",
            bgcolor="#DD4A48",
            on_click=btn_regis,
            width=200,
        )

        boton_login = ft.ElevatedButton(
            text="Volver a iniciar sesión",
            color="#F5EEDC",
            bgcolor="#DD4A48",
            on_click=btn_login,
            width=200,
        )


        # Agregar elementos a la página
        page.overlay.append(snack_bar)
        page.add(
            texto_registrar,
            usuario,
            texto_contra,
            contra,
            boton_regis,
            boton_login,
        )

# El main donde se llama a la appLibreria y donde se loguea el usuario y entra a la app directo
def main(page: ft.Page):

    # Configuración de la ventana
    page.window.width = 450
    page.window.height = 800
    page.window.resizable = False  # Permitir redimensionar la ventana
    page.bgcolor = "#C0D8C0"

    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Función de login
    def btn_login(e):
        try:
            auth.sign_in_with_email_and_password(usuario.value, contra.value)
            usuario.value = ""
            contra.value = ""
            page.clean()

            app_libreria = AppLibreria(page)
            page.add(app_libreria)

        except:
            snack_bar.content = ft.Text("Inicio de sesión no exitoso", color="white")
            snack_bar.bgcolor = "red"
            snack_bar.open = True
            usuario.value = ""
            contra.value = ""

        page.update()

    def btn_regis(e):
        page.clean()
        regis = regisPage(page)
        page.add(regis)

    # Elementos de la UI
    texto_login = ft.Text(
        value="Iniciar Sesión",
        size=40,
        weight="bold",
        color="#DD4A48",
    )

    usuario = ft.TextField(
        hint_text="Usuario",
        label="Usuario",
        border_color="#DD4A48",
        color="#DD4A48",
        width=400,
    )

    contra = ft.TextField(
        hint_text="Contraseña",
        label="Contraseña",
        border_color="#DD4A48",
        color="#DD4A48",
        password=True,
        can_reveal_password=True,
        width=400,
    )

    boton_login = ft.ElevatedButton(
        text="Iniciar Sesión",
        color="#F5EEDC",
        bgcolor="#DD4A48",
        on_click=btn_login,
        width=200,
    )

    boton_regis = ft.ElevatedButton(
        text="Registrate aquí",
        color="#F5EEDC",
        bgcolor="#DD4A48",
        on_click=btn_regis,
        width=200,
    )

    # SnackBar inicializado con contenido predeterminado
    snack_bar = ft.SnackBar(content=ft.Text(""))

    # Agregar elementos a la página
    page.overlay.append(snack_bar)
    page.add(
        texto_login,
        usuario,
        contra,
        boton_login,
        boton_regis
    )

# Ejecuta la app y el assets_dir es para que entre en la carpeta "assets"
ft.app(target=main, assets_dir="assets")