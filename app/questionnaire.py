__author__ = 'kthurime'

from libraries.traitify import Traitify

class Questionnaire:

    def __init__(self, deck_id):
        self.secrect_key = "13ba33b4bi33jlq1lnu9i3oroe"
        self.traitify_instance = Traitify(self.secrect_key)
        self.assessment = self.traitify_instance.create_assessment(deck_id)

    def create_new_questionnaire(self):
        return self.traitify_instance.get_assessment(self.assessment.id)

    def get_assessment_results(self):
        personality_types = self.traitify_instance.get_personality_types(self.assessment.id)
        return personality_types["personality_types"][0].personality_type
