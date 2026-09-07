import streamlit as st

st.set_page_config(page_title="AI Prompt Generátor", page_icon="🎨")

st.title("🎨 AI Prompt Generátor")
st.write("Vyplň pár otázek a dostaneš hotový prompt pro Midjourney, Bing Image Creator nebo DALL-E.")

# --- Vstupy od uživatele ---
subjekt = st.text_input("Co / kdo má být na obrázku?", placeholder="např. usměvavá žena")

cinnost = st.text_input("Co dělá?", placeholder="např. pije mléko na terase")

prostredi = st.selectbox(
    "Prostředí",
    ["Středomořská terasa", "Pláž při západu slunce", "Kavárna", "Vinice", "Městská ulice", "Les", "Jiné"]
)

if prostredi == "Jiné":
    prostredi = st.text_input("Popiš vlastní prostředí")

styl = st.selectbox(
    "Styl obrázku",
    ["Fotorealistický", "Ilustrace / kreslený", "Akvarel", "3D render", "Retro / vintage"]
)

nálada = st.select_slider(
    "Nálada",
    options=["Klidná", "Veselá", "Dramatická", "Snová"],
    value="Veselá"
)

# --- Generování promptu ---
if st.button("Vygenerovat prompt"):
    if not subjekt or not cinnost:
        st.warning("Vyplň prosím alespoň 'Co/kdo' a 'Co dělá'.")
    else:
        prompt = (
            f"{styl} obrázek: {subjekt}, {cinnost}, "
            f"prostředí: {prostredi}, nálada: {nálada.lower()}, "
            f"přírodní osvětlení, vysoký detail, ostré zaostření"
        )
        st.success("Hotovo! Zkopíruj si tento prompt:")
        st.code(prompt, language=None)
        st.caption("Tip: AI nástroje reagují nejlépe na anglické prompty — případně nech přeložit.")

st.divider()
st.caption("Vytvořeno jako ukázka appky v Pythonu (Streamlit), spustitelná v mobilu bez instalace Pythonu.")
