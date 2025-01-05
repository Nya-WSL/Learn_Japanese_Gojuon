import json
import random
from nicegui import ui, native, app

version = "0.10.0"
hira_path = "data/hira_dict.json"
kata_path = "data/kata_dict.json"
app.add_static_files('/static', 'static')
port = native.find_open_port(65000, 65525)

def check_hira(id):
    with open(hira_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if data[id]["status"] == True:
        data[id]["status"] = False
    else:
        data[id]["status"] = True
    with open(hira_path, "w+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def check_kata(id):
    with open(kata_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if data[id]["status"] == True:
        data[id]["status"] = False
    else:
        data[id]["status"] = True
    with open(kata_path, "w+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

### Init Dict ###
with open(hira_path, "r", encoding="utf-8") as f:
    hira_data = json.load(f)
with open(kata_path, "r", encoding="utf-8") as f:
    kata_data = json.load(f)

for i in hira_data:
    hira_data[i]["status"] = False
with open(hira_path, "w+", encoding="utf-8") as f:
    json.dump(hira_data, f, ensure_ascii=False, indent=4)

for i in kata_data:
    kata_data[i]["status"] = False
with open(kata_path, "w+", encoding="utf-8") as f:
    json.dump(kata_data, f, ensure_ascii=False, indent=4)

### GUI ###

# Main Page #
@ui.page("/")
def index():
    ui.add_head_html(r'''
<style>
@font-face{
    font-family: "ResourceHanRounded";
    src: url('/static/RESOURCEHANROUNDEDJ-MEDIUM.TTF') format('truetype');
    font-weight: normal;
    font-style: normal;
}
</style>
''')

    def start():
        with open(hira_path, "r", encoding="utf-8") as f:
            hira_data = json.load(f)
        with open(kata_path, "r", encoding="utf-8") as f:
            kata_data = json.load(f)
        bool_hira = []
        bool_kata = []
        for id in hira_data:
            if hira_data[id]["status"] == True:
                bool_hira.append(id)
        for id in kata_data:
            if kata_data[id]["status"] == True:
                bool_kata.append(id)

        if bool_hira == [] and bool_kata == []:
            ui.notify("请选择行", position="center", type="negative")
        else:
            ui.navigate.to("/roman")

    with open(hira_path, "r", encoding="utf-8") as f:
        hira_data = json.load(f)
    with open(kata_path, "r", encoding="utf-8") as f:
        kata_data = json.load(f)
    with ui.row().style('font-family: "ResourceHanRounded"; font-weight: bold;'):
        with ui.card(align_items="center"):
            with ui.row():
                with ui.column():
                    a_hira = ui.checkbox("清音あ行 ひらがな", value=hira_data["a_hira"]["status"], on_change=lambda: check_hira("a_hira"))
                    ka_hira = ui.checkbox("清音か行 ひらがな", value=hira_data["ka_hira"]["status"], on_change=lambda: check_hira("ka_hira"))
                    sa_hira = ui.checkbox("清音さ行 ひらがな", value=hira_data["sa_hira"]["status"], on_change=lambda: check_hira("sa_hira"))
                    ta_hira = ui.checkbox("清音た行 ひらがな", value=hira_data["ta_hira"]["status"], on_change=lambda: check_hira("ta_hira"))
                    na_hira = ui.checkbox("清音な行 ひらがな", value=hira_data["na_hira"]["status"], on_change=lambda: check_hira("na_hira"))
                    ha_hira = ui.checkbox("清音は行 ひらがな", value=hira_data["ha_hira"]["status"], on_change=lambda: check_hira("ha_hira"))
                    ma_hira = ui.checkbox("清音ま行 ひらがな", value=hira_data["ma_hira"]["status"], on_change=lambda: check_hira("ma_hira"))
                    ya_hira = ui.checkbox("清音や行 ひらがな", value=hira_data["ya_hira"]["status"], on_change=lambda: check_hira("ya_hira"))
                    ra_hira = ui.checkbox("清音ら行 ひらがな", value=hira_data["ra_hira"]["status"], on_change=lambda: check_hira("ra_hira"))
                    bion_hira = ui.checkbox("鼻音 ひらがな", value=hira_data["bion_hira"]["status"], on_change=lambda: check_hira("bion_hira"))
                    ga_hira = ui.checkbox("濁音が行 ひらがな", value=hira_data["ga_hira"]["status"], on_change=lambda: check_hira("ga_hira"))
                    za_hira = ui.checkbox("濁音ざ行 ひらがな", value=hira_data["za_hira"]["status"], on_change=lambda: check_hira("za_hira"))
                with ui.column():
                    da_hira = ui.checkbox("濁音だ行 ひらがな", value=hira_data["da_hira"]["status"], on_change=lambda: check_hira("da_hira"))
                    pa_hira = ui.checkbox("濁音ぱ行 ひらがな", value=hira_data["pa_hira"]["status"], on_change=lambda: check_hira("pa_hira"))
                    kya_hira = ui.checkbox("拗音きゃ行 ひらがな", value=hira_data["kya_hira"]["status"], on_change=lambda: check_hira("kya_hira"))
                    sya_hira = ui.checkbox("拗音しゃ行 ひらがな", value=hira_data["sya_hira"]["status"], on_change=lambda: check_hira("sya_hira"))
                    cya_hira = ui.checkbox("拗音ちゃ行 ひらがな", value=hira_data["cya_hira"]["status"], on_change=lambda: check_hira("cya_hira"))
                    nya_hira = ui.checkbox("拗音にゃ行 ひらがな", value=hira_data["nya_hira"]["status"], on_change=lambda: check_hira("nya_hira"))
                    hya_hira = ui.checkbox("拗音ひゃ行 ひらがな", value=hira_data["hya_hira"]["status"], on_change=lambda: check_hira("hya_hira"))
                    mya_hira = ui.checkbox("拗音みゃ行 ひらがな", value=hira_data["mya_hira"]["status"], on_change=lambda: check_hira("mya_hira"))
                    rya_hira = ui.checkbox("拗音りゃ行 ひらがな", value=hira_data["rya_hira"]["status"], on_change=lambda: check_hira("rya_hira"))
                    gya_hira = ui.checkbox("拗音ぎゃ行 ひらがな", value=hira_data["gya_hira"]["status"], on_change=lambda: check_hira("gya_hira"))
                    bya_hira = ui.checkbox("拗音びゃ行 ひらがな", value=hira_data["bya_hira"]["status"], on_change=lambda: check_hira("bya_hira"))

        with ui.card(align_items="center"):
            with ui.row():
                with ui.column():
                    a_kata = ui.checkbox("清音あ行 カタカナ", value=kata_data["a_kata"]["status"], on_change=lambda: check_kata("a_kata"))
                    ka_kata = ui.checkbox("清音か行 カタカナ", value=kata_data["ka_kata"]["status"], on_change=lambda: check_kata("ka_kata"))
                    sa_kata = ui.checkbox("清音さ行 カタカナ", value=kata_data["sa_kata"]["status"], on_change=lambda: check_kata("sa_kata"))
                    ta_kata = ui.checkbox("清音た行 カタカナ", value=kata_data["ta_kata"]["status"], on_change=lambda: check_kata("ta_kata"))
                    na_kata = ui.checkbox("清音な行 カタカナ", value=kata_data["na_kata"]["status"], on_change=lambda: check_kata("na_kata"))
                    ha_kata = ui.checkbox("清音は行 カタカナ", value=kata_data["ha_kata"]["status"], on_change=lambda: check_kata("ha_kata"))
                    ma_kata = ui.checkbox("清音ま行 カタカナ", value=kata_data["ma_kata"]["status"], on_change=lambda: check_kata("ma_kata"))
                    ya_kata = ui.checkbox("清音や行 カタカナ", value=kata_data["ya_kata"]["status"], on_change=lambda: check_kata("ya_kata"))
                    ra_kata = ui.checkbox("清音ら行 カタカナ", value=kata_data["ra_kata"]["status"], on_change=lambda: check_kata("ra_kata"))
                    bion_kata = ui.checkbox("鼻音 カタカナ", value=kata_data["bion_kata"]["status"], on_change=lambda: check_kata("bion_kata"))
                    ga_taka = ui.checkbox("濁音が行 カタカナ", value=kata_data["ga_kata"]["status"], on_change=lambda: check_kata("ga_kata"))
                    za_kata = ui.checkbox("濁音ざ行 カタカナ", value=kata_data["za_kata"]["status"], on_change=lambda: check_kata("za_kata"))
                with ui.column():
                    da_kata = ui.checkbox("濁音だ行 カタカナ", value=kata_data["da_kata"]["status"], on_change=lambda: check_kata("da_kata"))
                    pa_kata = ui.checkbox("濁音ぱ行 カタカナ", value=kata_data["pa_kata"]["status"], on_change=lambda: check_kata("pa_kata"))
                    kya_kata = ui.checkbox("拗音きゃ行 カタカナ", value=kata_data["kya_kata"]["status"], on_change=lambda: check_kata("kya_kata"))
                    sya_kata = ui.checkbox("拗音しゃ行 カタカナ", value=kata_data["sya_kata"]["status"], on_change=lambda: check_kata("sya_kata"))
                    cya_kata = ui.checkbox("拗音ちゃ行 カタカナ", value=kata_data["cya_kata"]["status"], on_change=lambda: check_kata("cya_kata"))
                    nya_kata = ui.checkbox("拗音にゃ行 カタカナ", value=kata_data["nya_kata"]["status"], on_change=lambda: check_kata("nya_kata"))
                    hya_kata = ui.checkbox("拗音ひゃ行 カタカナ", value=kata_data["hya_kata"]["status"], on_change=lambda: check_kata("hya_kata"))
                    mya_kata = ui.checkbox("拗音みゃ行 カタカナ", value=kata_data["mya_kata"]["status"], on_change=lambda: check_kata("mya_kata"))
                    rya_kata = ui.checkbox("拗音りゃ行 カタカナ", value=kata_data["rya_kata"]["status"], on_change=lambda: check_kata("rya_kata"))
                    gya_kata = ui.checkbox("拗音ぎゃ行 カタカナ", value=kata_data["gya_kata"]["status"], on_change=lambda: check_kata("gya_kata"))
                    bya_kata = ui.checkbox("拗音びゃ行 カタカナ", value=kata_data["bya_kata"]["status"], on_change=lambda: check_kata("bya_kata"))
                    tsuika_kata = ui.checkbox("カタカナ追加", value=kata_data["tsuika_kata"]["status"], on_change=lambda: check_kata("tsuika_kata"))

        with ui.column():
            ui.button("开始", on_click=lambda: start())
            ui.button("网页", on_click=lambda: ui.navigate.to(f"http://localhost:{port}", True))

# Roman Page #
@ui.page("/roman")
def index():
    ui.add_head_html(r'''
<style>
@font-face{
    font-family: "ResourceHanRounded";
    src: url('/static/RESOURCEHANROUNDEDJ-MEDIUM.TTF') format('truetype');
    font-weight: normal;
    font-style: normal;
}
</style>
''')

    def hira_choice():
        with open(hira_path, "r", encoding="utf-8") as f:
            hira_data = json.load(f)
        for id in hira_data:
            if hira_data[id]["status"] == True:
                data_list = list(hira_data[id].keys())
                data_list.remove("status")
                key = random.choice(data_list)
                # return hira_data[id][key]
                data = {f"{key}": f"{hira_data[id][f'{key}']}"}
                return data

    def kata_choice():
        with open(kata_path, "r", encoding="utf-8") as f:
            kata_data = json.load(f)
        for id in kata_data:
            if kata_data[id]["status"] == True:
                data_list = list(kata_data[id].keys())
                data_list.remove("status")
                key = random.choice(data_list)
                data = {f"{key}": f"{kata_data[id][f'{key}']}"}
                return data

    def choice():
        with open(hira_path, "r", encoding="utf-8") as f:
            hira_data = json.load(f)
        with open(kata_path, "r", encoding="utf-8") as f:
            kata_data = json.load(f)
        bool_hira = []
        bool_kata = []
        for id in hira_data:
            if hira_data[id]["status"] == True:
                bool_hira.append(id)
        for id in kata_data:
            if kata_data[id]["status"] == True:
                bool_kata.append(id)

        if bool_hira != [] and bool_kata != []:
            return random.choice([hira_choice(), kata_choice()])
        else:
            if bool_hira != []:
                return hira_choice()
            if bool_kata != []:
                return kata_choice()

    def check_roman():
        if f"{roman.value}" in kana_value:
            ui.navigate.to("/roman")
        else:
            ui.notify("罗马音错误，请重新输入", type="negative")

    with ui.card(align_items="center").classes("absolute-center w-2/3").style('font-family: "ResourceHanRounded";'):

        kana = choice()
        for key, value in kana.items():
            name = key
            kana_value = value.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")

            # ui.markdown(f"<font size=30>**{name}**</font>")
            ui.label(name).style("font-size: 15rem;")

        roman = ui.input(label="罗马音").classes("w-full")
        with ui.row():
            ui.button("确认", on_click=lambda: check_roman())
            ui.button("返回", on_click=lambda: ui.navigate.to("/"))
            ui.button("答案", on_click=lambda: ui.notify(f"罗马音：{kana_value}"))

ui.run(title=f"Learn Japanese Gojūon | v{version}", favicon="static/logo.png", port=port, show=False, native=True, reload=False, window_size=[900, 800])