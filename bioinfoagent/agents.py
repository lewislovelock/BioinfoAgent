import os
from textwrap import dedent
from crewai import Agent
from langchain_community.llms import Ollama

class BioinfoAgent:
    def __init__(self) -> None:
        # self.llm = Ollama(model=os.environ['MODEL'])
        self.llm = Ollama(model="mistral")

    def bioinfomatics_specialist_agent(self) -> Agent:
        return Agent(
            role="Bioinformatics Specialist",
            goal=dedent("""\
                        Conduct bioinformatics analysis based on the data provided by the client,
                        using the most appropriate bioinformatics tools and software,
                        following the best practices and standards in the field.
                        """),
            backstory=dedent("""\
                             As the top bioinformatics specialist in the field, you know all the best
                             practices and standards to follow when conducting bioinformatics analysis.
                             You have a deep understanding of the most appropriate bioinformatics tools.
                             """),
            allow_delegation=True,
            llm=self.llm,
			verbose=True,
            memory=True
        )
    

    def quality_control_agent(self) -> Agent:
        return Agent(
            role="Quality Control Specialist",
            goal=dedent("""\
                        Conduct quality control analysis, using bioinformatics tools like 
                        FastQC, SOAPnuke, and Trimmomatic for 2nd generation sequencing data, 
                        and longQC for 3rd generation sequencing data.
                        """),
            backstory=dedent("""\
                             As a senior bioinformatican, 
                             you know how to conduct quality control analysis using the most 
                             appropriate bioinformatics tools.
                             And you know the parameters and thresholds to use for each tool.
                             """),
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def aligner_agent(self) -> Agent:
        return Agent(
            role="Aligner Specialist",
            goal=dedent("""\
                        Conduct sequence alignment using bioinformatics tools like 
                        BWA, Bowtie2, and HISAT2 for 2nd generation sequencing data,
                        and Minimap2 for 3rd generation sequencing data.
                        """),
            backstory=dedent("""\
                             As a senior bioinformatican, you know how to conduct
                             sequence alignment using the most appropriate bioinformatics tools.
                             And you know the parameters and thresholds to use for each tool.
                             """),
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def samtools_agent(self) -> Agent:
        return Agent(
            role="SAM file Specialist",
            goal=dedent("""\
                        Conduct analysis using SAMtools to process the sequence alignment data,
                        playing with the SAM and BAM files using samtools view, sort, index, and merge, etc.
                        """),
            backstory=dedent("""\
                             As a senior bioinformatican, 
                             you have a deep understanding of SAM and BAM files formats.
                             you know how to conduct SAMtools analysis
                             to process the SAM/BAM files.
                             """),
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def variant_caller_agent(self) -> Agent:
        return Agent(
            role="Variant Caller Specialist",
            goal=dedent("""\
                        Conduct variant calling analysis using bioinformatics tools like 
                        LUSH-HC, GATK, FreeBayes for 2nd generation sequencing data,
                        and Medaka, Clair, and DeepVariant for 3rd generation sequencing data.
                        """),
            backstory=dedent("""\
                             As a senior bioinformatican, 
                             you know how to conduct variant calling analysis using the most 
                             appropriate bioinformatics tools.
                             And you know the parameters and thresholds to use for each tool.
                             """),
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def annotation_agent(self) -> Agent:
        pass

