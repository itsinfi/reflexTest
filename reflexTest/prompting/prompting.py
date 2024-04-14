from reflexTest.utils import u
import reflex as rx


class PromptingState(rx.State):
    

    def submitPrompt(self):
        print('yo')



def prompting() -> rx.Component:
    return  rx.vstack(
                u.Card(
                    rx.form(
                        rx.text(
                            'Prompt with Mr. GPT',
                            size='8',
                            weight='bold',
                            paddingBottom="1rem",
                        ),
                        rx.text_area(
                            placeholder='Type here...',
                            marginTop='2rem',
                            marginBottom='2rem',
                            minHeight='200px',                              
                        ),
                        rx.center(
                            rx.button(
                                'Start prompting',
                                size='2',
                                color=u.primaryTextColor,
                                backgroundColor=u.primaryBackgroundColor,
                                # on_click=PromptingState.submitPrompt,
                            ),
                        ),
                        rx.divider(
                            marginTop='4rem',
                            marginBottom='4rem',
                        ),
                        rx.text(
                            'Response:',
                            weight='bold',
                        ),
                        rx.text(
                            'No response',
                        ),
                        width='1700px', #TODO: dynamisch anpassen an breite (muss noch rausfinden wie genau das hier geht)
                        # backgroundColor='red',
                    ),
                    marginTop='40px',
                )
            )