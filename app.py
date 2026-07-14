import streamlit as st
st.set_page_config(page_title="Customer 360 AI - Bhavana Yalla", layout="wide")
st.title("Customer 360 AI Dashboard")
st.caption("Built by Bhavana Yalla for Volopay Growth Squad")

customer = st.text_input("Enter Company Name", "Acme Corp")

if st.button("Get Customer View"):
    st.metric("Health Score", "65/100", "-15 At Risk")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("CRM Data - Zoho")
        st.write("**Deal**: $20,000 | **Stage**: Proposal | **Owner**: Aman")
        st.subheader("Support Data - Intercom") 
        st.write("- Ticket #102: Invoice not received - Open 5 days")
    with col2:
        st.subheader("Risks")
        st.error("1. 2 open billing tickets")
        st.subheader("Opportunities")
        st.success("1. Renewal in 30 days")
    st.warning("**Next Best Action**: CS to call finance and resolve invoice today.")
@Bhavana916-b
Comment
