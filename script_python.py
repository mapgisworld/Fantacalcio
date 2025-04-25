import pandas as pd

squadre_fantaecr=pd.read_excel("DATI/DATI FANTACALCIO.xlsx", sheet_name="SQUADRE_FANTAECR")
statistiche_fantacalcio=pd.read_excel("DATI/DATI FANTACALCIO.xlsx", sheet_name="Statistiche_Fantacalcio")

# il file contiene le statistiche dei calciatori delle squadre fanta ecr
file_merge=squadre_fantaecr.merge(statistiche_fantacalcio,how="inner",on="Calciatore")

# Questo file andrà ad aggiornare il foglio Classifica Fair Play presente sul file excel DATI FANTACALCIO
# In questa fase i dati del Fair Play sono stati aggiornati con le squadre successive al calciomercato, bisogna aggiungere i voti dei giocatori svincolati
file_merge.to_excel("DATI/STATISTICHE_FANTAECR_BASE.xlsx", sheet_name="STATISTICHE_FANTAECR", index=False)
