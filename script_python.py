import pandas as pd

squadre_fantaecr=pd.read_excel("DATI/DATI FANTACALCIO.xlsx", sheet_name="SQUADRE_FANTAECR")
statistiche_fantacalcio=pd.read_excel("DATI/DATI FANTACALCIO.xlsx", sheet_name="Statistiche_Fantacalcio")

# il file contiene le statistiche dei calciatori delle squadre fanta ecr
file_merge=squadre_fantaecr.merge(statistiche_fantacalcio,how="inner",on="Calciatore")

file_merge.to_excel("DATI/STATISTICHE_FANTAECR_BASE.xlsx", sheet_name="STATISTICHE_FANTAECR", index=False)
