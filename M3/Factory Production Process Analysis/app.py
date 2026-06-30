import streamlit as st
import pandas as pd
df = pd.read_csv("production_quality_dataset.csv")
st.title("Production Process Analysis")
st.write('''A factory manager is worried 
         that scrap is increasing in the 
         production process. You receive 
         a simplified production dataset 
         and must use Pandas to investigate 
         machine and shift performance.''')
st.dataframe(df)
df["scrap_rate"] = df["defective_units"] / df["units_produced"].replace(0, pd.NA)
machine_summary = (
    df.groupby("machine")
    .agg({
        "batch_id" : "count",
        "units_produced" : "sum",
        "defective_units" : "sum",
        "scrap_rate" : "mean"
    })
)
st.subheader("Machine-level summary")
st.dataframe(machine_summary)
shift_summary = (
    df.groupby("shift")
    .agg({
        "batch_id" : "count",
        "units_produced": "sum",
        "defective_units": "sum",
        "scrap_rate" : "mean"
    })
)
st.subheader("Shift-level summary")
st.dataframe(shift_summary)
machine_filter = df[df["units_produced"] > 500]
st.dataframe(machine_filter)