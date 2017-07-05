# Introduction

NOTE: Acknowledge exploratory nature of study 
1. A description of the high-level domain / environment
2. A key problem that happens in this high-level domain
3. Current solutions to that key problem
4. A problem with the current solutions
5. A glimpse at how you solve the problem in (4)
6. An overview of your evaluation / experiment results

1. Debugging is a time-consuming process. Show facts that support this statement. For this reason, we would like to reduce time spent on debugging. Reducing time spent on debugging can significantly reduce cost.
2. State-of-the-art research is looking into automated debugging techniques. Currently, a prominent technique is spectrum-based fault localization, which heavily relies on the quality of the test suites that are optimized with regards to adequacy measurements that focus on error detection.
3. However, Perez et al. show evidence that optimizing a test suite for diagnosability improves performance of automated debugging techniques. Perez et al. proposed DDU to quantify the diagnosability. The goal of DDU is to capture diagnosability and could possibly serve as a complementary metric that measures the quality of the test suite.
4. Currently, DDU is just a value in the domain [0, 1], but this does not help the developer in writing better tests. For example, what should the developer do when the DDU is 0.1? In short, we strive to make DDU more practical, just like how code coverage is nowadays shown to developers.
5. To be able to make DDU more practical, we first need to obtain a deeper understanding of DDU. Therefore, this study will mostly be exploratory. We start off with a case study on DDU in open source projects.
6. Contributions of this study:
      - A case study with real project of how DDU and its individual components are affected by different kinds of tests.
      - Empirical evidence that DDU is not correlated with diagnosability .
      - Empirical evidence that density is correlated with error detection.
7. Structure of report.

Contributions of this study:

1. A case study with real project of how DDU and its individual components are affected by different kinds of tests. 
2. Empirical evidence that DDU is not correlated with diagnosability.
3. Empirical evidence that density is correlated with error detection.

# Background
1. Spectrum-based reasoning: Barinel
2. Evaluation of diagnosis: wasted effort
3. Diagnosability: the property of faults to be easily and precisely located
4. Diagnosability metric:
      - Entropy
      - DDU
          - Density
          - Diversity
          - Uniqueness
5. Error detection

# Research Questions
RQ1: What kind of values do density, diversity, uniqueness, and DDU take on in open source software?
RQ2: What is the relation between density, diversity, uniqueness, and DDU and diagnosability in open source software?
RQ3: What is the relation between density, diversity, uniqueness, and DDU and test coverage in open source software?
RQ4: What kinds of tests have positive or negative effects on density, diversity, uniqueness, and DDU?

Motivate case study
Approach
  - Selection of open source projects
How does normalized density vary among projects?
How does diversity vary among projects?
How does uniqueness vary among projects?
How does DDU vary among projects?

OPTIONAL:
How to write tests to optimize DDU?
  - How does this work for multiple components faults?

1. In this chapter, we perform a case study on DDU in open source projects. First, we describe the approach used for this case study and the selection criteria. Then, we explore how DDU and its individual components vary as a consequence to types of tests. 
2. Approach:
      - In this case study, we are interested in how DDU varies as a consequence to types of tests. Getting a better understanding of what kinds of tests affect DDU and its individual components 
      - Selection criteria:
          - Executable test suite
          - Maven project
3. 

Experiment A: Does DDU correlate with wasted effort?
  - Motivation
  - Approach, experimental setup
  - Does DDU correlate with wasted effort?
      1. Explain outliers; outliers are caused by classes with many components
      2. Normalized wasted effort does show correlation
      3. How does wasted effort correlate with effort when we control for erroneous matrices?
      4. No correlation, that is a bummer
      5. What caused the correlation when we don't filter out non-erroneous matrices?
          - Error detection seems to be lower bounded by DDU.
          - What causes error detection to be lower bounded by DDU?
              - Density? Diversity? Uniqueness? Transaction that cover almost all components?
