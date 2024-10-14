# # COEFF = 1.96
COEFF =  1.955
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

PySimpleGUI_License = 'owggSIrkq5rhPbeWKVHMmYJX6NM0VIZjGovgOIninI7suIcCNJUDPb72S1lwwYyWV5F57IGjNoLgDIVl6BJ57UX2glbtsckG5xClaUx2M9JmGdnCPIDs0ImCOJ5DqdwX9NO09b32610lxctkflJ'

import PySimpleGUI as sg

import PySimpleGUI as pg

# layout = [
#     [pg.Text("EUR:",font=("Arial",16)),pg.InputText(focus=True,size=(30,1)),pg.Button("Convert")],
#     [pg.Text("BGN:"),pg.InputText(readonly=True,size=(30,)),pg.Button("Close")]
# ]

layout = [
    [pg.Text("EUR:"),pg.InputText(focus=True),pg.Button("Convert")],
    [pg.Text("BGN:"),pg.InputText(readonly=True),pg.Button("Close")]
]

pg.theme("BluePurple")
window = pg.Window("Money Converter",layout=layout)

while True:
    event, values = window.read()

    if event in (pg.WIN_CLOSED,"Close"):
        break
    elif event=="Convert":
        # print(values[0])
        euro = float(values[0])
        result = round(euro*COEFF,2)
        # print(result)
        window[1].update(result)

window.close()