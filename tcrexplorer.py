import panel as pn
from tcrapi import TCRAPI
import sankey as sk

# Loads javascript dependencies and configures Panel (required)
pn.extension()

# Initialize the tcr api
api = TCRAPI()
api.load_tcr("tcr.csv")

# WIDGET DECLARATIONS

# Search Widgets
diagnosis = pn.widgets.Select(name="Diagnosis", options=api.get_diagnosis(), value='Malignant')
min_cases = pn.widgets.IntSlider(name="Min Cases", start=1, end=10, step=1, value=3)

# Country Widget
countries = sorted(api.get_countries())
country_selector = pn.widgets.Select(name="Country", options=countries, value=countries[0])

# Plotting widgets
width = pn.widgets.IntSlider(name="Width", start=250, end=2000, step=250, value=1000)
height = pn.widgets.IntSlider(name="Height", start=200, end=2500, step=100, value=1000)

# CALLBACK FUNCTIONS

# CALLBACK FUNCTIONS

def get_catalog(diagnosis, min_cases, country):
    global local
    # Pass the selected country as a single country
    local = api.extract_local_network(diagnosis, min_cases, countries=[country])  # Make sure to pass a list
    table = pn.widgets.Tabulator(local, selectable=False)
    return table

def get_plot(diagnosis, min_cases, country, width, height):
    local_data = api.extract_local_network(diagnosis, min_cases, countries=[country])  # Filter by the selected country (as a list)
    return sk.make_sankey(local_data, "Diagnosis", "Age", vals="ncases", width=width, height=height)


# CALLBACK BINDINGS (Connecting widgets to callback function parameters)
catalog = pn.bind(get_catalog, diagnosis, min_cases, country_selector)
plot = pn.bind(get_plot, diagnosis, min_cases, country_selector, width, height)

# DASHBOARD WIDGET CONTAINERS ("CARDS")

card_width = 320

search_card = pn.Card(
    pn.Column(
        diagnosis,
        min_cases,
        country_selector  # Add country selector to the search card
    ),
    title="Search", width=card_width, collapsed=False
)

plot_card = pn.Card(
    pn.Column(
        width,
        height
    ),
    title="Plot", width=card_width, collapsed=True
)

# LAYOUT

layout = pn.template.FastListTemplate(
    title="Thyroid Cancer Risk Data",
    sidebar=[
        search_card,
        plot_card,
    ],
    theme_toggle=False,
    main=[
        pn.Tabs(
            ("Cases", catalog),  # Replace None with callback binding
            ("Network", plot),  # Replace None with callback binding
            active=1  # Which tab is active by default?
        )
    ],
    header_background='#a93226'
).servable()

layout.show()
