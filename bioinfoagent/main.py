from crewai import Crew, Process
from textwrap import dedent
from agents import BioinfoAgent
from tasks import BioinformaticsAnalysisTasks
from langchain_community.llms import Ollama


class BioinfoCrew:
    def __init__(self, pipeline, data_path) -> None:
        self.pipeline = pipeline
        self.data_path = data_path
        self.manager_llm = Ollama(model="mistral")
        
    def invoke(self):
        agents = BioinfoAgent()
        tasks = BioinformaticsAnalysisTasks(self.pipeline, self.data_path)

        pipeline_designer = agents.bioinfomatics_specialist_agent()
        aligner = agents.aligner_agent()
        quality_control = agents.quality_control_agent()
        variant_caller = agents.variant_caller_agent()
        samtools = agents.samtools_agent()

        pipeline_design = tasks.pipeline_design(pipeline_designer)
        aligner_task = tasks.alignment(aligner)
        quality_control_task = tasks.quality_control(quality_control)
        variant_calling_task = tasks.variant_calling(variant_caller)
        samtools_task = tasks.samtools(samtools)

        crew = Crew(
            agents=[pipeline_designer, quality_control, aligner, samtools, variant_caller],
            tasks=[pipeline_design, aligner_task, quality_control_task, variant_calling_task, samtools_task],
            manager_llm=self.manager_llm,
            process=Process.hierarchical,
            verbose=True
        )

        result = crew.kickoff()
        return result
    
    def solo(self):
        agents = BioinfoAgent()
        tasks = BioinformaticsAnalysisTasks(self.pipeline, self.data_path)

        aligner = agents.aligner_agent()
        alignment = tasks.alignment(aligner)

        pipeline_designer = agents.bioinfomatics_specialist_agent()
        pipeline_design = tasks.pipeline_design(pipeline_designer)

        crew = Crew(
            agents=[aligner],
            tasks=[alignment],
            verbose=True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to the Bioinformatics Crew!")
    print("--------------------------------------")
    pipeline = input(
        dedent("""\
        What type of bioinformatics pipeline do you want to execute?
        (e.g., variant calling etc.): """)
    )
    data_path = input(
        dedent("""\
        Enter the path to the data you want to analyze: """)
    )
    crew = BioinfoCrew(pipeline, data_path)
    # result = crew.invoke()
    result = crew.solo()
    print("\n\n##############################")
    print(f"## Here is the {pipeline} pipline Result")
    print(result)