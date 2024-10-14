# # COEFF = 1.96
# COEFF =  1.955
# euro = float(input("EUR: "))
# print(f"BGN: {round(euro*COEFF,2)}")

tuple = (1,2,3)
print(tuple)
print(tuple[2])
# tuple[2] = "abc"
# tuple.add("abc")
# tuple.remove("abc")
tuple = (1,2,"abc")
print(tuple)
tuple = (3,)
print(tuple)

URL = "https://api.exchangerate-api.com/v4/latest/EUR"

import requests

response = requests.get(URL)
print(response.json()["rates"])
print(response.status_code)
if response.status_code ==200:
    COEFF = response.json()["rates"]["BGN"]
else:
    COEFF =  1.955

# PySimpleGUI_License = 'owggSIrkq5rhPbeWKVHMmYJX6NM0VIZjGovgOIninI7suIcCNJUDPb72S1lwwYyWV5F57IGjNoLgDIVl6BJ57UX2glbtsckG5xClaUx2M9JmGdnCPIDs0ImCOJ5DqdwX9NO09b32610lxctkflJ'

import PySimpleGUI as sg

import PySimpleGUI as pg

# layout = [
#     [pg.Text("EUR:",font=("Arial",16)),pg.InputText(focus=True,size=(30,1)),pg.Button("Convert")],
#     [pg.Text("BGN:"),pg.InputText(readonly=True,size=(30,)),pg.Button("Close")]
# ]

layout = [
    [pg.Combo(("EUR","BGN"),default_value="EUR",
              key="--IN-MONEY--",enable_events=True,readonly=True),
              pg.InputText(focus=True,key="--IN--"),pg.Button("Convert",bind_return_key=True)],
    [pg.Combo(("EUR","BGN"),default_value="BGN",readonly=True,
              key="--OUT-MONEY--"),
              pg.InputText(readonly=True,key="--OUT--"),pg.Button("Close")]
]

pg.theme("BluePurple")
window = pg.Window("Money Converter",layout=layout)

while True:
    event, values = window.read()

    if event in (pg.WIN_CLOSED,"Close"):
        break
    elif event =="--IN-MONEY--":
        money_type = values["--IN-MONEY--"]
        if money_type == "EUR":
            new_money = "BGN"
        else:
            new_money = "EUR"
        window["--OUT-MONEY--"].update(new_money)
    elif event=="Convert" and values["--IN--"]!="":
        euro = float(values["--IN--"])
        if euro <= 0:
            window["--IN--"].update("")
            window["--OUT--"].update("")
            continue
        if values["--IN-MONEY--"]=="EUR":
            result = round(euro*COEFF,2)
        else:
            result = round(euro/COEFF,2)
        window["--OUT--"].update(result)

window.close()