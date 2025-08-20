
import streamlit as st

# ------------------ Passwortschutz ------------------ #
def check_password():
    def password_entered():
        if st.session_state["password"] == "plenum2025":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Entferne Passwort nach Prüfung
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("🔒 Passwort erforderlich", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("🔒 Passwort erforderlich", type="password", on_change=password_entered, key="password")
        st.error("❌ Falsches Passwort")
        return False
    else:
        return True

# ------------------ App Inhalt ------------------ #
if check_password():
    st.set_page_config(page_title="Plenum Tools", layout="centered")
    st.title("🔧 Plenum Tool Startseite")
    st.markdown("Willkommen! Wähle unten das gewünschte Tool:")

    st.markdown("### 1️⃣ Vertriebsprovision berechnen")
    st.write("Berechne die monatliche Vertriebsfolgeprovision basierend auf NAV, Units und Basispunkten.")
    st.link_button("➡️ Öffnen", "https://vertriebsprovision.streamlit.app")

    st.markdown("### 2️⃣ NAV Mapping Tool")
    st.write("Konvertiert NAV-Dateien ins einheitliche Layout für die Provisionsberechnung.")
    st.link_button("➡️ Öffnen", "https://nav-mapping-tool.streamlit.app")

    st.markdown("### 3️⃣ Holding Mapping Tool")
    st.write("Einheitliche Aufbereitung verschiedenster Holdings-Dateien von Distributoren.")
    st.link_button("➡️ Öffnen", "https://holding-mapping.streamlit.app")

    st.markdown("---")
    st.caption("🔐 Zugriff nur mit Passwort – vertraulich © Plenum AG")
