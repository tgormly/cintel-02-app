"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
import shinyswatch
from shiny import *


# TODO: Change the shinyswatch theme to morph, cosmo, darkly, flatly, sketchy (or other shinyswatch theme)
# Completed with quartz selected

# Preview at https://bootswatch.com/
app_ui = ui.page_navbar(
    shinyswatch.theme.quartz(),
    ui.nav(
        "Home",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Sidebar Panel"),
                ui.tags.hr(),
                ui.h3("User Interaction Here"),
                ui.input_text("name_input", "Enter your name", placeholder="Your Name"),
                ui.input_text("language_input", "Enter your favorite language(s)", placeholder="Favorite Programming Language(s)"),
                ui.tags.hr(),
            ),
            ui.panel_main(
                ui.h2("Main Panel with Reactive Output"),
                ui.output_text_verbatim("welcome_output"),
                ui.output_text_verbatim("insights_output"),
            ),
        ),
    ),
    # TODO: Update the links to reflect your own about, GitHub repo, and app
    # App link updated, but
    # TODO: needs to be taken care of in Github
    ui.nav(ui.a("About", href="https://github.com/tgormly")),
    ui.nav(ui.a("GitHub", href="https://github.com/tgormly/cintel-02-app")),
    ui.nav(ui.a("App", href="https://tgormly.github.io/cintel-02-app/")),
    ui.nav(ui.a("Shiny", href="https://shiny.posit.co/py/")),
    ui.nav(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.nav(ui.a("Themes", href="https://rstudio.github.io/py-shinyswatch/")),
    ui.nav(ui.a("Deploy", href="https://docs.posit.co/shinyapps.io/getting-started.html#working-with-shiny-for-python")),
    # TODO: Update the title to reflect yourname Dashboard
    # Completed
    title=ui.h1("Tim Gormly Dashboard"),
)


def server(input, output, session):
    """
    This is the required server function.
    @param input: a dictionary of input values
    @param output: a dictionary of output functions
    @param session: a dictionary of session values (not used)
    """

    # Define the reactive outputs. Tell what to render and how to render it
    # TODO: Customize the reactive greeting.
    # Completed

    @output
    @render.text
    def welcome_output():
        user = input.name_input();
        if len(user) > 0:
            welcome_string = f'{user}! Hello, and welcome to my app!';
            return welcome_string
        else:
            welcome_string = f'Hello!  Please enter your name in the box on the left.';
            return welcome_string


    @output
    @render.text
    def insights_output():
        answer = input.language_input()
        count = len(answer)
        if answer == '':
            message = 'Tell us your favorite programming language(s) in the textbox on the left'
            return message
        else:
            language_string = f'You like {answer}. That takes {count} characters'
            return language_string

# Create a Shiny App by passing in the two parts defined above.
app = App(app_ui, server, debug=True)