import streamlit as st
import pandas as pd
import plotly.express as px
import webbrowser as wb
import openpyxl
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Hi, NurElisya Haslinda 👧🏻")
st.header("Im Watching you 👁️")
#st.title("🚚 Genuine Inside (M) Sdn. Bhd.")
st.markdown("##")

df1 = pd.read_excel("Example Dataset.xlsx",sheet_name="Receiving")
df2 = pd.read_excel("Example Dataset.xlsx",sheet_name="Putaway")
df3 = pd.read_excel("Example Dataset.xlsx",sheet_name="Batch Picking")
df4 = pd.read_excel("Example Dataset.xlsx",sheet_name="Sorting")
df5 = pd.read_excel("Example Dataset.xlsx",sheet_name="Packing")
df6 = pd.read_excel("Example Dataset.xlsx",sheet_name="Loading")

df1.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)
df2.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)
df3.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)
df4.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)
df5.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)
df6.rename(columns = {'date (D/M/Y)':'tarikh'}, inplace = True)

with pd.ExcelWriter('RENAMED ATZ Daily.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Receiving', index = False)
    df2.to_excel(writer, sheet_name='Putaway', index = False)
    df3.to_excel(writer, sheet_name='Batch Picking', index = False)
    df4.to_excel(writer, sheet_name='Sorting', index = False)
    df5.to_excel(writer, sheet_name='Packing', index = False)
    df6.to_excel(writer, sheet_name='Loading', index = False)

data_file2 = pd.read_excel('RENAMED ATZ Daily.xlsx')
#fileloc(r"C:\...\...")

# ---- Select sheet ----
#if data_file2:
#    file_details = {
#        "Filename":data_file2.name,
#        "FileType":data_file2.type,
#        "FileSize":data_file2.size}

#    wb = openpyxl.load_workbook(data_file2)

#    sheet_selector = st.sidebar.selectbox("Select sheet:",wb.sheetnames)
#    selected_df = pd.read_excel(data_file2,sheet_selector)
    #st.markdown(f"### Sheet : `{sheet_selector}`")
    #st.write(selected_df)

# ---- SIDEBAR ----
#st.sidebar.header("Please Filter Here:")

#username = st.sidebar.multiselect(
#"Select username:",
#options=selected_df["user_name"].unique(),
#default= selected_df["user_name"].unique(),
#)

#dmy = st.sidebar.multiselect(
#"Select Date:",
#options= selected_df["tarikh"].unique(),
#default= selected_df["tarikh"].unique(),
#)

#---- FILTERED ----
#df_filtered = df.query(
#"user_name == @username & tarikh == @dmy"
#)
##st.dataframe(df_filtered)

