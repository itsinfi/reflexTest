import reflex as rx
import requests

"""Farb-Variablen"""
primaryBackgroundColor = 'indigo'
secondaryBackgroundColor = 'yellow'
primaryTextColor = 'white'
secondaryTextColor = 'black'


"""Card Komponente"""
def Card(*children: rx.Component, **props: any) -> rx.Component:
    return  rx.container(
                rx.center(
                    rx.vstack(
                        *children,
                        align='center',
                    )
                ),
                width='calc(100% - 100px)',
                size='4',
                backgroundImage='linear-gradient(#272727, #111111)',
                opacity="90%",
                borderRadius='30px',
                boxShadow='2px 2px 5px #00000055',
                marginLeft='50px',
                marginRight='50px',
                marginBottom='50px',
                padding='50px',
                **props,
            )