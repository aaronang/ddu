# Experiment

The goal of this experiment is to verify that DDU does indeed result in a better fault diagnosis.


## Approach

1. Select activity matrices with at least `8` components.
1. For each matrix:
    1. Generate multiple candidate sets with a particular cardinality.
    1. For each candidate set:
        1. Generate modify error vector where health probability equals `0`.
        1. Generate activity matrix for Barinel.
        1. Compute effort.
    1. Average effort.