st.header("✍ Receiving")
df1s = df1.groupby('user_name').sum(numeric_only=True)
containerA = st.container()
chart1, chart2 = containerA.columns(2)
with chart1:
    # ---- BARCHART ----
    fig = px.bar(
        df1,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'}
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_trace(go.Scatter(
    x=df1s.index,
    y=df1s['totaldoc'],
    text=df1s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart2:
    # ---- LINE CHART----
    fig = px.line(
        df1,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

st.header("📦 Putaway")
df2=df2[(df2['user_name'].str.contains('Ko Latt')) | (df2['user_name'].str.contains('Thaw Zin Oo')) | (df2['user_name'].str.contains('MR LOW')) | (df2['user_name'].str.contains('Nyi Nyi')) | (df2['user_name'].str.contains('THAT TI TUN')) | (df2['user_name'].str.contains('BoBO')) | (df2['user_name'].str.contains('Than Naing'))]
df2s = df2.groupby('user_name').sum(numeric_only=True)
containerB = st.container()
chart3, chart4 = containerB.columns(2)
with chart3:
    # ---- BARCHART ----
    fig = px.bar(
        df2,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'},
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_trace(go.Scatter(
    x=df2s.index,
    y=df2s['totaldoc'],
    text=df2s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart4:
    # ---- LINE CHART----
    fig = px.line(
        df2,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        markers=True,
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

st.header("🧺 Picking")
df3=df3[(df3['user_name'].str.contains('PAPA')) | (df3['user_name'].str.contains('SAN SAN MAW')) | (df3['user_name'].str.contains('Wai Mar Lwin')) | (df3['user_name'].str.contains('Htet Htet Aung')) | (df3['user_name'].str.contains('Thae Mon Thu')) | (df3['user_name'].str.contains('Wine Wine Lail')) | (df3['user_name'].str.contains('Tun Win Sein')) | (df3['user_name'].str.contains('Myo Myat Thu'))]
df3s = df3.groupby('user_name').sum(numeric_only=True)
containerC = st.container()
chart5, chart6 = containerC.columns(2)
with chart5:
    # ---- BARCHART ----
    fig = px.bar(
        df3,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'},
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_hline(y=5000, line_dash="dash", line_color="white" )
    fig.add_trace(go.Scatter(
    x=df3s.index,
    y=df3s['totaldoc'],
    text=df3s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart6:
    # ---- LINE CHART----
    fig = px.line(
        df3,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        markers=True,
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.add_hline(y=800, line_dash="dash", line_color="white" )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

st.header("📥 Sorting")
df4=df4[(df4['user_name'].str.contains('Aye Thida Aung')) | (df4['user_name'].str.contains('HLA HLA WIN')) | (df4['user_name'].str.contains('Phyu Htwe Tun')) | (df4['user_name'].str.contains('MALISSA')) | (df4['user_name'].str.contains('MIN OO')) | (df4['user_name'].str.contains('Wine Wine Lail'))]
df4s = df4.groupby('user_name').sum(numeric_only=True)
containerD = st.container()
chart7, chart8 = containerD.columns(2)
with chart7:
    # ---- BARCHART ----
    fig = px.bar(
        df4,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'},
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_hline(y=9000, line_dash="dash", line_color="white" )
    fig.add_trace(go.Scatter(
    x=df4s.index,
    y=df4s['totaldoc'],
    text=df4s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart8:
    # ---- LINE CHART----
    fig = px.line(
        df4,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        markers=True,
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.add_hline(y=1000, line_dash="dash", line_color="white" )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

st.header("🎁 Packing")
df5=df5[(df5['user_name'].str.contains('Mu Mu Lwin')) | (df5['user_name'].str.contains('Myo Ma')) | (df5['user_name'].str.contains('Shwe Win')) | (df5['user_name'].str.contains('Nyi Nyi')) | (df5['user_name'].str.contains('Maung Oo')) | (df5['user_name'].str.contains('Aung Soe Lin')) | (df5['user_name'].str.contains('Win Than Htay'))]
df5s = df5.groupby('user_name').sum(numeric_only=True)
containerE = st.container()
chart9, chart10 = containerE.columns(2)
with chart9:
    # ---- BARCHART ----
    fig = px.bar(
        df5,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'},
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_trace(go.Scatter(
    x=df5s.index,
    y=df5s['totaldoc'],
    text=df5s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart10:
    # ---- LINE CHART----
    fig = px.line(
        df5,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        markers=True,
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

st.header("🚛 Loading")
df6s = df6.groupby('user_name').sum(numeric_only=True)
containerF = st.container()
chart11, chart12 = containerF.columns(2)
with chart11:
    # ---- BARCHART ----
    fig = px.bar(
        df6,
        x="user_name",
        y="totaldoc",
        color="user_name",
        title="This Month Total",
        labels={'user_name':'Name','totaldoc':'Total'},
        )
    #fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    fig.add_trace(go.Scatter(
    x=df6s.index,
    y=df6s['totaldoc'],
    text=df6s['totaldoc'],
    mode='text',
    textposition='top center',
    showlegend=False))
    st.plotly_chart(fig, use_container_width=True)
with chart12:
    # ---- LINE CHART----
    fig = px.line(
        df6,
        x="tarikh",
        y="totaldoc",
        color="user_name",
        markers=True,
        text="totaldoc",
        title="Total Per Day",
        labels={'user_name':'Name','tarikh':'Date'},
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)

