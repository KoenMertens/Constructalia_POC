import streamlit as st

# Pagina instellingen
st.set_page_config(page_title="ArcelorMittal POC Bot", layout="centered")

# Custom CSS voor een strakke 'show' (geen icons/symbols)
st.markdown("""
<style>
    .stChatMessage { background-color: #f0f2f6; border-radius: 10px; padding: 10px; margin-bottom: 10px; }
    .stChatInputContainer { padding-bottom: 20px; }
</style>
""", unsafe_allow_html=True)

st.title("Constructalia Product Expert POC")
st.write("Vraag informatie over XCarb, Angelina, Granite, Magnelis of specifieke bouwoplossingen.")

# De verzamelde data van je vragen
KNOWLEDGE_BASE = {
    "xcarb": "XCarb is the umbrella brand for ArcelorMittal's low-carbon steel initiatives. It includes green steel certificates, recycled and renewably produced steel (EAF route), and an innovation fund. The biggest benefit is reducing Scope 3 emissions. Link: https://constructalia.arcelormittal.com/en/sustainability",
    "angelina": "Angelina beams are structural steel beams with sinusoidal web openings. They are ideal for long spans (20-40m) and allow technical services to pass through the beam. Link: https://constructalia.arcelormittal.com/en/products/acb-and-angelina-beams",
    "magnelis": "Magnelis is the most durable solution for corrosion resistance (Zinc, 3.5% Al, 3% Mg). It is up to 10x better than galvanized steel and has self-healing properties. Link: https://constructalia.arcelormittal.com/en/products/magnelis",
    "granite": "Granite is an organic coated steel range with high UV and corrosion resistance (RC5/RUV4). It is used for aesthetic facades and roofing. Link: https://constructalia.arcelormittal.com/en/products/granite",
    "sica": "SiCA (Sustainable Industrial Construction Assistant) is a tool with 5 lessons to evaluate the environmental and economic impact of industrial buildings. Link: https://constructalia.arcelormittal.com/en/tools-and-services/sica-sustainable-industrial-construction-assistant",
    "office": "For office buildings, we recommend Angelina beams (HVAC integration), Slim Floor (flat ceilings), and Steligence for flexible design. Link: https://constructalia.arcelormittal.com/en/applications/offices",
    "residential": "For residential buildings, we offer Cofraplus/Cofradal floors, Mauka Line roofing, and Granite facade coatings. Link: https://constructalia.arcelormittal.com/en/applications/residential-buildings",
    "silos": "The most durable solution for silos is Magnelis (ZM310) or S390 EK for enameled silos. Link: https://constructalia.arcelormittal.com/en/applications/agriculture",
    "co2": "The product with the lowest CO2 emissions is XCarb Recycled and Renewably Produced steel (approx. 300kg CO2/tonne). Link: https://constructalia.arcelormittal.com/en/products/xcarb-recycled-and-renewably-produced"
}

# Chat logica
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hallo! Ik ben de Constructalia expert. Waar kan ik je mee helpen?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Typ je vraag (bijv. 'Wat is XCarb?')..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simpele keyword matching
    query = prompt.lower()
    response = "Ik heb in deze POC alleen informatie over XCarb, Angelina, Magnelis, Granite, SiCA, kantoren, woningbouw, silo's en CO2 uitstoot."
    
    for key, value in KNOWLEDGE_BASE.items():
        if key in query:
            response = value
            break

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})