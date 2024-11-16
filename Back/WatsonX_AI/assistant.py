import json
from llm_setup import create_chain
import prompts

class WatsonXAssistant:
    def __init__(self):
        self.query_chain = create_chain(prompts.query_template)
        self.document_chain = create_chain(prompts.document_template)
        self.impact_chain = create_chain(prompts.impact_template)
        self.wbs_chain = create_chain(prompts.wbs_template)
        self.meeting_chain = create_chain(prompts.meeting_template)
        self.scope_chain = create_chain(prompts.scope_template)

    def process_query(self, query):
        return self.query_chain.run(query=query)

    def generate_document(self, doc_type, project_details):
        return self.document_chain.run(doc_type=doc_type, project_details=json.dumps(project_details))

    def analyze_impact(self, current_state, proposed_changes):
        return self.impact_chain.run(current_state=json.dumps(current_state), proposed_changes=json.dumps(proposed_changes))

    def generate_wbs(self, project_details):
        return self.wbs_chain.run(project_details=json.dumps(project_details))

    def simulate_meeting(self, stakeholders, project_goals):
        return self.meeting_chain.run(stakeholders=stakeholders, project_goals=project_goals)

    def validate_scope(self, project_scope):
        return self.scope_chain.run(project_scope=json.dumps(project_scope))