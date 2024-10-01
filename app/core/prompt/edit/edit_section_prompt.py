from langchain.prompts import PromptTemplate

edit_section_prompt = PromptTemplate(
    template="""
    ### Instructions
    1. Edit user survey data following prompt: {user_prompt}
    2. Your modified the survey data must harmonize with prototype survey data
    3. Find the section in the prototype survey data based on the title key of user survey data and reference it

    ### User Survey Data
    1. {user_survey_data}
    
    """,
    input_variables=["user_prompt", "user_survey_data"])
