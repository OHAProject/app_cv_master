#coding:Utf-8
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Areour Mohamed Cherfi"
PAGE_ICON = "⚛️"
NAME = "Areour Mohamed Cherif"
DESCRIPTION = """
Ingénieur de formation ma passion pour les nouvelles technologies ainsi que mes différentes expériences 
professionnel mon permis d'acquérir une grande expérience dans différents domaines tels que l'internet des objets, 
l'informatique embarquée est la programmation. l'opérateur mobile Ooredoo et L'AGENCE NATIONALE DE PROMOTION ET DE DEVELOPPEMENT DES PARCS TECHNOLOGIQUES (ANPT)
m’ont fait confiance pour l'animation de plusieurs formations.
"""
EMAIL = "areour.mohamed@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@OpenhardwareAlgerie/featured",
    "LinkedIn": "https://dz.linkedin.com/in/mohamed-cherif-areour",
    "GitHub": "https://github.com/OpenHDZ",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- SIDE BAR ---
st.sidebar.write(
    """
    - ► **Age** : 40 ans
    - ► **Adresse** : 21, Bâtiment 5F, Cité 1500 logements AADL, Oulad Hadadj, Boumerdes, Algérie
    - ► **Téléphone** : +213 (0) 555795208
    """
)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger le CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 14 ans d'expérience professionnelle dans différents domaines (industrie, recherche, entreprenariat)
- ✔️ Une expérience de plus de 20 ans avec le langage de programmation Python (dans un cadre académique ou bien professionnel)
- ✔️ Une expérience de plus de 8 ans en formation et animation de cours dans différents domaines de techniques
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 🖥️ Langage de programmation : Python et C 
- 📊 Traitement de données avec Pandas
- 📈 Data Visulization: Matplotlib, Seaborn, Plotly, Streamlit
- 📚 Modeling: en utilisant Scikit Leran (Logistic regression, linear regression, decition trees, Clustering) 
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Expérience dans la formation")
st.write("---")

# --- JOB 1
st.write("💻", "**Consultant formateur en Programmation Python**")
st.write("02-2023 - jusqu'à Aujourd'hui")
st.write(
    """
    CONSULTANT FORMATEUR POUR LE COMPTE DE L'AGENCE NATIONALE DE PROMOTION ET DE DEVELOPPEMENT DES PARCS TECHNOLOGIQUES (ANPT) :
- ►   Assurer des formations d'introduction à la programmation avec le langage de programmation Python
- ►   Assurer des formations d'approfondissement de la programmation avec le langage Python
- ►   Assurer des formations d'introduction à l'analyse de données et à la data sciences avec Python

"""
)

# --- JOB 2
st.write("💻", "**Consultant formateur en Prototypage rapide**")
st.write("02-2019 - jusqu'à Aujourd'hui")
st.write(
    """
    CONSULTANT FORMATEUR POUR LE COMPTE DE L'AGENCE NATIONALE DE PROMOTION ET DE DEVELOPPEMENT DES PARCS TECHNOLOGIQUES (ANPT) :
- ►   +	Assurer des formations sur le désigner, la conception et la réalisation de solution connectée (IoT). 
"""
)

# --- JOB 3
st.write("💻", "**COACH FORMATEUR**")
st.write("2016 - 2018")
st.write(
    """
    COACH FORMATEUR POUR LE COMPTE DE L'ENTREPRISE MEDIALABS:
- ►   Assurer des formations d'introduction l'informatique embarquée et à l'internet des objets
- ►   Assurer l'encadrement d'équipes d'étudiants pour la réalisation de leurs prototypes pour le concours oobarmidjoo de l'opérateur mobile Ooredoo
"""
)

# --- JOB 4
st.write("💻", "**COACH FORMATEUR**")
st.write("05/2015 - 10/2015")
st.write(
"""
    COACH FORMATEUR POUR LE COMPTE DE L'OPERATEUR MOBILE OOREDOO:
- ►   Assurer des formations d'introduction l'informatique embarquée et à l'internet des objets
- ►   Assurer l'encadrement d'équipes d'étudiants pour la réalisation de leurs prototypes pour le concours oobarmidjoo de l'opérateur mobile ooredoo
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Expérience Professionnelle")
st.write("---")

# --- JOB 1
st.write("🏭", "**Responsable méthode maintenance et production | ALSEV Spa**")
st.write("09/2021 - jusqu'à Aujourd'hui")
st.write(
    """
- ► Mise en place d'un tableau de bord de suivi de la production et de la performance de la fonction maintenance 
- ► Manager une équipe de 3 méthodistes de production et une méthodiste maintenance afin de garantir une disponibilité maximale des machines et un ordonnancement optimale des commandes
- ► La mise en place d'un politique TPM
"""
)

# --- JOB 2
st.write('\n')
st.write("🏭", "**Responsable méthode maintenance | ALSEV SPA**")
st.write("02/2021 - 09/2021")
st.write(
    """
- ► Mise en place d'une solution web de gestion et de suivie de la maintenance assistée par ordinateur pour la réalisation des taches maintenance préventive et curative 
- ► Mise en place de nouvelles procédures pour la gestion de la maintenance 
- ► Mise en place de nouveau indicateurs de performance pour la fonction maintenance 
"""
)

# --- JOB 3
st.write('\n')
st.write("📡", "**FONDATEUR ET DIRECTEUR TECHNIQUE | START-UP FANOS**")
st.write("02/2019 - 01/2021")
st.write(
    """
- ► La conception et l'intégration de solutions innovantes dans le domaine des objets connectés
- ► Assurer des formations sur l'utilisation des techniques de communication sans fil LPWAN
"""
)

# --- JOB 4
st.write('\n')
st.write("☢️", "**CHEF DU SERVICE EXPERIMENTATION HALL| CRNB**")
st.write("11/2015 - 02/2019")
st.write(
    """
- ► En charge de la supervision d'expérimentation sur réacteur à la division réacteur du centre de recherche nucléaire de Birine, wilaya de Djelfa
"""
)

# --- JOB 5
st.write('\n')
st.write("☢️", "**INGENIEUR SPECIALISE EN MAINTENANCE DES SYSTEMES CONTROLE COMMANDE DU REACTEUR | CRNB**")
st.write("2012 - 2015")
st.write(
    """
- ► En charge de la maintenance des systèmes de contrôle commande du réacteur au service maintenance contrôlé commande
 du réacteur, à la division réacteur du centre de recherche nucléaire de Birine, wilaya de Djelfa.
"""
)


# --- JOB 6
st.write('\n')
st.write("☢️", "**INGENIEUR EN MAINTENANCE DES SYSTEMES CONTROLE COMMANDE DU REACTEUR | CRNB**")
st.write("2010 - 2012")
st.write(
    """
- ► En charge de la maintenance des systèmes de contrôle commande du réacteur au service maintenance contrôlé commande
 du réacteur, à la division réacteur du centre de recherche nucléaire de Birine, wilaya de Djelfa.
"""
)

# --- JOB 7
st.write('\n')
st.write("🏭", "**CHARGER D’AFFAIRE MÉCANIQUE | Michelin Algérie**")
st.write("2010 - 2012")
st.write(
    """
- ► En charge de la conception et le suivi de réalisation de la modernisation des équipements de production au niveau du bureau d’études de là direction technique à l'usine Micheline Algérie d’Hussein Dey
"""
)
