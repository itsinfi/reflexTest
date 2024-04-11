from rxconfig import config
import reflex as rx


class IndexState(rx.State):

    """Button Farbe und Text ändern und Image flippen"""
    isButton1: bool = True
    flipImage: bool = False
    
    def stateTest1(self):
        self.isButton1 = not self.isButton1
        self.flipImage = not self.flipImage



    """Opacity mit Mouse movement ändern"""
    percent: float = 100

    def stateTest2(self, isPositiveChange: bool):
        if isPositiveChange:
            self.percent += 1
        else:
            self.percent -= 100
        
        if self.percent < 0:
            self.percent = 0
        
        if self.percent > 100:
            self.percent = 100
        



def index() -> rx.Component:
    return  rx.container(
                rx.center(
                    rx.vstack(
                        rx.image(
                            src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F001%2F105%2F389%2Fnon_2x%2Fwireframe-landscape-banner-design-vector.jpg&f=1&nofb=1&ipt=9ad5dcdd927b90069c7c272e9dba352aa9d53e9d0a434efa3d0eb793f7b79ab5&ipo=images',
                            width='100%',
                            height='500px',
                            objectFit='cover',
                            borderRadius='30px',
                            transform=rx.cond(IndexState.flipImage, 'scaleY(-1)', '')
                        ),
                        rx.text(
                            'Are you enjoying this beautiful 80s scenery?',
                            size='8',
                            weight='bold',
                            paddingBottom="1rem",
                            paddingTop="2rem",
                        ),
                        rx.html(
                            '<p style="font-style:italic;text-align:center;">\'Our beautiful wallpaper design encaptures vigilance combined with magnificence.\'<br>~Donald J. Trump, Founder of \'Make America Great Again\' (2023)</p>'
                        ),
                        rx.button(
                            rx.cond(IndexState.isButton1, 'Buy', 'Sell'),
                            size='4',
                            marginTop="2rem",
                            color=rx.cond(IndexState.isButton1, 'white', 'black'),
                            backgroundColor=rx.cond(IndexState.isButton1, 'indigo', 'yellow'),
                            on_click=IndexState.stateTest1(),
                        ),
                        align='center',
                    ),
                ),
                size='4',
                backgroundImage='linear-gradient(#272727, #111111)',
                opacity=f"{IndexState.percent}%",
                borderRadius='30px',
                boxShadow='2px 2px 5px #00000055',
                margin='50px',
                padding='50px',
                on_mouse_leave=IndexState.stateTest2(False),
                on_mouse_move=IndexState.stateTest2(True),
            ),

app = rx.App(
    theme=rx.theme(
        # theme_panel=rx.theme_panel(),
        appearance="dark",
        accentColor="yellow",
        grayColor="mauve",
        radius="full",
        scaling="110%",
        panel_background='translucent',
    )
)
app.add_page(index)