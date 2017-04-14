# Experiment

The goal of this experiment is to verify that DDU does indeed result in a better fault diagnosis.
Specifically, in this experiment, we would like to answer the two following questions:

>**TODO: The following questions must be rephrased more clearly.**

1. >Given a spectra and manually generated fault candidates that only cause a failure when executed together in a transaction, does a higher DDU matrix identify more generated fault candidates than matrices with a lower DDU? 

    The intuition behind the first question is that a matrix with a higher DDU will most likely have at least one failing transaction for any generated fault candidate, and thus a better diagnosability.
    For example, in the matrix below, when the fault candidate is `{c1, c2}` (a failure caused by multiple components), we obtain error vector `e1`.
    The failure that is caused by components `c1` and `c2` is not caught by the following test suite.
    However, when the fault candidate is `{c1, c3}`, then we obtain error vector `e2`, which includes a failing transaction that is caught by the test suite.
    Since there are three components, there are only three possible candidate sets of cardinality 2, namely `{c1, c2}`, `{c2, c3}`, and `{c1, c3}`.
    Given these three fault candidates, the test suite is able to catch a failure in `33%` of the possible candidate sets.

    ||c1|c2|c3|e1|e2|
    ---|---|---|---|---|---|
    t1|1|0|1|0|1|
    t2|0|1|0|0|0|
    t3|0|0|1|0|0|

    The hypothesis is that when the DDU of a test suite is high, then the percentage of diagnosable fault candidates will be high.
    Vice versa, when the DDU of a test suite is low, then the percentage of diagnosable fault candidates will be low.

2. >How is wasted effort related to DDU?

    The DDU metric was proposed to quantify the diagnosability of the test suite.
    Therefore, the hypothesis is that when the DDU is high, the average wasted effort will be low.
    Accordingly, when the DDU is low, the average wasted effort will be high.


## Approach

1. Select activity matrices with at least `8` components.
1. For each matrix:
    1. Generate multiple candidate sets with a particular cardinality.
    1. For each candidate set:
        1. Generate modify error vector where health probability equals `0`.
        1. Generate activity matrix for Barinel.
        1. Compute effort.
    1. Average effort.

To answer the questions described above, we make use of five open source projects, namely: `commons-csv`, `commons-text`, `commons-io`, `guice`, `jsoup`.
First, we collect spectra for all classes that have at least `8` components, i.e. methods.
For each class spectra excluding its error vector we generate a random fault candidate of cardinality `2`.
Then, we can compute for each transaction whether it fails or passes, i.e. compute the error vector.
We do this process of generating a fault candidate and computing the error vector `20` times, resulting in `20` activity matrices with identical activity but different error vectors.
For each spectra with the newly computed error vector we check if the spectra contains a failing transaction.
Essentially, we check whether the test suite for a given class is able to catch any random fault candidate.
Finally, we compute the percentage of generated fault candidates that were caught by the test suite.

The second question can be answered by computing the average wasted effort for the twenty generated activity matrices, and average the average wasted efforts.
In addition, we compute the average of average wasted efforts only for activity matrices that have at least one failing transaction.

## Results

![](img/ddu_faulty_spectra.png)

![](img/ddu_average_wasted_effort.png)