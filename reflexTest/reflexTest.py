from reflexTest.utils import u
from reflexTest.prompting import p

from rxconfig import config
import reflex as rx
import asyncio



#TODO: performance erhöhen (laggt manchmal extrem)
class Clock(rx.State):
    """Clock"""

    hasStarted: bool = False
    value: int = 0
    
    @rx.background
    async def runClock(self):
        while True:
            async with self:
                if not self.hasStarted:
                    return
                await asyncio.sleep(1)
                self.value += 1
    
    """Stoppuhr"""
    def toggleClock(self):
        self.hasStarted = not self.hasStarted
        if self.hasStarted:
            self.value = 0
            return Clock.runClock()



class IndexState(rx.State):

    """Button Farbe und Text ändern und Image flippen"""
    isButton1: bool = True
    flipImage: bool = False
    
    def stateTest1(self):
        self.isButton1 = not self.isButton1
        self.flipImage = not self.flipImage



    """Opacity mit Mouse movement ändern"""
    percent: float = 100

    def updateOpacity(self, isPositiveChange: bool):
        # if isPositiveChange:
        #     self.percent += 1
        # else:
        #     self.percent -= 100
        
        if self.percent < 0:
            self.percent = 0
        
        if self.percent > 100:
            self.percent = 100




"""Index Page"""

def index() -> rx.Component:
    return  rx.vstack(
                u.Card(
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
                        color=rx.cond(IndexState.isButton1, u.primaryTextColor, u.secondaryTextColor),
                        backgroundColor=rx.cond(IndexState.isButton1, u.primaryBackgroundColor, u.secondaryBackgroundColor),
                        on_click=IndexState.stateTest1,
                    ),
                    marginTop='50px'
                ),
                u.Card(
                    rx.heading(
                        f"{Clock.value}s",
                        size='9',
                        marginBottom='2rem',
                    ),
                    rx.cond(
                        Clock.hasStarted,
                        rx.button(
                        'Stop',
                        size = '3',
                        backgroundColor=u.secondaryBackgroundColor,
                        color=u.secondaryTextColor,
                        on_click=Clock.toggleClock,
                        ),
                        rx.button(
                        'Start',
                        size = '3',
                        backgroundColor=u.primaryBackgroundColor,
                        color=u.primaryTextColor,
                        on_click=Clock.toggleClock,
                        ),
                    ),
                ),
                u.Card(
                    rx.text(
                        'Do you wanna start a \'bit of prompting?',
                        size='8',
                        weight='bold',
                        paddingBottom="1rem",
                        paddingTop="2rem",
                    ),
                    rx.link(
                        rx.button(
                            'Start prompting',
                            size='4',
                            marginTop="2rem",
                            color=rx.cond(IndexState.isButton1, u.primaryTextColor, u.secondaryTextColor),
                            backgroundColor=rx.cond(IndexState.isButton1, u.primaryBackgroundColor, u.secondaryBackgroundColor),
                        ),
                        href='/prompting'
                    )
                ),
                opacity=f"{IndexState.percent}%",
                on_mouse_leave=IndexState.updateOpacity(False),
                on_mouse_move=IndexState.updateOpacity(True),
            )


"""App init"""

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
app.add_page(index, '/')
app.add_page(p.prompting, '/prompting')