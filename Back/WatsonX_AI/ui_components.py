import streamlit as st

def render_query_tab(assistant):
    st.markdown("## Natural Language Query")
    query = st.text_input("Enter your project management query")
    if st.button("Submit Query"):
        response = assistant.process_query(query)
        st.markdown("### Response:")
        st.markdown(response)

def render_documents_tab(assistant):
    st.markdown("## Generate Project Documents")
    project_name = st.text_input("Project Name")
    objectives = st.text_area("Objectives (comma-separated)")
    features = st.text_area("Features (comma-separated)")
    requirements = st.text_area("Requirements (comma-separated)")
    business_objectives = st.text_area("Business Objectives (comma-separated)")
    stakeholders = st.text_area("Stakeholders (comma-separated)")
    
    if st.button("Generate Documents"):
        project_details = {
            "project_name": project_name,
            "objectives": objectives.split(","),
            "features": features.split(","),
            "requirements": requirements.split(","),
            "business_objectives": business_objectives.split(","),
            "stakeholders": stakeholders.split(",")
        }
        for doc_type in ['PRD', 'BRD', 'Scope', 'Plans']:
            content = assistant.generate_document(doc_type, project_details)
            st.markdown(f"### {doc_type}")
            st.markdown(content)

def render_impact_tab(assistant):
    st.markdown("## Impact Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Current State")
        timeline = st.number_input("Current Timeline (months)", min_value=1, value=6)
        budget = st.number_input("Current Budget", min_value=0, value=500000)
        team_size = st.number_input("Current Team Size", min_value=1, value=10)
    with col2:
        st.markdown("### Proposed Changes")
        new_feature = st.text_input("Proposed New Feature")
        timeline_extension = st.number_input("Proposed Timeline Extension (months)", min_value=0, value=2)
        budget_increase = st.number_input("Proposed Budget Increase", min_value=0, value=100000)
    
    if st.button("Analyze Impact"):
        current_state = {
            "timeline": timeline,
            "budget": budget,
            "team_size": team_size
        }
        proposed_changes = {
            "new_feature": new_feature,
            "timeline_extension": timeline_extension,
            "budget_increase": budget_increase
        }
        impact_analysis = assistant.analyze_impact(current_state, proposed_changes)
        st.markdown("### Impact Analysis")
        st.markdown(impact_analysis)

def render_wbs_tab(assistant):
    st.markdown("## Work Breakdown Structure (WBS) Generator")
    if st.button("Generate WBS"):
        project_details = {
            "project_name": st.session_state.get('project_name', ''),
            "objectives": st.session_state.get('objectives', '').split(","),
            "features": st.session_state.get('features', '').split(","),
            "requirements": st.session_state.get('requirements', '').split(",")
        }
        wbs = assistant.generate_wbs(project_details)
        st.markdown("### Work Breakdown Structure")
        st.markdown(wbs)

def render_meeting_tab(assistant):
    st.markdown("## Stakeholder Meeting Simulation")
    if st.button("Simulate Stakeholder Meeting"):
        stakeholders = st.session_state.get('stakeholders', '').split(",")
        objectives = st.session_state.get('objectives', '').split(",")
        meeting_summary = assistant.simulate_meeting(
            stakeholders=", ".join(stakeholders),
            project_goals=", ".join(objectives)
        )
        st.markdown("### Meeting Summary")
        st.markdown(meeting_summary)

def render_scope_tab(assistant):
    st.markdown("## Project Scope Validation")
    in_scope = st.text_area("In Scope Items (comma-separated)")
    out_of_scope = st.text_area("Out of Scope Items (comma-separated)")
    constraints = st.text_area("Constraints (comma-separated)")
    
    if st.button("Validate Scope"):
        project_scope = {
            "in_scope": in_scope.split(","),
            "out_of_scope": out_of_scope.split(","),
            "constraints": constraints.split(",")
        }
        scope_validation = assistant.validate_scope(project_scope)
        st.markdown("### Scope Validation")
        st.markdown(scope_validation)