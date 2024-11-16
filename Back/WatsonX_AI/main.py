import streamlit as st
from assistant import WatsonXAssistant
from ui_components import (
    render_query_tab,
    render_documents_tab,
    render_impact_tab,
    render_wbs_tab,
    render_meeting_tab,
    render_scope_tab
)

def main():
    st.markdown("# WatsonX AI Project Assistant")
    st.markdown("Manage your project with AI-powered insights")

    assistant = WatsonXAssistant()

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Natural Language Query", "Generate Documents", "Impact Analysis", 
        "WBS Generator", "Stakeholder Meeting", "Scope Validation"
    ])

    with tab1:
        render_query_tab(assistant)

    with tab2:
        render_documents_tab(assistant)

    with tab3:
        render_impact_tab(assistant)

    with tab4:
        render_wbs_tab(assistant)

    with tab5:
        render_meeting_tab(assistant)

    with tab6:
        render_scope_tab(assistant)

if __name__ == "__main__":
    main()