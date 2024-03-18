from crewai import Task
from textwrap import dedent

class BioinformaticsAnalysisTasks:
    def __init__(self, pipeline_type, data_path) -> None:
        self.pipeline_type = pipeline_type
        self.data_path = data_path

    def __tip_section(self) -> str:
        return "If your do your BEST WORK, I'll give you a $10,000 commission!"
    
    def pipeline_design(self, agent):
        return Task(
            description=dedent(f"""\
                Design a bioinformatics pipeline: {self.pipeline_type}
                for the analysis data located at {self.data_path}
                The pipeline should include use the most appropriate 
                bioinformatics tools and software following the 
                best practices.
                {self.__tip_section()}
                """),
            expected_output="A bioinformatics pipeline design",
            agent = agent
        )
    
    def quality_control(self, agent):
        return Task(
            description=dedent(f"""\
                Conduct quality control analysis, using bioinformatics tools like 
                FastQC, SOAPnuke, and Trimmomatic for 2nd generation sequencing data, 
                and longQC for 3rd generation sequencing data.
                {self.__tip_section()}
                """),
            expected_output="Quality control analysis report",
            agent = agent
        )
    
    def alignment(self, agent):
        return Task(
            description=dedent(f"""\
                Conduct sequence alignment using bioinformatics tools like 
                BWA, Bowtie2, and HISAT2 for 2nd generation sequencing data,
                and Minimap2 for 3rd generation sequencing data.
                {self.__tip_section()}
                """),
            expected_output="bam file",
            agent = agent
        )
    

    def variant_calling(self, agent):
        return Task(
            description=dedent(f"""\
                Conduct variant calling analysis using bioinformatics tools like 
                GATK, FreeBayes, and VarScan for 2nd generation sequencing data,
                and Sniffles for 3rd generation sequencing data.
                {self.__tip_section()}
                """),
            expected_output="Variant calling analysis report",
            agent = agent
        )
    
    def samtools(self, agent):
        return Task(
            description=dedent(f"""\
                Conduct analysis using SAMtools to process the sequence alignment data,
                playing with the SAM and BAM files using samtools view, sort, index, and merge, etc.
                {self.__tip_section()}
                """),
            expected_output="SAMtools analysis report",
            agent = agent
        )
    

    
