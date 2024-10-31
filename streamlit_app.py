# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.header("Flaric Reports")
st.markdown(
    "> **Rising Flare** এর অভিযোগ ও পরামর্শ কেন্দ্র। আপনার নাম বা আইডি বা কোনো তথ্যই আমাদের কাছে জমা থাকার সুযোগও নেই। পাশাপাশি আপনার প্রদত্ত তথ্যও গোপন থাকবে।"
)
st.markdown(
    "> **Rising Flare**'s complaint and advice center. We do not store any information about your name, ID, or any other information. Your provided information will also remain confidential."
)

st.markdown("---")

st.subheader("চলুন শুরু করি...")
st.markdown("> নিচের প্রদত্ত তথ্যগুলো মেহেরবানি করে পূরণ করুন এবং সাবমিট করুন।")

title = st.text_input("শিরোনাম", placeholder="উদাহারণস্বরূপ, resource খুজে পাই না...")
title_description = st.text_area(
    "বিস্তারিত",
    placeholder="উদাহারণস্বরূপ, সবগুলো বিষয়ভিত্তিক টপিকে একই সাথে progress ও resource এর সংমিশ্রণের কারণে progress খুজে পেতে অসুবিধা হয়...",
)

try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    if st.button("সাবমিট করুন", icon=":material/mood:", use_container_width=True):
        # Read the latest data from the spreadsheet
        df = conn.read()

        data = {"Title": title, "Description": title_description}
        temp_df = pd.DataFrame([data])

        # Update the dataframe and the spreadsheet
        updated_df = pd.concat([df, temp_df], ignore_index=True)
        conn.update(data=updated_df)
        st.success("সফলভাবে সাবমিট হয়েছে!")

except Exception as e:
    st.error(f"Error: {e}")
