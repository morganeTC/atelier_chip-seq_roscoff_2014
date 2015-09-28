ChIP-seq Peak Calling
=====================

## 1. Retrieve datasets on Gene Expression Omnibus

**Objective:** this first exercice is meant to demonstrate how one can typically retrieve published datasets from the [Gene Expression Omnibus](http://www.ncbi.nlm.nih.gov/geo/) (*GEO*) website, for further analysis. However, we will then use datasets that have already been downloaded and pre-processed to save time.

### 1.1 About the dataset
BLABLBAL For this tutorial we will use ChIP-seq datasets produced by [Theodorou _et al_](http://www.ncbi.nlm.nih.gov/pubmed/23172872). The authors used ChIP-Seq technology in order to systematically identify Estrogen receptor (abbreviated as ER or ERS1) binding regions across the human genome. Importantly, they demonstrated that knock-down of GATA3 through siRNA strongly affect ESR1 binding sites. The corresponding abstract of the article is provided below.

##### Abstract

*Estrogen receptor (ESR1) drives growth in the majority of human breast cancers by binding to regulatory elements and inducing transcription events that promote tumor growth. Differences in enhancer occupancy by ESR1 contribute to the diverse expression profiles and clinical outcome observed in breast cancer patients. GATA3 is an ESR1-cooperating transcription factor mutated in breast tumors; however, its genomic properties are not fully defined.   
In order to investigate the composition of enhancers involved in estrogen-induced transcription and the potential role of GATA3, we performed extensive ChIP-sequencing in unstimulated breast cancer cells and following estrogen treatment. We find that GATA3 is pivotal in mediating enhancer accessibility at regulatory regions involved in ESR1-mediated transcription. GATA3 silencing resulted in a global redistribution of cofactors and active histone marks prior to estrogen stimulation. These global genomic changes altered the ESR1-binding profile that subsequently occurred following estrogen, with events exhibiting both loss and gain in binding affinity, implying a GATA3-mediated redistribution of ESR1 binding. The GATA3-mediated redistributed ESR1 profile correlated with changes in gene expression, suggestive of its functionality. Chromatin loops at the TFF locus involving ESR1-bound enhancers occurred independently of ESR1 when GATA3 was silenced, indicating that GATA3, when present on the chromatin, may serve as a licensing factor for estrogen-ESR1-mediated interactions between cis-regulatory elements. Together, these experiments suggest that GATA3 directly impacts ESR1 enhancer accessibility, and may potentially explain the contribution of mutant-GATA3 in the heterogeneity of ESR1+ breast cancer.*

##### Data access
Within the article, there is a section mentioning the accession number of the dataset produced:
_The microarray data and ChIP-seq data from this study have been deposited in the NCBI Gene Expression Omnibus (GEO) (http://www.ncbi.nlm.nih.gov/geo/) under accession nos. GSE39623 and **GSE40129**, respectively._

### 1.2 Find the dataset on Gene Expression Omnibus

Gene Expression Omnibus ([GEO](http://www.ncbi.nlm.nih.gov/geo/)) is a public repository providing tools to submit, access and mine functional genomics data. Data may be related to array- or sequence-based technologies. For *HTS* (*High-Throughput Sequencing*) data, GEO provides both processed data (such as *.bam, *.bed, *.wig files) and links to raw data. Raw data are available from the Sequence Read Archive ([SRA](http://trace.ncbi.nlm.nih.gov/Traces/sra/)) database (including 454, IonTorrent, Illumina, SOLiD, Helicos and Complete Genomics). Both web sites propose search engines to query their databases.

**Procedure**

1.  Go to [GEO web site](http://www.ncbi.nlm.nih.gov/geo/).
2.  Choose "Search" and paste **GSE40129** (GSE stands for GEO Series Experiment). Click "GO" to get information about this experiment.
3.  In the "sample section" (middle of the page), click on "More" to visualize all sample names.
4.  Click on GSM986059 hyperlink (GSM stands for GEO SaMple) to get information about this sample.
5.  In the "relations" section, select "SRX176856" hyperlink to open the SRA page corresponding to this sample.
6.  Click on the SRR link (bottom left) to access the record of the run.
7.  On the new page, click on the **Reads** tab to view the read sequence.

From there, you might also download the dataset as a .sra file, but we **will not do it in the context of this practical** (beware, this would take time and occupy disk space, since SRA files typically weight several hundred MB!).

**Questions**

1.   What is the HTS platform used to sequence this sample?
2.   Is this experiment single-end or paire-end sequencing?
3.   What is the read length?
4.   How many runs (_i.e._ lanes) are associated to this sample?
5.   How many reads were produced (# of Spots)?
6.   Select SRR540188 hyperlink. What is the sequence of the first read?

At this point, you should be able to find a given dataset in GEO, and obtain the raw data (reads).




## 2. Analyze the mapped reads

**Objective:** Retrieve BAM files that contain alignment results, inspect and analyze the mapped reads.

### 2.1 Getting the mapped reads (BAM) within Galaxy

For the sake of time and to avoid repetitions of processing steps already covered in other tutorials, we have already performed quality-check of the reads and mapping. The steps are described [here](../00_read_mapping/mapping_tutorial.html).We encourage participants to check these steps later.

In the next section, we will search for ER (Estrogen Receptor) binding sites in control samples (ChIP Estrogen Receptor on MCF-7 cell line treated with E2). In this tutorial, we will focus on **quality control** of the aligned datasets, **peak calling** and **differential binding analysis**. Hence, the starting point will be **bam files of aligned reads** for the different datasets:

*   ChIP-seq on estrogen receptor (ER) in wild-type condition (siNT), after estrogen induction (E2) (3 replicates available, _siNT_ER_E2_r1, 2, 3_)
*   ChIP-seq on estrogen receptor (ER) after GATA knockout (siGATA), after estrogen induction (E2) (3 replicates available, _siGATA_ER_E2_r1, 2 ,3_)
*   ChIP-seq on the histone mark H3K4me1 in siNT (1 replicate available, _siNT_H3K4me1_Veh_r1_)
*   ChIP-seq on the histone mark H3K4me1 in siGATA (1 replicate available, _siGATA_H3K4me1_Veh_r1_)
*   input control in MCF7 cells (1 replicate available)

**Procedure to import shared history**
    
    TODO: VALIDATE IMPORT

1.  Log into your Galaxy account.
2.  Use **Shared data > published histories > ChIP-seq datasets**
3.  Click on the history name, then in the top right of the page on **Import history**
4.  The datasets should appear in a newly created history called **Imported: ChIP-seq datasets**
5.  Rename this history

### 2.2 Number of mapped reads
Before starting the peak calling analysis, it is interesting to determine the type of alignments enclosed in the BAM files, and the **level of duplicates**.

**Procedure**

1.  In the **search tools box**, search for the **flagstats** tool.
2.  Run this tool on 2 BAM files you imported: **siNT_ER_E2_r3** and **siGATA_ER_E2_r3**.

**Question** 

How many reads does the BAM files contain?  
The table below sumarizes the results for all datasets (all flagstat files are accessible in the Galaxy shared history).

    BAM file                Nb reads
    siNT_ER_E2_r1           21 377 808
    siNT_ER_E2_r2           12 035 808
    siNT_ER_E2_r3           26 826 609
    siGATA_ER_E2_r1         14 177 394
    siGATA_ER_E2_r2         11 588 402
    siGATA_ER_E2_r3         27 429 291
    siNT_H3K4me1_Veh_r1     22 205 385
    siGATA_H3K4me1_Veh_r1   22 227 392
    MCF_input_r3            19 361 330

### 2.3 Coverage for individual BAM files

We will now convert a BAM file to a [bigWig](http://www.genome.ucsc.edu/goldenPath/help/bigWig.html) file, which we can then upload to IGV for visual inspection. We will do this separately for signal and input, and then produce a combined file in which the background noise has been subtracted from the signal.

**Procedure**

1.  Find the tool **bamCoverage** in the **deepTools** section
2.  Select the BAM file for the signal file **siNT_ER_E2_r3**, and run the tool **on chromosome 1 to reduce computational time !**
3.  For _Average size of fragment length_, choose 150 bp. We will check later on whether this estimation is corrrect !
4.  Keep other parameters by default
5.  Execute, and rename the output (otherwise, it might be erased by another run)
6.  Download the resulting file and open it in the IGV browser
7.  In IGV, right click on the left panel: use **set data range**, and set Max Value to **100**
8.  Repeat the same operation for the BAM file corresponding to the **H3K4me1**, and open the resulting bigwig file under the previous one in IGV.
9.  Repeat the same operation for the BAM file corresponding to the **input**, and open the resulting bigwig file under the previous one in IGV.
10.  Download the **BAM files and corresponding indexes (bai)** for: **siNT_ER_E2_r3**, **H3K4me1** and **input**. Load them using IGV. Go to KIAA1324 gene.
11.  For each bam, click on the left panel of the corresponding track and set **Color alignment by > read strand**.
12.  Unzoom and and select regions displaying high signal based on the coverage tracks (_i.e_ bigWig).

**Questions**

1.  Do you see regions that seem to be enriched in signal compared to background?
2.  In the TFF1 gene, check the signal on plus and minus strands for the BAM track obtained from siNT_ER_E2_r3. Does it correspond to the expected signal?
3.  Do you recognize any region where both tracks show enrichment? Could these correspond to copy-number alterations in the MCF7 cell line?
4.  If you compare ER ChIP-seq with H3K4me1 ChIP-seq, do you see a difference in the shape of the data (sharper peaks or broader domains of enrichment)?

### 2.4 Combined coverage file

We want to combine the treatment and input files into one signal file which should indicate the level of signal, taking into account the background noise estimated from the input file. In order to do this, we will use the **bamCompare** tool from the **deepTools** toolbox, and use various normalization strategies discussed during the presentation.

**Procedure**

1.  Select the **bamCompare** tool
2.  Select the **siNT_ER_E2_r3** treatment BAM file and the input BAM file
3.  Choose the SES normalization method in _Method to use for scaling the largest sample to the smallest_
4.  Choose compute difference (substract input from treatment) in _How to compare the two files:_
5.  Choose a particular chromosome (chr1)
6.  Repeat the same operation on the **H3K4me1** treatment BAM file and the input BAM file


**Question** 

Compare the individual coverage files (treatment and input) and the combined one. Are they similar?

(all bamCompare result files are accessible in the Galaxy shared history **Herrmann_bamCompare**)

### 2.5 - Comparing replicates and distinct datasets

When we have replicates, an important check is to what extend they agree between each other. We can compute the correlation of the signal of two datasets in windows over all the genome; this can also be used to compare to distinct datasets and determine, which ones are closest. We will apply this to the 8 datasets we have (excluding the input datasets), using the tool **bamCorrelate** of the deepTools toolbox.

**Procedure**

1.  Find the tool **bamCorrelate** in the list of tools
2.  Supply the 8 bam files coresponding to treatment (exclude input!)
3.  Select **Pearson correlation**
4.  **Important: restrict to one chromosome (**of your choice this time ! Take your favorite chromosome**)**

**Questions**

1.  Which of the samples seem to cluster best?
2.  What about the replicates?
3.  Check with your neighbors how it looks like on a different chromosome.




## 3. Peak-calling using MACS on ER ChIP-Seq

**Objective:** Now that we are (hopefully) convinced that the dataset contains signal, we will perform peak calling for the ESR1 ChIP-seq datasets, using the input dataset as control to identify statistically enriched regions (a.k.a. peaks). Peak calling will be performed using MACS (version 1.4.2).

### 3.1 Single replicate

**Procedure**

1.  Select the tools **MACS14** and fill the form as below:

    *   **Experiment name**: give a name for the MACS run (siNT_ESR1_r3_MACS).
    *   **Paired end sequencing:** MACS can handle single or paired-end data; here we will select single end.
    *   **ChIP-seq tag file**: select the BAM file containing the treatment (ChIP): **siNT_ER_E2_r3**
    *   **ChIP-seq control file**: select the BAM file for the input.
    *   **Effective genome size**: this is the mappable genome size; default is hg19
    *   **Tag size**: these are Illumina datasets of read size 36.
    *   **Diagnosis report:** select **Produce a diagnosis report.**
    *   All other options should be set to default.


**Question** 

1. What type of files does MACS return?

MACS running using these options should generate 2 result files:

*   A html report describing the model built by MACS, and links to additional files
*   A bed file containing the peaks.

For the sake of time, we have already run MACS on all BAM files. The results are available in the Galaxy shared history.

2. Look at the pdf file generated by MACS: what fragment length has been determined by MACS? Is this consistent accross replicates/experiments?

3.   How many peaks have been called by MACS? Use the **Line/Word/Character count** in the **toolbox** to count the number of lines in the bed file.
4.   Use the sort tool in the toolbox to sort MACS peaks according to the score.

### 3.2 Consensus set of peaks

Here, we have 3 replicates for each condition, and therefore 3 sets of peaks. We can build a consensus set by determining the peaks that are found in all 3 replicates. This very simple procedure is likely to reduce the number of false positive peaks (keep in mind however that we might also have an increased false negative rate, if one of the replicates departs largely from the others...).

**Procedure**

1.  Use the tool **intersectBed**, and make the intersection of the files containing the peaks for **siNT** for replicate 1 and 2.
2.  Intersect again the resulting file with the peaks of replicate 3
3.  Repeat the same operation with siGATA replicates.

**Question** 

How many consensus peaks do we have for each condition?


## 4. Differential analysis

**Objective:** Treatment of MCF-7 cells using siRNA to GATA3 is expected to induce a re-localization of ER binding sites. Hence, we want to compare the 2 consensus sets of peaks to determine common/specific peaks. We will compare a "naive" approach with a more quantitative approach.  


### 4.1 Simple approach

**Procedure**

1.  Use the tool **intersectBed**, and make the intersection of the two consensus peak sets for siNT and siGATA

**Question**

1.  How many common peaks do we have?
2.  How many specific peaks do we have for siNT and siGATA?

### 4.2 Quantitative differential analysis using diffBind

Having replicates, we can perform a **quantitative analysis** to identify differentially bound regions. This method is based on the read counts in certain regions, and the identification of regions that show a significant difference in read counts between 2 conditions. This is very similar to the analysis of **differential expression** in RNA-seq, and indeed the underlying statistical models are often the same.  
 Several tools exist, but are not all implemented under Galaxy. We will work with the output file of a tool called [diffBind](http://www.bioconductor.org/packages/release/bioc/html/DiffBind.html) which is part of the Bioconductor packages.  
 DiffBind works by focusing on peak regions shared between a certain number of samples (here: 2 or 3 samples). These regions are then analyzed for differential binding using either [edgeR](http://www.bioconductor.org/packages/release/bioc/html/edgeR.html) or [DESeq2](http://www.bioconductor.org/packages/release/bioc/html/DESeq2.html).

**Procedure**

1.  The files are located in your Galaxy history as **ER.m2.db.bed** and **ER.m3.db.bed**
2.  Determine the number of differential peaks in the 2 files **ER.m2.db.bed** and **ER.m3.db.bed**
3.  Import the 2 bed files into the IGV session; your IGV session should contain
    *   the coverage files for the 3 siNT and siGATA replicates (bigwig, 6 tracks)
    *   the MACS output files for each replicate (bed, 6 tracks)
    *   the consensus peak files for both conditions (bed, 2 tracks)
    *   the differentially bound regions as determined by diffBind (bed, 2 tracks)

**Questions**

1.  Zoom into several differentially bound regions, and look at the peaks determined by MACS.
2.  Can you determine cases in which
    *   a DB region has MACS peaks for both conditions?
    *   a DB region has peaks only for one condition?
    *   Regions with MACS peaks in one condition and not the other are **NOT** differentially bound?Make screenshots of these different situation a try to get an explanation for each one of these cases.


