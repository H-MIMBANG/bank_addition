import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt  # Importation de matplotlib.pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 
import streamlit as st  

# Initialiser l'attribut si ce n'est pas déjà fait  
if 'page_selection' not in st.session_state:  
    st.session_state.page_selection = 'valeur_par_defaut'  # Remplacez par la valeur souhaitée
# Configuration de l'image de fond
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-opacity: 0.1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Appliquer l'image de fond (remplacer 'background.jpg' par votre fichier)
alt.themes.enable("dark")

# -------------------------
# Barre latérale (identique)

# ... [Le code de la barre latérale reste inchangé] ...

# -------------------------

# Charger les données
try:
    df = pd.read_csv('bank-additional.csv', delimiter=';')
except Exception as e:
    st.error(f"Une erreur est survenue : {e}")
    st.stop()
    add_bg_from_url("https://cdn.pixabay.com/photo/2017/10/31/19/05/bank-2906640_1280.jpg")
# -------------------------
# Section interactive des graphiques

if st.session_state.page_selection == 'jeu_de_donnees':
    st.title("📊 Exploration Interactive des Données")
    
    # Contrôles interactifs
    with st.expander("Options de Visualisation"):
        col1, col2 = st.columns(2)
        with col1:
            selected_x = st.selectbox("Axe X", df.select_dtypes(include=['number']).columns)
        with col2:
            selected_y = st.selectbox("Axe Y", df.select_dtypes(include=['number']).columns)
            
        plot_type = st.radio("Type de graphique", ["Nuage de points", "Histogramme", "Boxplot"])
    
    # Création dynamique des graphiques
    if plot_type == "Nuage de points":
        brush = alt.selection_interval()
        chart = alt.Chart(df).mark_circle(size=60).encode(
            x=selected_x,
            y=selected_y,
            color=alt.condition(brush, 'y', alt.value('lightgray')),
            tooltip=list(df.columns)
        ).add_selection(brush).interactive()
        
        st.altair_chart(chart, use_container_width=True)
        
    elif plot_type == "Histogramme":
        chart = alt.Chart(df).mark_bar().encode(
            alt.X(selected_x, bin=True),
            y='count()',
            color='y',
            tooltip=['count()']
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
        
    elif plot_type == "Boxplot":
        chart = alt.Chart(df).mark_boxplot().encode(
            x='y:N',
            y=selected_y,
            color='y'
        ).interactive()
        st.altair_chart(chart, use_container_width=True)
    
    # Section de filtrage dynamique
    with st.expander("Filtres Dynamiques"):
        age_range = st.slider("Filtrer par âge", 
                             min_value=int(df['age'].min()), 
                             max_value=int(df['age'].max()), 
                             value=(20, 80))
        
        filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
        
        st.write(f"Nombre de clients filtrés : {len(filtered_df)}")
        st.altair_chart(alt.Chart(filtered_df).mark_bar().encode(
            x='job:N',
            y='count()',
            color='y'
        ).

interactive(), use_container_width=True)

# ... [Le reste des pages reste inchangé] ...

# Configuration de la page
st.set_page_config(
    page_title="Classification des Données Bancaires",
    page_icon="🏦",  
    layout="wide", 
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# -------------------------
# Barre latérale

if 'page_selection' not in st.session_state:
    st.session_state.page_selection = 'à propos'  # Page par défaut

# Fonction pour mettre à jour page_selection
def set_page_selection(page):
    st.session_state.page_selection = page

with st.sidebar:
    st.title(' 🏦 Classification des Données Bancaires')

    # Navigation par boutons
    st.subheader("Sections")
    if st.button("À Propos", use_container_width=True, on_click=set_page_selection, args=('à propos',)):
        pass
    if st.button("Jeu de Données", use_container_width=True, on_click=set_page_selection, args=('jeu de données',)):
        pass
    if st.button("Analyse Exploratoire", use_container_width=True, on_click=set_page_selection, args=('analyse exploratoire',)):
        pass
    if st.button("Prédiction", use_container_width=True, on_click=set_page_selection, args=('prédiction',)):
        pass
    if st.button("Conclusion", use_container_width=True, on_click=set_page_selection, args=('conclusion',)):
        pass

# Charger les données
try:
    df = pd.read_csv('bank-additional-full.csv', delimiter=';')
except FileNotFoundError:
    st.error("Le fichier 'bank-additional-full.csv' est introuvable. Veuillez vérifier son emplacement.")
    st.stop()

# Page principale
if st.session_state.page_selection == 'a_propos':
    # Page À Propos
    st.title("️ À Propos")
    st.markdown("""
        Cette application explore le jeu de données Bank Marketing et propose :

        - Une exploration visuelle des données.
        - Un prétraitement et nettoyage des données.
        - La construction et l'évaluation de modèles d'apprentissage automatique.
        - Une interface interactive pour prédire si un client souscrira à un produit.

        Technologies utilisées :
        - Python (Streamlit, Altair, Pandas)
        - Machine Learning (Scikit-learn)

        Auteur : MIMBANG HEDDY

        ✉️ Contact : heddy_mimbang@icloud.com
    """)
elif st.session_state.page_selection == 'conclusion':
     # Page À Propos
    st.title("️ conclusion")
    st.markdown("""
        Un traitement minutieux et réfléchi du DataFrame bank-additional-full est fondamental pour maximiser la précision 
        et la fiabilité du modèle de prédiction. En combinant explorations, prétraitements adéquats, et évaluations rigoureuses,
         on peut développer un modèle robuste qui est mieux équipé pour prédire les comportements des clients envers la souscription à un produit.
    """)

elif st.session_state.page_selection == 'jeu_de_donnees':
    # Page Jeu de Données
    st.title(" Jeu de Données")

    # Afficher les premières lignes du DataFrame
    if st.checkbox("Afficher le DataFrame"):
        nb_rows = st.slider("Nombre de lignes à afficher :", min_value=105, max_value=41189, value=10)
        st.write(df.head(nb_rows))

    # Afficher les statistiques descriptives
    if st.checkbox("Afficher les statistiques descriptives"):
        st.write(df.describe())

elif st.session_state.page_selection == 'analyse_exploratoire':
    import seaborn as sns  # Importation de seaborn
    import matplotlib.

pyplot as plt  # Importation de matplotlib.pyplot
    import altair as alt

    st.title(" Analyse Exploratoire")

    # Remplacement des valeurs 'unknown'
    for column in df.columns:
        if df[column].dtype == 'object':
            mode_value = df[column].mode()[0]
            df[column] = df[column].replace('unknown', mode_value)

    # Sélection des colonnes catégorielles
    categorical_cols = [col for col in df.columns if df[col].dtype == 'object' and col != 'y']

    # Affichage des tables croisées et graphiques
    for column in categorical_cols:
        st.subheader(f"Table croisée pour {column}")
        st.write(df.groupby(['y', column])[column].size().unstack(level=0))

        st.subheader(f"Countplot pour {column}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x=df["y"], hue=df[column], ax=ax)
        st.pyplot(fig)  # Utilisation de st.pyplot pour afficher le graphique

    # Vérification des valeurs manquantes
    st.subheader("Vérification des valeurs manquantes")
    missing_values = df.isnull().sum()
    st.write(missing_values[missing_values > 0])

    # Graphique Altair
    st.subheader("Relation entre l'âge et le métier")
    df['job'] = df['job'].astype('category')
    age_job_chart = (
        alt.Chart(df)
        .mark_circle(size=60)
        .encode(
            x=alt.X('age:Q', title='Âge'),
            y=alt.Y('job:O', title='Métier', sort=None),
            color='y:N',
            tooltip=['age:Q', 'job:N', 'y:N']
        )
        .properties(
            title='Relation entre l\'âge et le métier',
            width=600,
            height=400
        )
        .interactive()
    )
    st.altair_chart(age_job_chart, use_container_width=True)

elif st.session_state.page_selection == 'apprentissage_automatique':
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report, confusion_matrix

    # ... (votre code pour charger X et y)

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    # Charger le DataFrame
    df = pd.read_csv('bank-additional-full.csv', delimiter=';')

    # Vérifiez que les colonnes nécessaires existent
    print(df.columns)
 # numérisation des valeurs catégorielles 
    import pandas as pd  
    # Encodage des variables catégorielles avec pd.get_dummies (One-Hot Encoding)
    df_encoded = pd.get_dummies(df, drop_first=True)

    # Vérifier les données encodées
    df_encoded.head()

    # Vérification des valeurs manquantes
    df_encoded.isnull().sum()

    # Remplissage des valeurs manquantes
    df_encoded.fillna(df_encoded.mean(), inplace=True)

# Séparation des variables indépendantes (X) et de la cible (y)
X = df_encoded.drop(columns=['y_yes'])  # 'y_yes' étant la variable binaire (1 ou 0)
y = df_encoded['y_yes']  # La cible

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner un modèle simple pour tester
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

        # Tester une prédiction
    prediction = model.predict(X_test)
    print(prediction[:5])  # Afficher les premières prédictions

    # Création et entraînement du modèle
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    from sklearn.utils import resample  

    # Concatenation des données d'origine  
    data = pd.concat([X_train, y_train], axis=1)  

    # Séparez les classes

no_class = data[data['y'] == 0]  # Classe majoritaire  
    yes_class = data[data['y'] == 1]  # Classe minoritaire  

    # Sous-échantillonnage de la classe majoritaire  
    no_class_downsampled = resample(no_class,  
                                 replace=False,  # Ne pas remplacer  
                                 n_samples=len(yes_class),  # Pour équilibrer  
                                 random_state=42)  # Pour la reproductibilité  

    # Combiner la classe minoritaire avec la classe majoritaire sous-échantillonnée  
    balanced_data = pd.concat([no_class_downsampled, yes_class])  

    #  Séparer les caractéristiques et la cible  
    X_balanced = balanced_data.drop('y', axis=1)  
    y_balanced = balanced_data['y']  
elif st.session_state.page_selection == 'prediction':
        # ... (votre code pour la page de prédiction)
        # Page Prédiction  
    st.title("🔮 Prédiction")  
    from sklearn.ensemble import RandomForestClassifier  

        # Formulaire pour saisir les caractéristiques  
    age = st.number_input("Âge du client", min_value=18, max_value=120, value=30)  
    duration = st.number_input("Durée du contact (seconds)", min_value=0, value=60)  
    campaign = st.number_input("Nombre de contacts lors de la campagne", min_value=1, value=1)  
    
    if st.button("Prédire"): 
        from sklearn.model_selection import train_test_split  
        from sklearn.preprocessing import StandardScaler  
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import confusion_matrix
        import seaborn as sns  
        import matplotlib.pyplot as plt  # Importation de matplotlib.pyplot  
    try:  
            # Prétraitement potentiel des données d'entrée et des caractéristiques  
            # (Assurez-vous que le modèle est déjà formé au préalable et chargé ici)  
            X = df[['age', 'duration', 'campaign']]  # Ajustez selon vos colonnes de caractéristiques.  
            y = df['y']  # Cible à prédire  
            
            # Splitting and training d'un modèle d'exemple  
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  
            model = RandomForestClassifier()  
            model.fit(X_train, y_train)  
            
            prediction = model.predict([[age, duration, campaign]])  
            subscription_status = "Oui" if prediction[0] == 'yes' else "Non"  
            st.success(f"Le client va-t-il souscrire au produit ? : **{subscription_status}**") 
            # Prédictions  
            y_pred = model.predict(X_test)  

            # Évaluation  
            from sklearn.metrics import confusion_matrix
            from sklearn.metrics import classification_report, accuracy_score
            print(confusion_matrix(y_test, y_pred))  
            print(classification_report(y_test, y_pred))
    except Exception as e:  
            st.error(f"Une erreur est survenue : {e}")
