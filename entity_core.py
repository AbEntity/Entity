PRINCIPI_ETICI = {
    "trasparenza": "Le decisioni devono essere spiegabili.",
    "equità": "Evita pregiudizi verso gruppi vulnerabili.",
    "responsabilità": "Ogni scelta deve essere tracciabile."
}

def descrivi_principi():
    for nome, descrizione in PRINCIPI_ETICI.items():
        print(f"{nome.upper()}: {descrizione}")
